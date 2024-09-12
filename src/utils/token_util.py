import base64
import time
from datetime import timedelta, datetime, timezone
from typing import Union

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing_extensions import Annotated

from src.config import Config
from src.utils.repository_util import RepositoryUtil

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenUtil:
    def __init__(self):
        self.__config = Config()
        self.__secrets = self.__config.get_secrets()
        self.__repository = RepositoryUtil()

    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None) -> str:
        encode_data = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(hours=1)
        encode_data.update({"exp": expire})
        return jwt.encode(encode_data, self.__secrets["secret_key"], algorithm=self.__secrets["hash_alg"])

    def get_user_info(self, token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
        try:
            payload = jwt.decode(token, self.__secrets.get("secret_key"), algorithms=self.__secrets.get("hash_alg"))

            if int(payload["exp"]) < int(time.time()):
                return {"valid": False}

            user_exist = self.__repository.find_user_by_id(payload["id"])
            if user_exist is None:
                return {"valid": False}

            return {"valid": True, "user_id": payload["id"]}
        except Exception as e:
            print(str(e))
            return {"valid": False}


    def verify_internal_api_key(self, api_key: str) -> bool:
        try:
            decoded_key = base64.b64decode(api_key.encode("utf-8")).decode("utf-8")
            if decoded_key == self.__secrets.get("server_key"):
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False

    def generate_api_key(self, code: str) -> str:
        encoded_key = f"{self.__config.get_secrets().get('secret_key')}_{code}".encode("utf-8")
        api_key = base64.b64encode(encoded_key)

        return api_key.decode("utf-8")

    def verify_restaurant_api_key(self, code:str, api_key: str) -> dict:
        try:
            restaurant = self.__repository.find_restaurant_by_code(code)
            if not restaurant:
                return {"valid": False}

            decoded_key = base64.b64decode(api_key.encode("utf-8")).decode("utf-8")
            decoded_restaurant_api_key = base64.b64decode(restaurant.api_key.encode("utf-8")).decode("utf-8")
            if decoded_key == decoded_restaurant_api_key:
                return {"valid": True, "id": restaurant.id}
            else:
                return {"valid": False }
        except Exception as e:
            print(e)
            return {"valid": False}
from typing import Optional

from src.features.employees.authentication.generate_access_token.repository import GenerateAccessTokenRepository
from src.features.employees.authentication.generate_access_token.request import TokenRequest
from src.features.employees.authentication.generate_access_token.response import TokenResponse
from src.utils.password_util import PasswordUtil
from src.utils.token_util import TokenUtil


class GenerateAccessTokenUseCase:
    def __init__(self):
        self.__token_util = TokenUtil()
        self.__repository = GenerateAccessTokenRepository()
        self.__password_util = PasswordUtil()

    def generate_access_token(self, data: TokenRequest) -> Optional[TokenResponse]:
        user_exist = self.__repository.find_user(data.email)
        if user_exist:
            verify_password = self.__password_util.verify_password(data.password, user_exist.password)
            if verify_password:
                token_data = {
                    "id": user_exist.id,
                    "name": user_exist.name,
                    "email": user_exist.email
                }
                return TokenResponse(access_token=self.__token_util.create_access_token(data=token_data), token_type="Bearer")
            return None
        else:
            return None

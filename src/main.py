import mimetypes
from copyreg import pickle
from datetime import datetime
from typing import Union

from fastapi import FastAPI, Header, status, HTTPException, UploadFile
from fastapi.openapi.models import HTTPBearer
from fastapi.params import Depends, Path
from fastapi.security import APIKeyHeader
from typing_extensions import Annotated

from src.features.employees.authentication.generate_access_token.request import TokenRequest
from src.features.employees.authentication.generate_access_token.usecase import GenerateAccessTokenUseCase
from src.features.employees.authentication.token_validation.usecase import TokenValidationUseCase
from src.features.employees.create_employee.request import CreateEmployeeRequest
from src.features.employees.create_employee.usecase import CreateEmployeeUseCase
from src.features.restaurants.create_menu.usecase import CreateMenuUsaCase
from src.features.restaurants.create_restaurant.request import CreateRestaurantRequest
from src.features.restaurants.create_restaurant.usecase import CreateRestaurantUseCase
from src.features.restaurants.retrieve_menu.usecase import RetrieveMenuUseCase
from src.features.restaurants.vote_menu.request import VoteMenuRequest
from src.features.restaurants.vote_menu.usecase import VoteMenuUseCase
from src.utils.token_util import TokenUtil

app = FastAPI()

api_key_scheme = APIKeyHeader(name="x-api-key")
api_version_scheme = APIKeyHeader(name="x-api-version")
bearer_scheme = HTTPBearer()
token_util = TokenUtil()

@app.get("/")
def greetings():
    return {"message": "Hello"}

# Endpoint for employees operation
@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: CreateEmployeeRequest, api_key: str = Depends(api_key_scheme)):
    valid_key = token_util.verify_internal_api_key(api_key)
    if valid_key:
        usecase = CreateEmployeeUseCase()
        result = usecase.create(employee)
        if not result:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create employee")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

# Endpoints for restaurants operation
@app.post("/restaurants", status_code=status.HTTP_201_CREATED)
def create_restaurant(restaurant: CreateRestaurantRequest, api_key: str = Depends(api_key_scheme)):
    valid_key = token_util.verify_internal_api_key(api_key)
    if valid_key:
        usecase = CreateRestaurantUseCase()
        result = usecase.create(restaurant)
        if not result:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create restaurant")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/restaurants/{restaurant_code}/menus", status_code=status.HTTP_201_CREATED)
def upload_menu(menu: UploadFile, restaurant_code: Annotated[str, Path(title="The external ID of restaurant")], api_key: str = Depends(api_key_scheme)):
    valid_key = token_util.verify_restaurant_api_key(restaurant_code, api_key)
    if valid_key.get("valid", False):
        if menu.content_type != mimetypes.types_map.get(".csv"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file format. Must be a csv file")

        usecase = CreateMenuUsaCase()
        result = usecase.create(menu, valid_key.get("id"), restaurant_code)
        if not result:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to upload menu")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid restaurant credential")

@app.get("/menus")
def get_menu_by_date(date: datetime, authorization: Annotated[Union[str, None], Header()]):
    authorization_arr = authorization.split(" ")
    valid_token = token_util.get_user_info(authorization_arr[1])
    if not valid_token.get("valid"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    usecase = RetrieveMenuUseCase()
    return usecase.get_menus_by_date(date)

@app.post("/menus/vote", status_code=status.HTTP_201_CREATED)
def vote_menu(votes: list[VoteMenuRequest], authorization: Annotated[Union[str, None], Header()], api_version: str = Depends(api_version_scheme)):
    authorization_arr = authorization.split(" ")
    valid_token = token_util.get_user_info(authorization_arr[1])
    if not valid_token.get("valid"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    str_api_version = str(api_version)
    if str_api_version == "1.0":
        if len(votes) != 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Can only vote 1 menu")

        usecase = VoteMenuUseCase()
        result = usecase.vote_menu(votes, valid_token.get("user_id"), str_api_version)
        if not result.get("valid"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result.get("detail"))
    elif str_api_version == "2.0":
        usecase = VoteMenuUseCase()
        result = usecase.vote_menu(votes, valid_token.get("user_id"), str_api_version)
        if not result.get("valid"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result.get("detail"))
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="API version is not supported")

# Endpoints for authentication
@app.post("/access_token")
def generate_access_token(data: TokenRequest):
    usecase = GenerateAccessTokenUseCase()
    access_token = usecase.generate_access_token(data)
    if access_token:
      return access_token

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")


@app.post("/validate_token")
def validate_access_token(authorization: Annotated[Union[str, None], Header()]):
    usecase = TokenValidationUseCase()
    response = usecase.validate_token(authorization)
    return response

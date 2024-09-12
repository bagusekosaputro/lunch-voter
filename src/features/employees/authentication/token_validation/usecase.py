from src.features.employees.authentication.token_validation.repository import TokenValidationRepository
from src.utils.token_util import TokenUtil


class TokenValidationUseCase:
    def __init__(self):
        self.__token_util = TokenUtil()
        self.__repository = TokenValidationRepository()

    def validate_token(self, token:str) -> bool:
        user_info = self.__token_util.get_user_info(token)

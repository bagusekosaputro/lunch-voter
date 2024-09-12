import bcrypt

from src.config import Config


class PasswordUtil:
    def __init__(self):
        self.__config = Config()
        self.__config = self.__config.get_secrets()

    def hash_password(self, password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode("utf-8")

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

import os


class Config:
    def __init__(self):
        self.__environment = os.environ["ENV"]
        self.__db_host = os.environ["DB_HOST"]
        self.__db_name = os.environ["DB_NAME"]
        self.__db_user = os.environ["DB_USER"]
        self.__db_pass = os.environ["DB_PASSWORD"]
        self.__server_key = os.environ["SERVER_KEY"]
        self.__secret_key = os.environ["SECRET_KEY"]
        self.__hash_alg = os.environ['SECRET_ALG']

    def get_environment(self) -> str:
        return self.__environment

    def get_dsn(self) -> str:
        # return f"dbname='{self.__db_name}' user='{self.__db_user}' host='{self.__db_host}' password='{self.__db_pass}'"
        return f"postgresql://{self.__db_user}:{self.__db_pass}@{self.__db_host}/{self.__db_name}"

    def get_secrets(self) -> dict:
        return {
            "secret_key": self.__secret_key,
            "server_key": self.__server_key,
            "hash_alg": self.__hash_alg
        }

from sqlalchemy import Engine

from src.config import Config
from sqlmodel import create_engine


class DBConnection:
    def __init__(self):
        self.__config = Config()

    def create_connection(self) -> Engine:
        try:
            return create_engine(self.__config.get_dsn())
        except Exception as e:
            raise e

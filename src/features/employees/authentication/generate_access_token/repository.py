from sqlmodel import Session, select

from src.features.employees.model import Employees
from src.utils.db_conn import DBConnection


class GenerateAccessTokenRepository:
    def __init__(self):
        self.__db_conn = DBConnection()

    def find_user(self, email: str) -> bool:
        with Session(self.__db_conn.create_connection()) as session:
            query = select(Employees).where(Employees.email == email)
            result = session.exec(query).first()
            
            return result

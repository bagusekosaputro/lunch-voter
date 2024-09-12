from typing import Optional

from sqlmodel import Session, select

from src.features.employees.model import Employees
from src.utils.db_conn import DBConnection


class TokenValidationRepository:
    def __init__(self):
        self.__db_conn = DBConnection()

    def find_user(self, user_id: Optional[int] = None, email: Optional[str] = None):
        with Session(self.__db_conn.create_connection()) as session:
            if user_id is not None:
                query = select(Employees).where(Employees.id == user_id)
            elif email is not None:
                query = select(Employees).where(Employees.email == email)
            else:
                return None
            result = session.exec(query)
            return result

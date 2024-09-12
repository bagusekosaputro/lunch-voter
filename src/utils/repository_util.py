from cgitb import reset

from dns.e164 import query
from sqlalchemy.testing.suite.test_reflection import users
from sqlmodel import Session, select

from src.features.employees.model import Employees
from src.features.restaurants.restaurant_model import Restaurants
from src.utils.db_conn import DBConnection


class RepositoryUtil:
    def __init__(self):
        self.__db_conn = DBConnection()


    def find_restaurant_by_code(self, code: str):
        with Session(self.__db_conn.create_connection()) as session:
            query = select(Restaurants).where(Restaurants.restaurant_code == code)
            return session.exec(query).first()

    def find_user_by_id(self, user_id: int):
        with Session(self.__db_conn.create_connection()) as session:
            query = select(Employees).where(Employees.id == user_id)
            return session.exec(query).first()
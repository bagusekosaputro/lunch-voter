from datetime import datetime
from sqlmodel import Session, select

from src.features.restaurants.menu_model import Menus
from src.features.restaurants.restaurant_model import Restaurants
from src.utils.db_conn import DBConnection


class RetrieveMenuRepository:
    def __init__(self):
        self.__db_conn = DBConnection()

    def find_menus_by_date(self, menu_date: datetime) -> list:
        with Session(self.__db_conn.create_connection()) as session:
            query = select(Menus).where(Menus.menu_date == menu_date)
            return session.exec(query).all()

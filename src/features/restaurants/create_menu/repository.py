from sqlmodel import Session

from src.features.restaurants.menu_model import Menus
from src.utils.db_conn import DBConnection


class CreateMenuRepository:
    def __init__(self):
        self.__db_conn = DBConnection()

    def insert_menu(self, data: Menus):
        with Session(self.__db_conn.create_connection()) as session:
            session.add(data)
            session.commit()

        session.close()

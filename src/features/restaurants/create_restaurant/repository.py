from sqlmodel import Session

from src.features.restaurants.restaurant_model import Restaurants
from src.utils.db_conn import DBConnection


class CreateRestaurantRepository:
    def __init__(self):
        self.__db_conn = DBConnection()

    def insert_restaurant(self, data: Restaurants):
        with Session(self.__db_conn.create_connection()) as session:
            session.add(data)
            session.commit()

        session.close()

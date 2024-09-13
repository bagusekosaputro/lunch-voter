from datetime import datetime

from sqlmodel import Session, select

from src.features.restaurants.menu_model import Menus
from src.features.restaurants.vote_model import Votes
from src.utils.db_conn import DBConnection


class RetrieveVoteResultRepository:
    def __init__(self):
        self.__db_conn = DBConnection()


    def get_vote_result(self, date: datetime):
        with Session(self.__db_conn.create_connection()) as session:
            query = select(Votes, Menus).join(Menus, isouter=True).where(Votes.vote_date == date)
            return session.exec(query).all()
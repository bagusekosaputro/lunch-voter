from datetime import datetime

from sqlmodel import Session, select

from src.features.restaurants.vote_model import Votes
from src.utils.db_conn import DBConnection


class VoteMenuRepository:
    def __init__(self):
        self.__db_conn = DBConnection()


    def find_user_vote(self, user_id: int):
        with Session(self.__db_conn.create_connection()) as session:
            query = select(Votes).where(Votes.employee_id == user_id).where(Votes.vote_date == datetime.now().strftime("%Y-%m-%d"))
            return session.exec(query).first()

    def insert_vote(self, data: Votes):
        with Session(self.__db_conn.create_connection()) as session:
            query = session.add(data)
            session.commit()

        session.close()
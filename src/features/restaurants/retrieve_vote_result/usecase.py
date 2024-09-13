from datetime import datetime
from typing import List

from src.features.restaurants.retrieve_vote_result.repository import RetrieveVoteResultRepository
from src.features.restaurants.retrieve_vote_result.response import RetrieveVoteResultResponse


class RetriveVoteResultUseCase:
    def __init__(self):
        self.__repository = RetrieveVoteResultRepository()


    def result(self, vote_date: datetime = datetime.now()) -> dict:
        result = {}
        try:
            votes = self.__repository.get_vote_result(vote_date.strftime("%Y-%m-%d"))
            for vote, menus in votes:
                if result.get(menus.name):
                    result[menus.name] = result.get(menus.name) + vote.vote_point
                else:
                    result[menus.name] = vote.vote_point
        except Exception as e:
            print(e)

        return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

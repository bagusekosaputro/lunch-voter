from datetime import datetime
from typing import Optional, List, Dict

from src.features.restaurants.vote_menu.repository import VoteMenuRepository
from src.features.restaurants.vote_menu.request import VoteMenuRequest
from src.features.restaurants.vote_model import Votes


class VoteMenuUseCase:
    def __init__(self):
        self.__repository = VoteMenuRepository()


    def vote_menu(self, votes: List[VoteMenuRequest], employee_id: int, api_version: str, vote_date: Optional[datetime] = datetime.now()) -> dict:
        vote_exist = self.__repository.find_user_vote(employee_id)
        if vote_exist:
            return {"valid": False, "detail": "You're already vote menu for today"}

        for vote in votes:
            point = 3 if api_version == "1.0" else vote.point
            try:
                data = Votes(menu_id=vote.id, employee_id=employee_id, vote_date=vote_date.strftime("%Y-%m-%d"), created_by=str(employee_id), vote_point=point)
                self.__repository.insert_vote(data)
            except Exception as e:
                print(e)
                return {"valid": False, "detail": "Failed to vote for menu"}

        return {"valid": True}

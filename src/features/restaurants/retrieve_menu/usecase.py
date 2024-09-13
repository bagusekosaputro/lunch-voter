from datetime import datetime

from typing_extensions import Optional

from src.features.restaurants.retrieve_menu.repository import RetrieveMenuRepository
from src.features.restaurants.retrieve_menu.response import RetrieveMenuResponse
from src.utils.token_util import TokenUtil


class RetrieveMenuUseCase:
    def __init__(self):
        self.__token_util = TokenUtil()
        self.__repository = RetrieveMenuRepository()

    def get_menus_by_date(self, menu_date: Optional[datetime] = datetime.now()) -> list:
        menus = self.__repository.find_menus_by_date(menu_date.strftime("%Y-%m-%d"))
        response = []

        for menu in menus:
            response.append(RetrieveMenuResponse(id=menu.id, name=menu.name, description=menu.description, restaurant_code=menu.created_by))

        return response

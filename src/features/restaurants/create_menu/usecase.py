import csv

from fastapi import UploadFile

from src.features.restaurants.create_menu.repository import CreateMenuRepository
from src.features.restaurants.menu_model import Menus
from src.utils.token_util import TokenUtil


class CreateMenuUsaCase:
    def __init__(self):
        self.__token_util = TokenUtil()
        self.__repository = CreateMenuRepository()

    def create(self, menu: UploadFile, restaurant_id: int, restaurant_code: str):
        if menu.size == 0:
            return False
        try:
            with open(menu.filename, "r", newline="\n", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
                next(reader)
                for row in reader:
                    menu_model = Menus(
                        name=row[0],
                        restaurant_id=restaurant_id,
                        description=row[1],
                        menu_date=row[2],
                        created_by=restaurant_code
                    )
                    self.__repository.insert_menu(menu_model)

            return True
        except Exception as e:
            print(str(e))
            return False
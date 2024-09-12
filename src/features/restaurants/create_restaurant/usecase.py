from src.features.restaurants.create_restaurant.repository import CreateRestaurantRepository
from src.features.restaurants.create_restaurant.request import CreateRestaurantRequest
from src.features.restaurants.restaurant_model import Restaurants
from src.utils.token_util import TokenUtil


class CreateRestaurantUseCase:
    def __init__(self):
        self.__repository = CreateRestaurantRepository()
        self.__token_util = TokenUtil()


    def create(self, restaurant: CreateRestaurantRequest):
        try:
            restaurant_code = self.__generate_restaurant_code(restaurant.name)
            restaurant_model = Restaurants(
                name=restaurant.name,
                description=restaurant.description,
                restaurant_code=restaurant_code,
                api_key=self.__token_util.generate_api_key(restaurant_code),
                created_by="admin"
            )

            self.__repository.insert_restaurant(restaurant_model)
            return True
        except Exception as e:
            print(str(e))
            return False

    def __generate_restaurant_code(self, name:str) -> str:
        identifier = "RST"
        if len(name) > 16:
            code = name[:15].upper().replace(" ", "-")
        else:
            code = name.upper().replace(" ", "-")

        return "-".join(["".join(code), identifier])

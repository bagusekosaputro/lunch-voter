from unittest.mock import patch

from src.features.restaurants.create_restaurant.request import CreateRestaurantRequest
from src.features.restaurants.create_restaurant.usecase import CreateRestaurantUseCase
from src.features.restaurants.restaurant_model import Restaurants


class TestCreateRestaurantUseCase:
    @patch("src.features.restaurants.create_restaurant.repository.CreateRestaurantRepository.insert_restaurant")
    @patch("src.utils.token_util.TokenUtil.generate_api_key")
    def test_create_restaurant_succeeded(self, mock_restaurant, mock_api_key):
        mock_api_key.return_value = "asdafsafsfsfdfdfdf"
        mock_restaurant.return_value = Restaurants(id=1, name="yummy resto", restaurant_code="YUMMY-RESTO-RST", api_key=mock_api_key)
        request = CreateRestaurantRequest(name="yummy resto")
        usecase = CreateRestaurantUseCase()
        result = usecase.create(request)

        assert result is True

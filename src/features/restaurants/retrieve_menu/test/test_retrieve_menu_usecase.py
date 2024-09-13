from datetime import datetime
from unittest.mock import patch

from src.features.restaurants.menu_model import Menus
from src.features.restaurants.retrieve_menu.usecase import RetrieveMenuUseCase


class TestRetrieveMenuUseCase:
    @patch("src.features.restaurants.retrieve_menu.repository.RetrieveMenuRepository.find_menus_by_date")
    def test_retrieve_menu_succeeded(self, mock_menus):
        mock_menus.return_value = [Menus(id=1, restaurant_id=1, name="Chicken steak", menu_date=datetime.now().strftime("%Y-%m-%d"))]
        usecase = RetrieveMenuUseCase()
        result = usecase.get_menus_by_date()

        assert len(result) == 1
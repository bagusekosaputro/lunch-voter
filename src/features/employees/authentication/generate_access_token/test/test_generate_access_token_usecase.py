import pytest
from pydantic import ValidationError

from src.features.employees.authentication.generate_access_token.request import TokenRequest
from src.features.employees.authentication.generate_access_token.usecase import GenerateAccessTokenUseCase
from unittest.mock import patch

class TestGenerateAccessToken:
    @patch("src.")
    def test_succeed_generate_access_token(self, monkeypatch):
        usecase = GenerateAccessTokenUseCase()
        data = TokenRequest(id=123, name="John", email="john@example.com")
        result = usecase.generate_access_token(data)

        assert hasattr(result, "access_token")
        assert hasattr(result, "token_type")

    def test_failed_generate_access_token(self):
        usecase = GenerateAccessTokenUseCase()
        with pytest.raises(ValidationError) as excinfo:
            data = TokenRequest(id=123, name="John")
            usecase.generate_access_token(data)

        assert "validation error " in str(excinfo)

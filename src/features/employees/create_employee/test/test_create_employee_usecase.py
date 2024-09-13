from unittest.mock import patch

from src.features.employees.create_employee.request import CreateEmployeeRequest
from src.features.employees.create_employee.usecase import CreateEmployeeUseCase
from src.features.employees.model import Employees


class TestCreateEmployeeUseCase:
    @patch("src.utils.password_util.PasswordUtil.hash_password")
    @patch("src.features.employees.create_employee.repository.CreateEmployeeRepository.insert_employee")
    def test_create_employee_succeeded(self, mock_password_hash, mock_employee):
        mock_password_hash.return_value = "aaaaabbbbccccddd"
        mock_employee.return_value = Employees(id=1, name="John", email="john@mail.com", password="aaaaabbbbccccddd")
        request = CreateEmployeeRequest(name="John", email="john@mail.com", password="abc12345")
        usecase = CreateEmployeeUseCase()
        result = usecase.create(request)

        assert result is True

from src.features.employees.create_employee.repository import CreateEmployeeRepository
from src.features.employees.create_employee.request import CreateEmployeeRequest
from src.features.employees.model import Employees
from src.utils.password_util import PasswordUtil


class CreateEmployeeUseCase:
    def __init__(self):
        self.__repository = CreateEmployeeRepository()
        self.__password_util = PasswordUtil()

    def create(self, employee: CreateEmployeeRequest):
        try:
            hashed_password = self.__password_util.hash_password(employee.password)
            employee_model = Employees(name=employee.name, email=employee.email, password=hashed_password, created_by="admin")

            self.__repository.insert_employee(employee_model)
            return True
        except Exception as e:
            print(str(e))
            return False

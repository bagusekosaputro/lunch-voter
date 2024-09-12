from src.features.employees.model import Employees
from src.utils.db_conn import DBConnection
from sqlmodel import Session


class CreateEmployeeRepository:
    def __init__(self):
        self.__db_conn = DBConnection()

    def insert_employee(self, data: Employees):
        with Session(self.__db_conn.create_connection()) as session:
            session.add(data)
            session.commit()

        session.close()

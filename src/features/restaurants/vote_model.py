from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Votes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    menu_id: int = Field(foreign_key="menus.id")
    employee_id: int = Field(foreign_key="employees.id")
    vote_point: Optional[int] = None
    vote_date: datetime
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
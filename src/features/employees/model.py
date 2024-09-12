from typing import Optional
from sqlmodel import SQLModel, Field


class Employees(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

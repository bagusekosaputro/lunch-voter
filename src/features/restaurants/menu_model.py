from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship



class Menus(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    restaurant_id: int = Field(foreign_key="restaurants.id")
    name: str
    menu_date: datetime
    description: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

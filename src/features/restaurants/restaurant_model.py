from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship



class Restaurants(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    restaurant_code: str
    api_key: str
    description: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

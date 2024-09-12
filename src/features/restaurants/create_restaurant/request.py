from typing import Optional

from pydantic import BaseModel, Field


class CreateRestaurantRequest(BaseModel):
    name: str = Field(min_length=5)
    description: Optional[str] = None
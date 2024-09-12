from typing import Optional

from pydantic import BaseModel


class RetrieveMenuResponse(BaseModel):
    id: int
    name: str
    restaurant_code: Optional[str] = None
    description: Optional[str] = None
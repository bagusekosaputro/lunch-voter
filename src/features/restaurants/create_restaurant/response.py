from pydantic import BaseModel


class CreateRestaurantResponse(BaseModel):
    name: str
    restaurant_code: str
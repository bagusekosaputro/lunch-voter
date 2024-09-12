from pydantic import BaseModel, Field, EmailStr


class CreateEmployeeRequest(BaseModel):
    email: EmailStr
    name: str = Field(min_length=2)
    password: str = Field(min_length=8)

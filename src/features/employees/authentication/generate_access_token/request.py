from pydantic import BaseModel, EmailStr


class TokenRequest(BaseModel):
    password: str
    email: EmailStr

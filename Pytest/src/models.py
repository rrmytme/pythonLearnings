from pydantic import BaseModel, EmailStr, Field

from src.validators import PHONE_NUMBER_REGEX


class Person(BaseModel):
    name: str
    email: EmailStr
    title: str
    phone: str = Field(pattern=PHONE_NUMBER_REGEX)
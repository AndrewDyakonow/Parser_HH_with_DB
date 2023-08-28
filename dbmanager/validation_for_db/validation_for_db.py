from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.class_validators import validator


class Employer(BaseModel):
    name: str | None
    alternate_url: str | None
    id: int


class Metro(BaseModel):
    station_name: str | None
    line_name: str | None


class Address(BaseModel):
    raw: str | None

    @validator('raw')
    @classmethod
    def validate_raw(cls, value):
        if value is None:
            return "Не указан"
        else:
            return value


class Salary(BaseModel):
    from_: int | None = Field(alias='from')
    to: int | None
    currency: str | None

    @validator('from_')
    @classmethod
    def validate_from(cls, value):
        if value is None:
            return None
        else:
            return value

    @validator('to')
    @classmethod
    def validate_to(cls, value):
        if value is None:
            return None
        else:
            return value

    @validator('currency')
    @classmethod
    def validate_currency(cls, value):
        if value is None:
            return "-"
        else:
            return value


class Snippet(BaseModel):
    requirement: str | None
    responsibility: str | None


class Vacanci(BaseModel):
    """Валидация данных"""
    id: int
    name: str | None
    employer: Employer | None
    salary: Salary | None
    address: Address | None
    alternate_url: str | None
    published_at: str | None
    snippet: Snippet | None

    @validator('address')
    @classmethod
    def validate_address(cls, value):
        if value is None:
            return "Не указан"
        else:
            return value

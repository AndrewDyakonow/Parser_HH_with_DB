from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.class_validators import validator


class Employer(BaseModel):
    name: str | None


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
            return 0
        else:
            return value

    @validator('to')
    @classmethod
    def validate_to(cls, value):
        if value is None:
            return 0
        else:
            return value

    @validator('currency')
    @classmethod
    def validate_currency(cls, value):
        if value is None:
            return "-"
        else:
            return value


class Vacancies(BaseModel):
    """Валидация данных"""
    name: str | None
    employer: Employer | None
    salary: Salary | None
    address: Address | None
    alternate_url: str | None
    published_at: str | None

    @validator('address')
    @classmethod
    def validate_address(cls, value):
        if value is None:
            return "Не указан"
        else:
            return value

    def beautiful_output(self):
        """Вывод отвалидированых данных в требуемом формате"""
        return f'Вакансия:         {self.name}\n' \
               f'Организация:      {self.employer.name}\n' \
               f'Зарплата:         от {self.salary.from_ if self.salary.from_ else "-"} до ' \
               f'{self.salary.to if self.salary.to else "-"} {self.salary.currency}\n' \
               f'Адрес:            {self.address.raw if self.address != "Не указан" else "Не указан"}\n' \
               f'Ссылка:           {self.alternate_url}\n' \
               f'Дата размещения:  {self.published_at}\n'

from pydantic import BaseModel
from pydantic.class_validators import validator


class Employer(BaseModel):
    """Валидация"""
    title: str | None
    address: str | None
    link: str | None

    @validator('title')
    @classmethod
    def validate_title(cls, value):
        """Валидация"""
        if value is None:
            return "Не указан"
        else:
            return value

    @validator('address')
    @classmethod
    def validate_address(cls, value):
        if value is None:
            return "Не указан"
        else:
            return value

    @validator('link')
    @classmethod
    def validate_link(cls, value):
        if value is None:
            return "Не указан"
        else:
            return value


class Vacancies_SJ(BaseModel):
    """Валидация данных"""
    profession: str | None
    client: Employer | None
    payment_from: int | None
    payment_to: int | None

    def beautiful_output(self):
        """Вывод отвалидированых данных в требуемом формате"""
        return f'Вакансия:         {self.profession}\n' \
               f'Организация:      {self.client.title}\n' \
               f'Зарплата:         от {self.payment_from if self.payment_from else "-"} до ' \
               f'{self.payment_to if self.payment_to else "-"} "RUB"\n' \
               f'Адрес:            {self.client.address if self.client.address != "Не указан" else "Не указан"}\n' \
               f'Ссылка:           {self.client.link}\n'

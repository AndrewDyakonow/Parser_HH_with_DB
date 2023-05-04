from typing import Dict, List, Any

import requests


class HH_request():
    """Класс запроса вакансий на HH"""
    def __init__(self, text, area=113):
        self.text = text
        self.area = area
        self.url = 'https://api.hh.ru/vacancies'
        self.page = 1

    def get_data(self) -> dict[str, list[Any]]:
        """Запрос"""
        responce = {"items": []}
        for page in range(1, 11):
            respon = requests.get(
                url=self.url,
                params={
                    'text': self.text,
                    'per_page': 50,
                    'page': self.page,
                    'area': self.area,
                    'only_with_salary': True
                },
            )
            self.page += 1

            responce.get('items').extend(respon.json().get("items"))
        return responce

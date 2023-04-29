from app.requests_classes.abstract_class import Servises
import requests
import json


class SJ_request(Servises):
    """Класс запроса вакансий на SJ"""
    def __init__(self, text='python'):
        self.text = text
        self.headers = {
            'X-Api-App-Id':
                'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
        }
        self.params = [
                ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", self.text)]),

                ("period", 0),
                ("count", 100)
        ]
        self.url = 'https://api.superjob.ru/2.0/vacancies/'


    @staticmethod
    def autorization():
        """Метод авторизации"""
        respon = requests.get(
            url=f'https://api.superjob.ru/2.0/oauth2/password/',
            headers={
                'X-Api-App-Id':
                    'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
            },
            params={
                'login': 'dronramone@mail.ru',
                'password': 'Created_1990',
                'client_id': '2265',
                'client_secret':
                    'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
            }
        )
        print(respon.text)

    def get_data(self) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=self.url,
            headers=self.headers,
            params=self.params,
        )
        return respon.json()

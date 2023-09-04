from Parser.app.requests_classes.HH_request_class.HH_class_request import HHrequest
from main.models import Vacancies
from django.db.utils import IntegrityError


def requests(keyword):
    ex_request = HHrequest(keyword)
    data = ex_request.get_data()
    create_vacancy(data['items'])


def create_vacancy(data_list):
    for_create = []
    for data in data_list:
        for_create.append(
            {
                'id_vacancy': data.get('employer').get('id'),
                'name_company': data.get('employer').get('name'),
                'name_vacancy': data.get('name'),
                'adress': None if data.get('address') is None else data.get('address').get('raw'),
                'url': data.get('url'),
                'salary': None if data.get('salary') is None else data.get('salary').get('to'),
                'requirement': data.get('snippet').get('requirement'),
                'responsibiliti': data.get('snippet').get('responsibiliti'),
                'date_created': data.get('published_at'),
            }
        )
    for obj in for_create:
        try:
            Vacancies.objects.create(**obj)
        except IntegrityError:
            print('Уже есть')
            continue

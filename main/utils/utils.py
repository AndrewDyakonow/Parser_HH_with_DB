from Parser.app.requests_classes.HH_request_class.HH_class_request import HHrequest
from main.models import Vacancies
from django.db.utils import IntegrityError


def requests(keyword):
    ex_request = HHrequest(keyword)
    data = ex_request.get_data()
    print(len(data['items']))
    create_vacancy(data['items'])


def create_vacancy(data_list):
    for_create = []
    for data in data_list:
        for_create.append(
            {
                'id_vacancy': data.get('employer').get('id'),
                'name_company': data.get('employer').get('name'),
                'name_vacancy': data.get('name'),
                'adress': data.get('area').get('name'),
                'url': data.get('alternate_url'),
                'salary_from': None if data.get('salary') is None else data.get('salary').get('from'),
                'salary_to': None if data.get('salary') is None else data.get('salary').get('to'),
                'requirement': data.get('snippet').get('requirement'),
                'responsibiliti': data.get('snippet').get('responsibiliti'),
                'date_created': data.get('published_at'),
            }
        )

    for obj in for_create:
        try:
            Vacancies.objects.create(**obj)
        except IntegrityError:
            continue

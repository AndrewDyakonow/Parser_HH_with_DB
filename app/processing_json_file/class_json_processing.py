from app.requests_classes.HH_request_class.HH_class_request import HH_request
from app.requests_classes.SJ_request_class.SJ_request_class import SJ_request
import json
from app_interface.user_exception import ErrorServiceName


class JsonProcessing:
    """Класс для создания, заполнения и чтения файла"""
    Urls = 'side_file/result.json'
    json_file_name = 'side_file/result.json'

    @classmethod
    def create_file(cls, text, servise_name) -> None:
        """Сохранение файлов в json"""
        with open(cls.json_file_name, 'w', encoding='utf-8') as file:
            if servise_name == "Head Hunter":
                ex_data = HH_request(text)
            elif servise_name == "Super Job":
                ex_data = SJ_request(text)
            else:
                raise ErrorServiceName
            data = ex_data.get_data()
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_data_from_json(cls):
        """Прочитать файл .json"""
        with open(cls.json_file_name, 'r', encoding='utf-8') as vacancies:
            return json.load(vacancies)

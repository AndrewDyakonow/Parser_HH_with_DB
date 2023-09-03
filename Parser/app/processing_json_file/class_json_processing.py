from app.requests_classes.HH_request_class.HH_class_request import HHrequest
import json


class JsonProcessing:
    """Класс для создания, заполнения и чтения файла"""
    Urls = 'side_file/result.json'
    json_file_name = 'side_file/result.json'

    @classmethod
    def create_file(cls, text) -> None:
        """Сохранение файлов в json"""
        with open(cls.json_file_name, 'w', encoding='utf-8') as file:
            ex_data = HHrequest(text)
            data = ex_data.get_data()
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_data_from_json(cls):
        """Прочитать файл .json"""
        with open(cls.json_file_name, 'r', encoding='utf-8') as vacancies:
            return json.load(vacancies)

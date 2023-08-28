from app.processing_json_file.class_json_processing import JsonProcessing
from app.processing_data.processing_data import ProcessingData
from app_dialog.user_exception import ErrorNotData
from app.validation.validation_HH import Vacancies


class Dialog:

    @staticmethod
    def first_dialog():
        """Вывод приветствия"""
        print('Здравствуйте!\nВас приветствует парсер вакансий Head Hunter')
        print('Для продолжения нажмите ENTER')
        input()

    @staticmethod
    def second_dialog():
        """Диалог по базе данных"""

    @staticmethod
    def input_key():
        """Ввод ключевого слова"""
        print('Введите слово или фразу для поиска\n')
        input_word = True

        while input_word:
            word = input()
            if word != '':
                input_word = False
            else:
                print('Нужно ввести хоть что-нибудь')
        return word

    @staticmethod
    def requests(word):
        try:
            JsonProcessing.create_file(word)
            list_vacancies = ProcessingData.get_vacancies_list(Vacancies)
            if len(list_vacancies) == 0:
                raise ErrorNotData
            else:
                for vacancies in list_vacancies:
                    print(vacancies.beautiful_output() + f'\n{"=" * 50}\n')
                    pass
        except ErrorNotData:
            print("Отсутствуют вакансии по указанному ключевому слову")
        return list_vacancies

    @staticmethod
    def sort(list_vacancies):
        sort = sorted(list_vacancies, key=lambda d: (d.salary.to, d.salary.from_))
        for element in sort:
            print(element.beautiful_output() + f'\n{"=" * 50}\n')

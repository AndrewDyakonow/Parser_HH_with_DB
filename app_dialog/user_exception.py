class UserError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class ErrorServiceName(UserError):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Не выбран сервис!'

    def __str__(self):
        return self.message


class ErrorChoiceTag(UserError):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Не выбрано слово для поиска!'

    def __str__(self):
        return self.message


class ErrorNotData(UserError):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'По указанным параметром нет вакансий'

    def __str__(self):
        return self.message


class ErrorNotDataForTop(UserError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Нет данных для сортировки!'

    def __str__(self):
        return self.message


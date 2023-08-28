from app_dialog.class_dialog import Dialog
from dbmanager.dbManager_class import DBManager


def dialog_one():
    """Диалог с пользователем № 1"""
    prog = None
    Dialog.first_dialog()

    while prog != "q":
        word = Dialog.input_key()
        list_vacancies: list = Dialog.requests(word)
        if len(list_vacancies) == 0:
            prog = input('Вы можете попробовать ввести новые слово или фразу для поиска, или ввести "Q" для выхода')
        else:
            prog = "q"
    sort = input('Наберите "1", если требуется сортировка')

    if sort == '1':
        Dialog.sort(list_vacancies)


def dialog_two():
    """Диалог с пользователем # 2"""
    db_data = DBManager()
    db_data.create_db()
    db_data.create_table()
    db_data.filling_db()
    db_data.filling_db_table()

    print()
    print('База данных создана и заполнена!')
    print("Вы можете поиграть с запросами, просто нажмите цифру на клавиатуре и нажмите 'ENTER'")

    print("0 - Закончить работу")
    print("1 - Получить список всех компаний и количество вакансий у каждой компании.")
    print("2 - Получить список всех вакансий с указанием названия компании,\
    названия вакансии и зарплаты и ссылки на вакансию.")
    print("3 - Получить среднюю зарплату по вакансиям.")
    print("4 - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.")
    print("5 - Получить список всех вакансий, в названии которых\
    содержатся переданные в метод слова")

    while True:

        try:
            user_choice = int(input('Выберите номер запроса или 0 для выхода: '))
            if 0 > user_choice or user_choice > 5:
                print('Такого запроса нет! Выберите другое значение!')
            elif user_choice == 0:
                break
            else:
                choise_request(user_choice, db_data)
        except ValueError:
            print("Введите цифру от 1 до 5")


def choise_request(user_choice, db_data):
    """Выбор запроса"""
    choice = {
        1: db_data.get_companies_and_vacancies_count,
        2: db_data.get_all_vacancies,
        3: db_data.get_avg_salary,
        4: db_data.get_vacancies_with_higher_salary,
    }

    if user_choice == 5:
        search_in_db(db_data)
    else:
        choice.get(user_choice)()


def search_in_db(db_data):
    while True:
        word = input('Введите слово для поиска: ')
        if word:
            db_data.get_vacancies_with_keyword(word.lower())
            break
        else:
            print("Попробуй ещё! ")

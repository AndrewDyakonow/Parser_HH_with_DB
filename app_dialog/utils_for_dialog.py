from app_dialog.class_dialog import Dialog


def dialog_one():
    """Диалог с пользователем"""
    global list_vacancies
    prog = None
    Dialog.first_dialog()

    while prog != "q":
        word = Dialog.input_key()
        list_vacancies = Dialog.requests(word)
        if len(list_vacancies) == 0:
            prog = input('Вы можете попробовать ввести новые слово или фразу для поиска, или ввести "Q" для выхода')
        else:
            prog = "q"
    sort = input('Наберите "1", если требуется сортировка')

    if sort == '1':
        Dialog.sort(list_vacancies)

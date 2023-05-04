from app_dialog.utils_for_dialog import dialog_one
from dbmanager.dbManager_class import DBManager


def main():
    dialog_one()
    a = DBManager()
    a.create_db()
    a.create_table()


if __name__ == '__main__':
    main()

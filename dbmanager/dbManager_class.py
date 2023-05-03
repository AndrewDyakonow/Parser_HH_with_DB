

class DBManager:
    __db_object = None

    def __new__(cls):
        if cls.__db_object is None:
            cls.__db_object = super().__new__(cls)
        return cls.__db_object




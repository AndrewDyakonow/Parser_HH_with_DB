import psycopg2
from psycopg2 import errors
from app.processing_data.processing_data import ProcessingData
from dbmanager.validation_for_db.validation_for_db import Vacanci

import config


class DBManager:
    __db_object = None

    def __new__(cls):
        if cls.__db_object is None:
            cls.__db_object = super().__new__(cls)
        return cls.__db_object

    def __init__(self):
        self.db_name = 'course_work_5_db'
        self.list_vacancies = ProcessingData.get_vacancies_list(Vacanci)

    def create_db(self):
        """Создание базы данных"""
        connector = psycopg2.connect(dbname='postgres', **config.get_config_db())
        connector.autocommit = True
        cursor = connector.cursor()

        try:
            cursor.execute(f'DROP DATABASE {self.db_name}')
            print('Удаляем старую базу данных')
        except psycopg2.errors.InvalidCatalogName:
            print('Создаём новую базу данных')
        finally:
            cursor.execute(f'CREATE DATABASE {self.db_name}')
            cursor.close()
            connector.close()

    def create_table(self):
        """Создание таблиц в БД"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        with connector.cursor() as cursor:
            cursor.execute("""
                    CREATE TABLE company 
                    (
                        id_company      int PRIMARY KEY,
	                    name_company    text UNIQUE NOT NULL,
	                    url             text,
	                    adress          text
                    )
                """)

        with connector.cursor() as cursor:
            cursor.execute("""
                                CREATE TABLE vacancy 
                    (
                        id_vacancy      int PRIMARY KEY,
	                    name_company    varchar(32) REFERENCES company (name_company) NOT NULL,
						name_vacancy	varchar(32) NOT NULL,
						adress			varchar(100),
	                    url             varchar(80),
	                    salary_from		integer,
						salary_to		integer,
						requirement		text,
						responsibiliti 	text
                    );
                                """)
        connector.commit()
        connector.close()

        self.filling_db()

    def filling_db(self):
        """Заполнение базы данных данными"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            for data in self.list_vacancies:

                try:
                    if data.address == 'Не указан':
                        address = None
                    else:
                        address = data.address.raw
                    cursor.execute(
                        '''
                        INSERT INTO company (id_company, name_company, url, adress) 
                        VALUES (%s, %s, %s, %s)
                        ''',
                        (data.employer.id, data.employer.name, data.employer.alternate_url, address)
                    )
                except psycopg2.errors.UniqueViolation:
                    continue

        connector.commit()
        connector.close()

    def get_companies_and_vacancies_count(self):
        """Получить список всех компаний и количество вакансий у каждой компании."""

    def get_all_vacancies(self):
        """
        Получить список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """

    def get_avg_salary(self):
        """Получить среднюю зарплату по вакансиям."""

    def get_vacancies_with_higher_salary(self):
        """Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

    def get_vacancies_with_keyword(self):
        """Получить список всех вакансий, в названии которых
        содержатся переданные в метод слова, например “python”."""

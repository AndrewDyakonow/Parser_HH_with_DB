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

    def create_db(self) -> None:
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

    def create_table(self) -> None:
        """Создание таблиц в БД"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        with connector.cursor() as cursor:
            cursor.execute("""
                    CREATE TABLE company 
                    (
                        id_company      int PRIMARY KEY,
	                    name_company    varchar(125) UNIQUE NOT NULL,
	                    url             text,
	                    adress          text
                    )
                """)

        with connector.cursor() as cursor:
            cursor.execute("""
                                CREATE TABLE vacancy 
                    (
                        id_vacancy      int PRIMARY KEY,
	                    name_company    text REFERENCES company (name_company) NOT NULL,
						name_vacancy	text NOT NULL,
						adress			text,
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
        self.filling_db_table()

    def filling_db(self) -> None:
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

    def filling_db_table(self) -> None:
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
                        INSERT INTO vacancy 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ''',
                        (
                            data.id,
                            data.employer.name,
                            data.name,
                            address,
                            data.alternate_url,
                            data.salary.from_,
                            data.salary.to,
                            data.snippet.requirement,
                            data.snippet.responsibility,
                        )
                    )
                except psycopg2.errors.UniqueViolation:
                    continue

        connector.commit()
        connector.close()

        self.get_companies_and_vacancies_count()

    def get_companies_and_vacancies_count(self):
        """Получить список всех компаний и количество вакансий у каждой компании."""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            cursor.execute(
                """ 
                    SELECT name_company, COUNT (vacancy.name_company) AS count_vacancy
                    FROM company
                    INNER JOIN vacancy USING (name_company)
                    GROUP BY company.name_company
                    ORDER BY count_vacancy DESC
                    LIMIT 20
                """
            )
            mobile_records = cursor.fetchall()

            print(mobile_records)


        connector.commit()
        connector.close()

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

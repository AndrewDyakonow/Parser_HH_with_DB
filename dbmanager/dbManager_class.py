import psycopg2
from psycopg2 import errors
from app.processing_data.processing_data import ProcessingData
from dbmanager.validation_for_db.validation_for_db import Vacanci
from dbmanager.dbmanager_utils import get_avg_salary

import config


class DBManager:

    def __init__(self):
        self.db_name = 'course_work_5_db'
        self.list_vacancies = ProcessingData.get_vacancies_list(Vacanci)
        self.avg_salary = None

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
	                    name_company    text REFERENCES company (name_company) NOT NULL,
						name_vacancy	text NOT NULL,
						adress			text,
	                    url             varchar(80),
	                    salary		    int,
						requirement		text,
						responsibiliti 	text
                    );
                                """)
        connector.commit()
        connector.close()

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

                    salary = get_avg_salary(data.salary.from_, data.salary.to)

                    cursor.execute(
                        '''
                        INSERT INTO vacancy 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ''',
                        (
                            data.id,
                            data.employer.name,
                            data.name,
                            address,
                            data.alternate_url,
                            salary,
                            data.snippet.requirement,
                            data.snippet.responsibility,
                        )
                    )
                except psycopg2.errors.UniqueViolation:
                    continue

        connector.commit()
        connector.close()

    def get_companies_and_vacancies_count(self, **kwargs):
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
                    ORDER BY count_vacancy ASC
                """
            )

            self.__output_request(cursor.fetchall())

        connector.commit()
        connector.close()

    def get_all_vacancies(self):
        """
        Получить список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            cursor.execute(
                """ 
                    SELECT name_company, name_vacancy, salary, url 
                    FROM vacancy
                """
            )

            self.__output_request(cursor.fetchall())

        connector.commit()
        connector.close()

    def get_avg_salary(self):
        """Получить среднюю зарплату по вакансиям."""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            cursor.execute(
                """ 
                    SELECT AVG (salary) AS avg_salary
                    FROM vacancy
                """
            )

            self.avg_salary = cursor.fetchall()
            self.__output_request(self.avg_salary)

        connector.commit()
        connector.close()

    def get_vacancies_with_higher_salary(self):
        """Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            cursor.execute(
                """ 
                    SELECT name_vacancy, salary
                    FROM vacancy
                    WHERE salary > (SELECT AVG(salary) FROM vacancy)
                """
            )

            self.__output_request(cursor.fetchall())

        connector.commit()
        connector.close()

    def get_vacancies_with_keyword(self, word):
        """Получить список всех вакансий, в названии которых
        содержатся переданные в метод слова, например 'python'."""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            cursor.execute(
                f""" 
                    select name_vacancy
                    from vacancy
                    where LOWER (name_vacancy) LIKE ('%{word}%')
                """
            )

            self.__output_request(cursor.fetchall())

        connector.commit()
        connector.close()

    @staticmethod
    def __output_request(data):
        """Вывод результатов запроса"""
        for line in data:
            print('=' * 100)
            print(*line, sep=' |*| ')

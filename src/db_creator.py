import psycopg2


class DBCreator:
    """Класс для создания БД и таблиц в PostgreSQL."""

    def __init__(self, db_name: str, params: dict):
        self.db_name = db_name
        self.params = params

    def create_database(self) -> None:
        """
        Создает базу данных для сохранения информации
        о вакансиях и работодателях.
        """
        connection = psycopg2.connect(dbname='postgres', **self.params)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f'DROP DATABASE IF EXISTS {self.db_name}')
        cursor.execute(f'CREATE DATABASE {self.db_name}')
        connection.close()

    def create_tables(self) -> None:
        """
        Создает таблицы "hh_companies" и "hh_vacancies" в БД vacancies.
        """
        connection = psycopg2.connect(dbname=self.db_name, **self.params)
        with connection.cursor() as cursor:
            cursor.execute('CREATE TABLE hh_companies('
                           'company_id int PRIMARY KEY,'
                           'company_name varchar(150),'
                           'company_url varchar(100));'
                           ''
                           'CREATE TABLE hh_vacancies('
                           'vacancy_id int PRIMARY KEY,'
                           'company_id int REFERENCES hh_companies(company_id),'
                           'vacancy_name varchar(100),'
                           'salary real,'
                           'currency varchar(4),'
                           'city varchar(50),'
                           'vacancy_url varchar(100));')
        connection.commit()
        connection.close()

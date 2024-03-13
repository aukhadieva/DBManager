import psycopg2
from config import PASSWORD


class DBCreator:
    """Класс для заполнения базы таблиц в БД PostgreSQL."""

    connection = psycopg2.connect(database='vacancies', user='postgres', password=PASSWORD)
    connection.commit()

    def create_database(self) -> None:
        """
        Подключается к базе данных PostgreSQL.
        Создает курсор для переменной connection
        и создает таблицу в БД PostgreSQL.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute('CREATE TABLE hh_vacancies'
                               '(vacancy serial PRIMARY KEY,'
                               'company_name varchar(200),'
                               'vacancy_name varchar(200),'
                               'salary int,'
                               'currency varchar(10),'
                               'url varchar(200),'
                               'city varchar(100))')

    def fills_database(self, data: dict) -> None:
        """
        Подключается к базе данных PostgreSQL.
        Создает курсор для переменной connection
        и заполняет созданную в БД PostgreSQL
        таблицу данными о работодателях и их вакансиях.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                for item in data['items']:
                    salary = str(item['salary']['from'])
                    if salary == 'None':
                        salary = 0
                    cursor.execute('INSERT INTO hh_vacancies (company_name, vacancy_name, salary, currency, url, '
                                   'city) VALUES (%s, %s, %s, %s, %s, %s)', (str(item["employer"]["name"]),
                                                                             str(item['name']),
                                                                             salary,
                                                                             str(item['salary']['currency']),
                                                                             str(item['apply_alternate_url']),
                                                                             str(item['area']['name'])))
        self.connection.close()

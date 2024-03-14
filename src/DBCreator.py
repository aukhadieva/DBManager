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
        и создает таблицы "hh_companies" и "hh_vacancies" в БД PostgreSQL.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
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
                               'city varchar(20),'
                               'vacancy_url varchar(100));')

    def fills_database(self, data: dict) -> None:
        """
        Подключается к базе данных PostgreSQL.
        Создает курсор для переменной connection
        и заполняет созданные в БД PostgreSQL
        таблицы данными о работодателях и их вакансиях.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                for item in data['items']:
                    cursor.execute(
                        'INSERT INTO hh_companies (company_id, company_name, company_url) '
                        'VALUES (%s, %s, %s) ON CONFLICT(company_id) DO NOTHING',
                        (str(item['employer']['id']), str(item['employer']['name']),
                         str(item['employer']['alternate_url'])))

                    salary = str(item['salary']['from'])
                    if salary == 'None':
                        salary = 0
                    cursor.execute(
                        'INSERT INTO hh_vacancies (vacancy_id, company_id, vacancy_name, salary, currency, city, '
                        'vacancy_url) VALUES (%s, %s, %s, %s, %s, %s, %s)', (str(item['id']),
                                                                             str(item['employer']['id']),
                                                                             str(item['name']),
                                                                             salary,
                                                                             str(item['salary']['currency']),
                                                                             str(item['area']['name']),
                                                                             str(item['apply_alternate_url'])))

        self.connection.close()

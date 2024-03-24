import psycopg2


class DBFiller:
    """Класс для заполнения базы данных в БД PostgreSQL."""

    def __init__(self, db_name: str, params: dict):
        self.db_name = db_name
        self.params = params
        self.connection = psycopg2.connect(dbname=self.db_name, **self.params)

    def fills_hh_companies(self, data: list[dict]) -> None:
        """
        Заполняет созданную в БД PostgreSQL
        таблицу данными о работодателях.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                for item in data:
                    cursor.execute(
                        'INSERT INTO hh_companies (company_id, company_name, company_url) '
                        'VALUES (%s, %s, %s)',
                        (item['id'], item['name'], item['alternate_url']))

        self.connection.commit()

    def fills_hh_vacancies(self, data: list[dict]) -> None:
        """
        Заполняет созданную в БД PostgreSQL
        таблицу данными о вакансиях.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                for item in data:
                    cursor.execute(
                        'INSERT INTO hh_vacancies (vacancy_id, company_id, vacancy_name, salary, currency, city, '
                        'vacancy_url) VALUES (%s, %s, %s, %s, %s, %s, %s)', (item['id'],
                                                                             item['employer']['id'],
                                                                             item['name'],
                                                                             item['salary']['from'],
                                                                             item['salary']['currency'],
                                                                             item['area']['name'],
                                                                             item['apply_alternate_url']))

        self.connection.commit()
        self.connection.close()
import psycopg2
from config import PASSWORD


class DBManager:
    """Класс для работы с данными в БД."""

    connection = psycopg2.connect(database='vacancies', user='postgres', password=PASSWORD)

    def get_companies_and_vacancies_count(self) -> None:
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT company_name, COUNT(vacancy_name) FROM hh_vacancies JOIN hh_companies '
                               'USING(company_id) GROUP BY company_name ORDER BY COUNT(vacancy_name) DESC')
                data = cursor.fetchall()
                print(data)

    def get_all_vacancies(self) -> None:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT company_name, vacancy_name, salary, vacancy_url FROM hh_vacancies '
                               'JOIN hh_companies USING(company_id) ORDER BY company_name')
                data = cursor.fetchall()
                print(data)

    def get_avg_salary(self) -> None:
        """
        Получает среднюю зарплату по вакансиям.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT AVG(salary) FROM hh_vacancies')
                data = cursor.fetchall()
                print(data)

    def get_vacancies_with_higher_salary(self) -> None:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT * FROM hh_vacancies WHERE salary > (SELECT AVG(salary) FROM hh_vacancies)')
                data = cursor.fetchall()
                print(data)

    def get_vacancies_with_keyword(self, keyword: str) -> None:
        """Получает список всех вакансий, в названии которых
        содержатся переданные в метод слова, например Python.
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM hh_vacancies WHERE vacancy_name LIKE '%{keyword}%'")
                data = cursor.fetchall()
                print(data)

        self.connection.close()

from src.db_config import config
from src.db_creator import DBCreator
from src.db_filler import DBFiller
from src.db_manager import DBManager
from src.job_portal_api import HeadHunterAPI


OPTIONS = ({1: ' - Получить список всех компаний и количество вакансий у каждой компании',
            2: ' - Получить список всех вакансий с указанием названия компании'
            'названия вакансии и зарплаты и ссылки на вакансию',
            3: ' - Получить среднюю зарплату по вакансиям',
            4: ' - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям',
            5: ' - Получить список всех вакансий, в названии которых содержатся переданные в метод слова',
            0: ' - Выйти из программы'})


def print_options() -> None:
    """Печатает доступные опции выбора в консоль."""
    print("Выбери одну из доступных опций:")
    for key, value in OPTIONS.items():
        print(key, value)


def main() -> None:
    """Реализует взаимодействие с пользователем."""
    hh_api = HeadHunterAPI()

    company_query = input('Введи названия компаний через запятую:\n').split(',')
    db_name = input('Введи название для базы данных (например, vacancies):\n')
    params = config()

    db = DBCreator(db_name, params)
    db.create_database()
    print(f"БД {db_name} успешно создана")
    db.create_tables()
    print("Таблицы hh_companies и hh_vacancies успешно созданы")

    emp_data = []
    try:
        for company in company_query:
            hh_employers = hh_api.get_employers(company)
            emp_data.extend(hh_employers['items'])

        db_filled = DBFiller(db_name, params)
        db_filled.fills_hh_companies(emp_data)
        print("Данные в hh_companies успешно добавлены")

        vac_data = []
        for emp_id in emp_data:
            hh_vacancies = hh_api.get_vacancies(emp_id["id"])
            vac_data.extend(hh_vacancies['items'])
        db_filled.fills_hh_vacancies(vac_data)
        print("Данные в hh_vacancies успешно добавлены\n")

        while True:
            try:
                print_options()
                choice = int(input())
                query = DBManager(db_name, params)
                if choice == 1:
                    query.get_companies_and_vacancies_count()
                    continue
                if choice == 2:
                    query.get_all_vacancies()
                    continue
                if choice == 3:
                    query.get_avg_salary()
                    continue
                if choice == 4:
                    query.get_vacancies_with_higher_salary()
                    continue
                if choice == 5:
                    keyword = input('Напиши слово для фильтра вакансий (например, Python):\n')
                    query.get_vacancies_with_keyword(keyword)
                if choice == 0:
                    print('До встречи!')
                    break
                if choice not in OPTIONS:
                    print('Такой команды нет, попробуй еще раз!\n')
                    continue
            except ValueError:
                print('Такой команды нет, попробуй еще раз!\n')
                continue

    except Exception:
        print('Попробуй позже!')

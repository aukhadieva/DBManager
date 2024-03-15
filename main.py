from src.DBCreator import DBCreator
from src.DBManager import DBManager
from src.Job_Portal_API import HeadHunterAPI


hh_api = HeadHunterAPI()
hh_employers = hh_api.get_employers('разработчик')

db = DBCreator()
db.create_database()

db.fills_hh_companies(hh_employers)
for emp_id in hh_employers['items']:
    hh_vacancies = hh_api.get_vacancies(emp_id["id"])
    db.fills_hh_vacancies(hh_vacancies)

query = DBManager()
query.get_companies_and_vacancies_count()
query.get_all_vacancies()
query.get_avg_salary()
query.get_vacancies_with_higher_salary()
query.get_vacancies_with_keyword('Python')

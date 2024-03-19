from abc import ABC, abstractmethod
import requests


class Job_Portal_API(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями.
    """

    @abstractmethod
    def get_employers(self, key_word):
        pass

    @abstractmethod
    def get_vacancies(self, emp_id):
        pass


class HeadHunterAPI(Job_Portal_API):
    """
    Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
    """

    def get_employers(self, key_word: str) -> dict:
        """
        Метод для подключения к API и получения информации о работодателях.
        Получает информацию с hh.ru в формате JSON.
        """
        params = {
            'text': f'{key_word}',
            'area': 113,
            'per_page': 10,
            'only_with_vacancies': "true",
        }

        try:
            request = requests.get('https://api.hh.ru/employers', params)
            employers = request.json()
            return employers
        except requests.exceptions.HTTPError as errh:
            print('Ошибка HTTP:')
            print(errh.args[0])
        except requests.exceptions.ReadTimeout as errrt:
            print("Ошибка таймаута:", errrt)
        except requests.exceptions.ConnectionError as conerr:
            print('Ошибка подключения:', conerr)
        except requests.exceptions.RequestException as errex:
            print('Ошибка запроса:', errex)

    def get_vacancies(self, emp_id: str) -> dict:
        """
        Метод для подключения к API и получения информации о вакансиях.
        Получает информацию с hh.ru в формате JSON.
        """
        params = {
            'area': 113,
            'per_page': 100,
            'employer_id': f'{emp_id}',
            'enable_snippets': "true",
            'only_with_salary': "true"
        }

        try:
            request = requests.get('https://api.hh.ru/vacancies', params)
            vacancies = request.json()
            return vacancies
        except requests.exceptions.HTTPError as errh:
            print('Ошибка HTTP:')
            print(errh.args[0])
        except requests.exceptions.ReadTimeout as errrt:
            print("Ошибка таймаута:", errrt)
        except requests.exceptions.ConnectionError as conerr:
            print('Ошибка подключения:', conerr)
        except requests.exceptions.RequestException as errex:
            print('Ошибка запроса:', errex)

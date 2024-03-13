from abc import ABC, abstractmethod
import requests


class Job_Portal_API(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, key_word):
        pass


class HeadHunterAPI(Job_Portal_API):
    """
    Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
    """

    def get_vacancies(self, key_word: str) -> dict:
        """
        Метод для подключения к API и получения вакансий.
        Получает вакансии с hh.ru в формате JSON.
        """
        params = {
            'text': f'{key_word}',
            'area': 113,
            'page': 0,
            'per_page': 100,
            'enable_snippets': "true",
            'only_with_salary': "true"
        }

        request = requests.get('https://api.hh.ru/vacancies', params)
        data = request.json()
        return data

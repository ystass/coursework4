from abc import ABC, abstractmethod
import requests
import json


class FromAPI(ABC):
    """Абстрактный класс"""
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass

class FromHHru(FromAPI):
    """Класс для подключения к API и получения вакансий"""
    def __init__(self, url_get='https://api.hh.ru/vacancies'):
        self.url_get = url_get

    def get_vacancies(self, keyword):
        """Получение списка вакансий в формате json"""
        response = requests.get(self.url_get, params={'text': keyword, 'area': '113', 'per_page': 100})
        vacancies = response.json()
        vacancies_json = json.dumps(vacancies['items'], ensure_ascii=False)
        print(vacancies.keys())
        print(vacancies)
        # print(response.text)
        #print(vacancies['items'])
        print(vacancies_json)
        print(vacancies['found'])
        print(vacancies['pages'])
        print(vacancies['page'])
        print(vacancies['per_page'])
        return vacancies_json

    # @staticmethod
    # def save_vacancies(vacancies_json):
    #     """Запись списка вакансий в файл"""
    #     with open("../data/vacancies.json", "w", encoding="utf8") as f:
    #         f.write(vacancies_json)


# h = FromHHru()
# h1 = h.get_vacancies()
# vacancies_json = h.get_vacancies()
# h2 = h.save_vacancies(vacancies_json)


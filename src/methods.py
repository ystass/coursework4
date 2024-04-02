from abc import ABC, abstractmethod
import json
from src.class_api import FromHHru


class Methods(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def add_vacancy(self, *args):
        pass

    @abstractmethod
    def get_data(self, *args):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class ListVacancies(Methods):
    # def __init__(self, vacancies_json="vacancies.json"):
    #     self.vacancies_json = vacancies_json

    @staticmethod
    def save_vacancies(vacancies_json):
        """Запись списка вакансий в файл"""
        with open("../data/vacancies.json", "w", encoding="utf8") as f:
            f.write(vacancies_json)

    def add_vacancy(self, user_vac):
        """Метод для добавления вакансий в файл"""
        list = []
        list_vacancies = json.dumps(list, ensure_ascii=False)
        # print(list_vacancies)
        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list_vacancies)
        with open("../data/my_vacancies.json", "r", encoding="utf8") as f:
            list_vacancies = json.load(f)

        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            for vac in vacancies:
                if vac["name"] == user_vac:
                    list_vacancies.append(vac)
        list_vacancies_json = json.dumps(list_vacancies, ensure_ascii=False)
        print(list_vacancies_json)
        with open("../data/my_vacancies.json", "w+", encoding="utf8") as f:
            f.write(list_vacancies_json)
        print(list_vacancies)
        return list_vacancies

    def get_data(self, criterion):
        """Метод получения данных из файла по указанным критериям"""
        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            #print(vacancies)
            criterion_vac = []
            for vac in vacancies:
                if criterion in vac["snippet"]["responsibility"]:
                    criterion_vac.append(vac)
        print(criterion_vac)
        return criterion_vac

    def delete_vacancy(self):
        """Метод удаления данных из файла по указанным критериям"""
        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            list_vacancies = json.load(f)
            for vac in list_vacancies:
                if vac["area"]["name"] != "Россия":
                    list_vacancies.remove(vac)
        return list_vacancies



# v = lv.delete_vacancy()
# v1 = lv.get_data("принимать")
#v2 = lv.add_vacancy("Диспетчер чатов (в Яндекс)")
# print(h)
# print(h1)
# lv = ListVacancies()
# v3 = lv.save_vacancies(vacancies_json)

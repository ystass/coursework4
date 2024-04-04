from src.class_vacancy import FromVacancy
import json

def vac_user():
    """Приводим полученные данные к данным для вывода"""
    with open("../data/vacancies.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)
    global salary, currency, url, requirement
    user_vac = []
    for vac in vacancies:
        name = vac["name"]
        if not vac["salary"]:
            salary = 0
            currency = " "
        elif vac["salary"]["from"] is None and vac["salary"]["to"] is None:
            salary = 0
        elif vac["salary"]["from"] is None and vac["salary"]["to"] is not None:
                salary = vac["salary"]["to"]
        elif vac["salary"]["from"] is not None and vac["salary"]["to"] is None:
                salary = vac["salary"]["from"]
        if vac["salary"]["currency"]:
            currency = vac["salary"]["currency"]
        else:
            currency = "Валюта не определена"
        url = vac["alternate_url"]
        if vac["snippet"]["requirement"]:
            requirement = vac["snippet"]["requirement"]
        else:
            requirement = "Информация отсутствует"
        #lv = FromVacancy
        user_vac.append(FromVacancy(name, salary, currency, url, requirement))
    print(user_vac)

    return user_vac

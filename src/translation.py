from src.class_vacancy import FromVacancy
from src.main import vacancies
import json

def vac_user():
    with open("../data/my_vacancies.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)
    global salary
    user_vac = []
    for vac in vacancies:
        name = vacancies["name"]
        if vac["salary"]["from"] is None and vac["salary"]["to"] is None:
            salary = 0
        elif vac["salary"]["from"] is None and vac["salary"]["to"] is not None:
            salary = vacancies["salary"]["to"]
        elif vac["salary"]["from"] is not None and vac["salary"]["to"] is None:
            salary = vacancies["salary"]["from"]
        currency = vacancies["currency"]
        url = vacancies["alternate_url"]
        requirement = vacancies["snippet"]["requirement"]
        lv = FromVacancy
        user_vac.append(lv(name, salary, currency, url, requirement))
    print(user_vac)
    return user_vac


vac_user()

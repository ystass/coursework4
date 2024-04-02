from src.class_api import FromHHru
from src.methods import ListVacancies

user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
hh = FromHHru()
vacancies = hh.get_vacancies(user_vacancy)
fv = ListVacancies()
fv1 = fv.save_vacancies(vacancies)

fv2 = fv.delete_vacancy()
print(fv2)

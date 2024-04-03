from src.class_api import FromHHru
from src.class_vacancy import FromVacancy
from src.methods import ListVacancies
import json

user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
hh = FromHHru()
vacancies = hh.get_vacancies(user_vacancy)


fv = ListVacancies()
fv1 = fv.save_vacancies(vacancies)
#
# name_vac = input('Введите название вакансии: \n')
# fv3 = fv.add_vacancy(name_vac)
# #
# name_exit = input('Завершим и очистим файл вакансий да/нет : \n')
# if name_exit == 'да':
#     fv4 = fv.delete_vacancy()
# print('Выбранные вакансии в my_vacancies.json')
name_criterion = input('Введите критерий для отбора вакансий: \n')
fv4 = fv.get_data(name_criterion)

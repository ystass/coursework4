from src.translation import vacancies


def sorting(n):
    sorted_list = sorted(vacancies, key=lambda x: x['Зарплата'], reverse=True)
    sorted_vac = sorted_list[:n]
    return sorted_vac


s_v = sorting(5)

print(s_v)
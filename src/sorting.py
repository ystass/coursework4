from src.translation import vac_user

user_vac = vac_user()

def sorting(n):
    sorted_list = sorted(user_vac, key=lambda x: x['Зарплата'], reverse=True)
    sorted_vac = sorted_list[:n]
    print(sorted_vac)
    return sorted_vac


# s_v = sorting(5)
#
# print(s_v)
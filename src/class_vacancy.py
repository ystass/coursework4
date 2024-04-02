class FromVacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, name, salary, currency, url, type_work='Нет данных', requirement='Нет данных'):
        self.name = name
        self.salary = salary
        # self.from_ = from_
        # self.to = to
        self.currency = currency
        self.url = url
        self.type_work = type_work
        self.requirement = requirement

    def __repr__(self):
        return f'{self.name}, {self.salary} {self.currency}, {self.type_work}, {self.requirement}, <{self.url}>'

    def __gt__(self, other):
        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""
        if self.salary is not None and other.salary is not None:
            if self.salary['to'] > other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __lt__(self, other):
        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""
        if self.salary is not None and other.salary is not None:
            if self.salary['to'] < other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'


v = FromVacancy

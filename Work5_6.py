# вызов родительских аргументов без повтора

from Work5_5 import Employee

class TEmployee(Employee):
    ''' '''
    def __init__(self, *args, **kwargs):                    # можно вводить произвольное количество любых аргументов
        super().__init__(*args, **kwargs)                   # забираем у родителя все доступные аргументы
        self.skills = []

    def dd_skills(self, skills):
        self.skills.extend(skills)

    def __add__(self, other):                               # учим класс работать со встроенными функциями
        return self.skills + other.skills

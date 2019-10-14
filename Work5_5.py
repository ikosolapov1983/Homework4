# вызов родительского конструктора

from Work5_3 import Person

class Employee(Person):
    ''' '''
    def __init__(self, name="", surname="", age=0, position="", salary="",skills=None):     # добавили свои свойства объекта
#        Person.__init__(self, name, surname, age)                                          # вызов конструктора из родительского класса
        super().__init__(name, surname, age)                                                # добавляет через фукцию super от родителя
        self.skills.extend(skills)                                                          # значение в виде списка
        self.position = position
        self.salary = salary

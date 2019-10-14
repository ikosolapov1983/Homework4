# Наследование класса от родительского класса

class Person:
    common_properties = {"species": "human"}

    def __init__(self, name="", surname="", age=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = []                    # создается пустой объект по умолчанию

    def full_n(self):
#        return self.name + ' ' + self.surname              # по старинке
#        return "{} {}".format(self.name, self.surname)     # метод формат
        return f"{self.name} {self.surname}"                # через f-строку

    def __str__(self):
#        return self.name + ' ' + self.surname              # по старинке
#        return "{} {}".format(self.name, self.surname)     # метод формат
        return f"Object{self.__class__} object: {self.name} {self.surname}"

    def get_older(self, years=0):
        self.age = self.age + years
        return self.age

class Employee(Person):                     # в скобках родительский класс
    ''' '''
    def __init__(self, name="", surname="", age=0, position="", salary=""):     # добавили свои свойства объекта
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = []
        self.position = position
        self.salary = salary

    def get_older(self, years=0):
        self.age = self.age - years
        return self.age                                                             # перепределили метод

# класс с вызовом __init__ - конструктора свойств объекта, примеры функций внутри класса

class Person:
    common_properties = {"species": "human"}

    def __init__(self, name="", surname="", age=0):     # создаем список параметров
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = []                    # создается пустой объект по умолчанию

    def full_n(self):
#        return self.name + ' ' + self.surname              # вывод по старинке
#        return "{} {}".format(self.name, self.surname)     # вывод метод формат
        return f"{self.name} {self.surname}"                # вывод через f-строку

    def __str__(self):
#        return self.name + ' ' + self.surname              # по старинке
#        return "{} {}".format(self.name, self.surname)     # метод формат
        return f"Object{self.__class__} object: {self.name} {self.surname}"

    def get_older(self, years=0):           # функция делает человека старше на years лет.
                                            # чтобы функция видела переменные из конструктора,
                                            # используй их через вызов self!!, в ином случае она не
                                            # будет о них знать, или ты будешь задавать их отдельно
        self.age = self.age + years
        return self.age

if __name__ == "__main__":
    p1 = Person("Vasya", "Petrov")
    print(p1.name)
    print(p1.age)
    print(p1.get_older(60))
    print(p1.age)
    print(p1.full_n())
    print(p1.get_older(5))

    p2 = Person()
    print(p2)

# простой класс с вызовом self


class Person:
    def printer_self(self):         # self - это первый аргумент функции в списке параметров
        print(self)

p1 = Person()
print(p1)
p1.printer_self()

p2 = Person()
print(p2)
p2.printer_self()

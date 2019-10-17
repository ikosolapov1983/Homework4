# класс с вызовом self


class Person:
    common_properties = {"species": "human"}
    def set_name(self, value):
        self.name = value

if __name__ == "__main__":
    p1 = Person()
    print(p1)
    p1.set_name("Vasya")

    p2 = Person()
    print(p2)
    p2.set_name("Kolya")

    print(p1.name, p2.name)
    print(p1.common_properties)
    print(p2.common_properties)
    print(p1.common_properties is p2.common_properties)


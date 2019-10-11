import task3

d = {"name": "Vasya", "surname": "Pet324234rov", "age": 35, "position": "Mana234234ger", "address": "Berd234234ichev", "skills": "Crooked Hands"}
d2 = {v: type(k) for v, k in d.items()}                             # формируем словарь с типами значений
print(d2)
d3 = {k: task3.let(d[k]).lower() for k in d if type(d[k]) is str}   # формируем словарь только со строковыми параметрами,
print(d3)                                                           # убираем цифры, если есть

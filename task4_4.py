import task3

l = [45, 67, 888, input('Введите значение: '), [5, 7]]
l_new = [task3.let(i) for i in l if type(i) is str]
print('Список со строками: ', l_new)

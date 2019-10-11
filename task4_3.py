l = [45, 67, 888, 'Пётр', -10, ',',  7.9, [5, 7]]
l_new = [i for i in l if type(i) is int]
print(l_new)

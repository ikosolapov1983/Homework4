def fu(*data):
    """
    :param data: произвольное количество элементов
    :return: возвращает второй элемент в списке
    """
    s = []
    for i in data:         # убираем повторяющиеся элементы
        if i not in s:
            s.append(i)
    s = sorted(s)       # сортируем то, что получилось
    return s[1]

print(fu(4, 6, 8, 1, 1, 1, 5, 9, 5, 6, 6))

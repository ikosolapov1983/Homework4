import string

def let(s):
    """
    :param s: параметр принимает значение в формате str
    :return: возвращает строку без цифр
    """
    res = ''
    assert type(s) is str       #проверка на тип вводимых данных
    for i in s:
        if i in string.ascii_letters:
            res =res + i
    return res

#assert let('asdfgh456kl;') == 'asdfghkl', "Function is bad"     # проверка на вывод функции



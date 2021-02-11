# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def fn_division(arg_1, arg_2):
    res = None
    if arg_2 == 0:
        print('Ошибка! Деление на ноль!')
    else:
        res = arg_1 / arg_2
    return res

v_arg = list(map(float, input('Введите два числа: ').split()))
if len(v_arg) < 2:
    print('Ошибка! Не задан аргумент!')
else:
    print(f'{v_arg[0]} / {v_arg[1]} = {fn_division(v_arg[0], v_arg[1])}')


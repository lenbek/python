# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    try:
        v_list = [float(arg_1), float(arg_2), float(arg_3)]
        v_list.sort(reverse=True)
        v_res = v_list[0] + v_list[1]
    except ValueError:
        return 'Ошибка! Некорректное число!'
    return v_res

v_arg = list(input('Введите три числа: ').split())
print(my_func(v_arg[0], v_arg[1], v_arg[2]))

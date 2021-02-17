# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('tsk5.txt', 'w+') as f_obj:
    while True:
        v_str = input()
        try:
            float(v_str)
            f_obj.write(v_str + ' ')
        except ValueError:
            break
    f_obj.seek(0)
    v_data = list(map(float, f_obj.readline().split()))
    print(sum(v_data))

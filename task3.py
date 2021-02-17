# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

tdata = []
v_min = 20000
with open('tsk3.txt', encoding='utf-8') as f_obj:
    data = [line.split() for line in f_obj]
    tdata = list(zip(*data))
    print('Средней доход = ', round(sum(map(float, tdata[1]))/len(tdata[1]), 2))
    print(*[i[0] for i in data if float(i[1]) < v_min], sep='\n')

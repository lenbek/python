# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

v_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('tsk4.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    for i, n in enumerate(lines):
        for key in v_dict.keys():
            lines[i] = lines[i].replace(key, str(v_dict[key]))
    with open('tsk4_rur.txt', 'w', encoding='utf-8') as fr_obj:
        fr_obj.writelines(lines)

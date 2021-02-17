# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('tsk2.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    print(f'Количество строк: {len(lines)}')
    for ind, line in enumerate(lines):
        print(f'Строка {ind+1}: {len(line.strip().split())} слов')

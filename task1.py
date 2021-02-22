# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, lsts_mtrx_data):
        self.mtrx_data = list(list(lsts_mtrx_data))

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.mtrx_data])

    def __add__(self, other):
        if len(self.mtrx_data) != len(other.mtrx_data) or any(len(self.mtrx_data[i]) != len(other.mtrx_data[i]) for i, el in enumerate(self.mtrx_data)):
            print('Ошибка! Несовпадение размерностей!')
        else:
            for i, row in enumerate(self.mtrx_data):
                self.mtrx_data[i] = list(map(sum, list(zip(self.mtrx_data[i], other.mtrx_data[i]))))
        return self


matrix_1 = Matrix([[1, 2, 3], [1, 2, 2], [1, 2, 2]])
matrix_2 = Matrix([[9, 7, 6], [1, 5, 6], [4, 3, 4]])

print('matrix_1', matrix_1, sep='\n')
print('matrix_2', matrix_2, sep='\n')
print('add:', matrix_1 + matrix_2, sep='\n')

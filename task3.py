# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#    name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
#    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(income)


class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        print(sum(self._income.values()))


pIvanov = Position('Иван', 'Иванов', 'специалист', {'wage': 100, 'bonus': 10})
print(pIvanov.name)
print(pIvanov.surname)
print(pIvanov.position)
print(pIvanov._income)
pIvanov.get_full_name()
pIvanov.get_total_income()

pPetrov = Position('Петр', 'Петров', 'специалист', {'wage': 100})
pPetrov.get_full_name()
pPetrov.get_total_income()

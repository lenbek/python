# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала....')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print('машина повернула ', direction)

    def show_speed(self):
        print('скорость: ', self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.__speed_max = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__speed_max:
            print(' === ПРЕВЫШЕНИИ СКОРОСТИ === ')


class SportCar(Car):
    pass


class WorkCar(TownCar, Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.__speed_max = 40


    # def show_speed(self):
    #     super().show_speed()
    #     if self.speed > self.__speed_max:
    #         print(' === ПРЕВЫШЕНИИ СКОРОСТИ === ')

class PoliceCar(Car):
    pass


car = Car(90, 'green', 'XFT', False)
tcar = TownCar(78, 'blue', 'vasja', False)
scar = SportCar(198, 'red', 'red', False)
wcar = WorkCar(50, 'white', 'w67', False)
pcar = PoliceCar(100, 'red', 'PC', True)

print(f'{car.speed = }')
print(f'{car.color = }')
print(f'{car.name = }')
print(f'{car.is_police = }')
car.go()
car.turn('left')
car.go()
car.show_speed()
car.stop()


print(f'{tcar.speed = }')
print(f'{tcar.color = }')
print(f'{tcar.name = }')
print(f'{tcar.is_police = }')
tcar.go()
tcar.turn('left')
tcar.go()
tcar.speed = 100
tcar.show_speed()
tcar.stop()


print(f'{scar.speed = }')
print(f'{scar.color = }')
print(f'{scar.name = }')
print(f'{scar.is_police = }')
scar.go()
scar.show_speed()
scar.stop()


print(f'{wcar.speed = }')
print(f'{wcar.color = }')
print(f'{wcar.name = }')
print(f'{wcar.is_police = }')
wcar.go()
wcar.turn('right')
wcar.go()
wcar.show_speed()
wcar.speed = 80
wcar.show_speed()
wcar.stop()


print(f'{pcar.speed = }')
print(f'{pcar.color = }')
print(f'{pcar.name = }')
print(f'{pcar.is_police = }')
pcar.go()
pcar.show_speed() 
import os
import function as fn

menuitems = [
        ("1.", "Вывод автобусов"),
        ("2.", "Добавление автобуса"),
        ("3.", "Вывод водителей"),
        ("4.", "Добавление водителя"),
        ('5.', "Вывод маршрута"),
        ('6.', "Добавление маршрута"),
        ("7.", "Выход")]

os.system('cls')

print('МЕНЮ: ')
for point in menuitems:
    print(point[0], point[1])

number = input('Введите номер команды: ')
if number == '1':
    print(fn.PrintBus())
elif number == '2':
    fn.AddBus()
elif number == '3':
    print(fn.PrintDriver())
elif number == '4':
    fn.AddDriver()
elif number == '5':
    print(fn.PrintRoute())
elif number == '6':
    fn.AddRoute()

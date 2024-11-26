while True:
    try:
        x = int(input('Введите x: '))
        break
    except Exception:
        print('Ошибка!')

while True:
    try:
        y = int(input('Введите y: '))
        break
    except Exception:
        print('Ошибка!')

z = (-y)^2+2*x-71*x*y
print('Значение выражения:', z)
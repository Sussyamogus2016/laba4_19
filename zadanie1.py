while True:
    try:
        x = float(input('Введите x: '))
        break
    except Exception:
        print('Ошибка!')

while True:
    try:
        y = float(input('Введите y: '))
        break
    except Exception:
        print('Ошибка!')

z = (-y)^2+2*x-71*x*y
print('Значение выражения:', z)
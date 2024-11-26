import math
a = 2.8
b = -0.3
c = 4
while True:
    try:
        x = float(input('Введите x: '))
        break
    except Exception:
        print('Ошибка!')

if x < 1.2:
    print('Ответ:', a*x**2+b*x+c)
elif x == 1.2:
    print('Ответ:', a/x+math.sqrt(x**2+1))
else:
    print('Ответ:', (a+b*x)/(math.sqrt(x**2)+1))

import math


a = float(input('podaj a'))
b = float(input('podaj b'))
c = float(input('podaj c'))

if b == 0 and c == 0:
    print('x = ' + '0')
elif b == 0 and c != 0:
    if -c / a > 0:
        print('x1 = ' + str(math.sqrt(-c/a)))
        print('x2 = ' + str(-math.sqrt(-c / a)))
    elif -c / a < 0:
        print('sprzecznw')
elif c == 0 and b != 0:
    print('1x = ' + '0')
    print('2x = ' + str(-b/a))
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        print('x1 = ' + str((-b + math.sqrt(delta)) / (2 * a)))
        print('x2 = ' + str((-b - math.sqrt(delta)) / (2 * a)))
    elif delta == 0:
        print('x ='+ str(-b / (2 * a)))
    else:
        print('sprzecze')

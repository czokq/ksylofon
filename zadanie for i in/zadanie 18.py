import random
lista = [1]
d1 = 1
d2 = 2
a = 1
k = 0
u = 0
b = int(input("jaka druzyna wygra? (wiebrz pomiedzy 1, 2): "))
for i in lista:
    lista.append(1)
    x = random.randint(1,2)
    print('akcja nr {}'.format(a))

    a += 1
    if x == 1:
        print("akcje wygrała durzyna 1")
        k += 1

    elif x == 2:
        print("akcje wygrała durzyna 2")
        u += 1
    print('{} : {}'.format(k, u))

    if k >= 25 and k > u + 1:
        if b == 1:
            print("wyrałęs zaklad")
        else:
            print("przegrales zkład")
        print("wygrałą druzna 1")
        break

    elif u >= 25 and u > k + 1:
        if b == 2:
            print("wyrałęs zaklad")
        else:
            print("przegrales zkład")
        print("wygrała druzna 2")
        break



#a
'''for x in range(3, 103, 3):
    y = 1/2*x+3
    print("{}\t{}".format(x, y))'''

#b)
#I)
'''
for i in range(-30, 61, 1):
    x= i / 10
    y = 1/2*x+3
    print("{}\t{}".format(x, y))'''
#II)
x = -3
lista = [1]
for i in lista:
    y = 1/2 * x + 3
    print("{}\t{}".format(x, y))
    x = x + 0.1
    if x > 6:
        break
    lista.append(1)
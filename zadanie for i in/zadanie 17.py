n = int(input("podaj ile ma byc liczb: "))
suma = 0

for i in range(n):
    liczba = float(input("podaj liczbe nr {} ".format(i + 1)))
    suma = suma + liczba
print("suma = {}".format(suma))

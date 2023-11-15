n = int(input("podaj ile ma byc liczb: "))
suma = 0
iloczyn = 1
licznik = 0#
licznik2 = 0
max_liczba = float(input("podaj liczbe nr 1: "))
min_liczba = max_liczba
suma = suma + max_liczba
iloczyn = iloczyn * max_liczba
if max_liczba < 3:
    licznik = licznik + 1

if max_liczba > -2 and max_liczba <= 11:
    licznik = licznik + 1

for i in range(1, n):
    liczba = float(input("podaj liczbe nr {} ".format(i + 1)))
    suma = suma + liczba
    iloczyn = iloczyn * liczba
    if liczba > max_liczba:
        max_liczba = liczba
    if liczba < min_liczba:
        min_liczba = liczba
    if liczba < 3:
        licznik = licznik + 1
print("suma = {}".format(suma))
print("srednia = {}".format(suma / n))
print("iloczyn = {}".format(iloczyn))
print("max liczba = {}".format(max_liczba))
print("min liczba = {}".format(min_liczba))
print("liczby dzielace sie przez 3 = {}".format(licznik))
import random
liczba = random.randint(1, 10)

x = input("podaj liczbę: ")


if liczba == int(x):
    print("wygrałeś")

else :
    print("przegrałes")

print("ukrytą liczbą była:")
print(liczba)
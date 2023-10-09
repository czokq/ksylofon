import sys
import random
i = 3
liczba = random.randint(1, 10)
print("masz 3 szanse :)")
x = int(input("podaj liczbę naturalną: "))

if x == 0 :
    print("bruh")
    sys.exit(0)

if liczba == int(x):
    print("wygrałeś")

else :
    print("przegrałes")

print("ukrytą liczbą była:")
print(liczba)
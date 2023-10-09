import sys
import random

liczba_szans = 3

while (liczba_szans):
    liczba = random.randint(1, 10)
    print(f"Masz {liczba_szans} szanse :)")
    x = int(input("Podaj liczbę naturalną: "))

    if x == 0:
        print("Bruh")
        sys.exit(0)

    if liczba == x:
        print("Wygrałeś")
        break
    else:
        print("Przegrałeś")

    liczba_szans -= 1

print("Ukrytą liczbą była:", liczba)
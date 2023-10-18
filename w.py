import sys
import random
import time

liczba_szans = 3
liczba = random.randint(1, 10)
print("grasz o 20psc i lipton brzoskwinia :)")
time.sleep(2)
while liczba_szans > 0:

    print(f"Masz {liczba_szans} szanse :)")
    x = int(input("Podaj liczbę naturalną (mniejszą niż 10): "))

    if x == 0 or x > 10:
        print("przeczytaj polecenie jeszcze raz :)")


    if liczba == x:
        print("brawo!!!! Wygrałeś")
        break
    else:
        print("Przegrałeś")

    liczba_szans -= 1

print("Ukrytą liczbą była:", liczba)
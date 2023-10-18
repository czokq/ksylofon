import random
import time

liczba_szans = 3        #ilość szans
liczba = random.randint(1, 10)  #losuje liczbe od 1 do 10
print("grasz o 20psc i lipton brzoskwinia :)") # wygrana
time.sleep(2)    #kod idzie spać na dwie sekundy
while liczba_szans > 0:  #sprawdza czy zostały ci sznase

    print(f"Masz {liczba_szans} szanse :)") # podaje ilość szans
    x = int(input("Podaj liczbę naturalną (mniejszą niż 10): ")) #pobiera liczbę o którą sprawdza

    if x == 0 or x > 10: # sprawdza czy użytkownik potrafi czytać
        print("przeczytaj polecenie jeszcze raz :)")


    if liczba == x: #sprawdza czy liczba podana przez uztkownika jest taka sama jak wylosowana
        print("brawo!!!! Wygrałeś 20 psc i pół liptona")
        break
    else: #jeśli nie jest:
        print("Przegrałeś")

    liczba_szans -= 1 #odejmuje jedna szanse

print("Ukrytą liczbą była:", liczba) #podaje ukrytą liczbę
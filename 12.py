import sys

jp = int(input("wypisz wynik język polski: "))
jo = int(input("wypisz wynik język obcy: "))
ujp = int(input("wypsiz wynik ustny język polski: "))
d = int(input("wypisz wynik dodatkowy: "))


if ujp < 0 or jo < 0 or ujp < 0 or d < 0:
    print("liczba nie może być ujemna")
    sys.exit(0)

wynik = (jp + jo + ujp + d) / 4


if jp > 30 and jo > 30 and ujp > 30 and ujo > 30 and d > 30:
    print("zdałeś bez amnesti")
    sys.exit(0)

if wynik > 30:
    print("zdałeś z amnestią")

else:
    print("nie zdałeś")

import sys
ocena = int(input("podaj swoją ocenę z klasy 8: "))#

wynik = int(input("podaj swój wynik z  testu: "))

if ocena > 6 or ocena < 0 :
    print("błendną informacją jest ocena", ocena)
    sys.exit(0)

elif wynik < 0 or wynik > 100:
    print("błendną informacją jest wynik", wynik)
    sys.exit(0)

if ocena >= 5 or wynik > 90 :
        print("dostałeś się do grupy zawansowanej")
        sys.exit(0)
else:
        print("dostałeś się do grupy niezawannsowanej")
        sys.exit(0)


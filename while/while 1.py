import time
uzytkownicy = {
        "admin": "admin",
        "user": "1234",
        "user1": "1234"
    }
x = 3
d = 1
w = 5
username = input("Podaj nazwę użytkownika: ")
while x > 0:
    password = input("Podaj hasło: ")
    if username in uzytkownicy and password == uzytkownicy[username]:
        print("Zalogowano pomyślnie!")
        break
    else:
        print("Błędna nazwa użytkownika lub hasło.")
        print("zostało ci {} próby".format(x - 1))
        x = x - 1
        if x == 0:
            print("podałeś 3 razy błednie hasło masz blokade na {}sekund".format(w))
            time.sleep(w)
            x = x + 1
            w = w * 2
            if username in uzytkownicy and password == uzytkownicy[username]:
                print("Zalogowano pomyślnie!")
                break







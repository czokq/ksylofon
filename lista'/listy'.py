lista = []
print(type(lista))
#wypełnianie listy
#1. wpisujemy elementy na sztywno
lista1 = [1, 2, 3, 4, 5]
#2. powielanie listy
lista2 = [1] * 1000
print(lista2)
lista3 = [1, 2, 3] * 10
print(lista3)
#3. kontatenacja sklejanie list
lista4 = [1, 2, 3] + [4, 5, 6]
print(lista4)
#4 dołącznie pojedynczych elementow na koncu listy
lista5 = []
lista5.append(3)
lista.append(7)
print(lista5)
#5 insertowanie - wstawianie elamentu na okreslonej pozycji
lista6 = [1, 2, 3, 4, 5, 6]
lista6.insert(1, 90)
print(lista6)
#6 rozszerznie listy o elementy innej listy
lista7 = [4, 0, 1, 7, 9]
lista7.extend([7, 1, 5])
print(lista7)
#II rozmiar listy
lista8 = [6, 7, 8]
print(len(lista8))
#III zliczanie ile razy na liście pojawia sie dany element
lista9 = [7, 9, 9, 7, 6, 4, 4, 4, 4, 0]
print(lista9.count(4)) #zliczamy ile bylo czworek na liscie
#IV zamiana napisu na listę
slowo = 'informatyka'
lista10 = list(slowo)
print(lista10)
print(lista10.count('a'))
#zamiana listy na napis
lista11 = [4, 9, 7, 1]
slowo2 = str(lista1)
print(slowo2)
print(len(slowo2))
#V wycinanie fragmentu listy
#1. wyciagenie pojedynczego elementu
lista12 = [6, 1, 3, 5, 2]
print(lista12[3]) #chcemy się dostac do czwartego elementu listy(o indeksie 3)
#wyciąganie fragmentu listy
lista13 = [6, 1, 3, 8, 9, 1, 2, 5]
#wycięci eprzedziału <1, 6)
print(lista13[1:4])#wyciągamy fragment od indeksu 1 do indeksu 3
#wycięci eprzedziału <1, 6) co 2 liczby
print(lista13[1:6:2]) #1 od indeksu 1 do indeksu 5 (bo 6-1) co dwie liczby
lista14 = list(range(0, 1001))
print(lista14[0:1001:3])
print(lista14[::3]) #od poczatku do konca co 3
#indeksy wsteczne
lista15 = [6, 1, 5, 3, 2, 9, 1]
print(lista15[-1])
print(lista15[len(lista15) - 1])

#ciekawy sposob na odwracanie listy
print(lista15[::-1])
#ciekawy sposob na odwracanie listy
print(lista15[-5:-3])
#listy - przydatne funkcje
#1.sortowanie
lista16 = [4, -1, 7, 2, 4, -10, 8]
lista16.sort() #doyslnie rosnaco
print(lista16)
lista16.sort(reverse=True)
print(lista16)
#2. odwracanie
slowo3 = 'kajak'
lista17 = list(slowo3)
lista17.reverse()
print(lista17)
#jak liste polaczyc z powrotem w slowo
slowo3_po_odwr = ''.join(lista17)
print(slowo3_po_odwr)

#VI Usuwanie elementów z listy
lista18 = ['kot', 2, 'pies', 7.4]

#usuwanie na podstawie nr elementu
del lista18[2]
print(lista18)

#usuwanie na bazie wartości elementu
lista18.remove('kot')
print(lista18)

#VII Funkcje

#czyszczenie listy
#czyszczenie łopatologiczne
lista19 = [4, 9, 'kot', 'qwerty', 5, 99, 45]
lista19 = []
print(lista19)

#czyszczenie eleganckie
lista20 = [4, 9, 'kot', 'qwerty', 5, 99, 45]
lista20.clear()
print(lista20)

#Sprawdzanie pod jakim indeksem jest dany element
lista21 = ['matematyka', 'fizyka', 'informatyka', 'język polski', 'fizyka']
print(lista21.index('fizyka'))

#Chodzenie po liście z nadzorowaniem indeksów:
lista22 = ['jabłko', 'gruszka', 'winogrono', 'śliwka']

for nr, o in enumerate(lista22):
    print(nr, o)

#Kopiowanie listy

#Jak nie kopiować listy
lista_oryginalna = [3, 1, 7, 8, 11]
lista_kopia = lista_oryginalna

lista_kopia[2] = 67 #Zmiana wykonana na kopii powoduje zmianę na liście oryginalnej

print(lista_oryginalna)

#Jak można kopiować listy
#Sposób chałupniczy
lista23 = [6, 1, 2, 9, 1, 5]
lista23_kopia = lista23[::] #tzw. płytka kopia
lista23_kopia[2] = 78 #zmiana na kopii NIE POWODUJE zmian na oryginale
print(lista23)
print(lista23_kopia)

#Sposób elegancki
lista24 = [6, 1, 2, 9, 1, 5]
lista24_kopia = lista24.copy() #tzw. płytka kopia
lista24_kopia[2] = 78 #zmiana na kopii NIE POWODUJE zmian na oryginale
print(lista24)
print(lista24_kopia)

#VIII Wyrażenia listowe
lista_zwierzat = ['kapibara', 'kos', 'żyrafa', 'pies', 'orangutan', 'antylopa', 'tygrys', 'małpa']

#Chcemy aby na liście pozostały tylko te nazwy zwierząt, które mają parzystą liczbę liter - bez wyrażeń listowych

#Przypomnienie - reszta z dzielenia
print(13 % 4) #obliczamy resztę z dzielenia liczby 13 przez 4

lista_zwierzat_parzyste = []

for z in lista_zwierzat:
    if len(z) % 2 == 0: #Jesli długość nazwy zwierzęcia daje przy dzieleniu przez 2 resztę 0 to...
        lista_zwierzat_parzyste.append(z)
print(lista_zwierzat_parzyste)

#Chcemy aby na liście pozostały tylko te nazwy zwierząt, które mają parzystą liczbę liter - z wyrażeniami listowymi
lista_zwierzat_parzyste2 = [z for z in lista_zwierzat if len(z) % 2 == 0]
print(lista_zwierzat_parzyste2)

#Ile jest liczb podzielnych na 4 w zakresie podanym przez użytkownika
a = int(input('Podaj pierwszą liczbę'))
b = int(input('Podaj drugą liczbę'))
print(len([i for i in range(a, b + 1) if i % 4 == 0]))

wynik = []

for i in range(a, b + 1):
    if i % 4 == 0:
        wynik.append(i)
print(len(wynik))

#Chcemy zamienić wszystkie elementy listy na liczby typu int
lista25 = ['123', '45', '7']
lista25_int = [int(n) for n in lista25]
lista25_int2 = list(map(int, lista25))
print(lista25_int2)



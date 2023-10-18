zmień origin w commit i wyślij do swojego repozytorium
import turtle

# Inicjalizacja okna Turtle
wn = turtle.Screen()
wn.bgcolor("white")

# Utworzenie żółwia
t = turtle.Turtle()
t.speed(0)  # Ustaw szybkość na maksymalną

# Pętla tworząca niekończący się wielokąt
while True:
    for i in range(4):  # Przykład: Tworzymy kwadrat
        t.forward(100)
        t.right(90)
    t.right(10)  # Zmiana kąta obrotu, aby uzyskać nieregularny kształt

# Poniższy kod sprawi, że okno Turtle nie zostanie zamknięte po narysowaniu
turtle.done()
import math
import tkinter as tk

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    if b == 0 and c == 0:
        result_label.config(text='x = 0')
    elif b == 0 and c != 0:
        if -c / a > 0:
            result_label.config(text='x1 = ' + str(math.sqrt(-c/a)))
            result2_label.config(text='x2 = ' + str(-math.sqrt(-c / a)))
        elif -c / a < 0:
            result_label.config(text='sprzeczne')
    elif c == 0 and b != 0:
        result_label.config(text='1x = 0')
        result2_label.config(text='2x = ' + str(-b/a))
    else:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            result_label.config(text='x1 = ' + str((-b + math.sqrt(delta)) / (2 * a)))
            result2_label.config(text='x2 = ' + str((-b - math.sqrt(delta)) / (2 * a)))
        elif delta == 0:
            result_label.config(text='x =' + str(-b / (2 * a)))
        else:
            result_label.config(text='sprzecze')

window = tk.Tk()
window.title("delta calculator")

label_a = tk.Label(window, text="Podaj a:")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

label_b = tk.Label(window, text="Podaj b:")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

label_c = tk.Label(window, text="Podaj c:")
label_c.pack()
entry_c = tk.Entry(window)
entry_c.pack()

calculate_button = tk.Button(window, text="Oblicz", command=calculate)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

result2_label = tk.Label(window, text="")
result2_label.pack()

window.mainloop()
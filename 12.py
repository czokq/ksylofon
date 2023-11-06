import sys
import tkinter as tk

def calculate_result():
    jp = int(jp_entry.get())
    jo = int(jo_entry.get())
    ujp = int(ujp_entry.get())
    d = int(d_entry.get())

    if ujp < 0 or jo < 0 or ujp < 0 or d < 0:
        result_label.config(text="Liczba nie może być ujemna", fg="red")  # Set text color to red
        return

    wynik = (jp + jo + ujp + d) / 4

    if jp >= 30 and jo >= 30 and ujp >= 30 and ujp >= 30 and d >= 30:
        result_label.config(text="Zdałeś bez amnestii", fg="green")  # Set text color to green
    elif wynik > 30:
        result_label.config(text="Zdałeś z amnestią", fg="green")  # Set text color to green
    else:
        result_label.config(text="Nie zdałeś", fg="red")  # Set text color to red

window = tk.Tk()
window.title("Exam Result Calculator")

jp_label = tk.Label(window, text="Wynik język polski:")
jp_label.pack()

jp_entry = tk.Entry(window, justify='center')
jp_entry.pack()

jo_label = tk.Label(window, text="Wynik język obcy:")
jo_label.pack()

jo_entry = tk.Entry(window, justify='center')
jo_entry.pack()

ujp_label = tk.Label(window, text="Wynik ustny język polski:")
ujp_label.pack()

ujp_entry = tk.Entry(window, justify='center')
ujp_entry.pack()

d_label = tk.Label(window, text="Wynik dodatkowy:")
d_label.pack()

d_entry = tk.Entry(window, justify='center')
d_entry.pack()

calculate_button = tk.Button(window, text="Oblicz", command=calculate_result)
calculate_button.pack()

result_label = tk.Label(window, text="", fg="black")  # Set default text color to black
result_label.pack()

window.mainloop()
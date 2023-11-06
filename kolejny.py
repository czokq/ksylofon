import sys
import tkinter as tk


def submit():
    cm = entry.get()
    label.config(text="jestes w grupie zawansowanej" + cm)

    if wynik >= 90:
        print("dostałeś się do grupy zawansowanej")
        sys.exit(0)

    if ocena >= 5:
        print("dostałeś się do grupy zawansowanej")
        sys.exit(0)
    else:
        print("dostałeś się do grupy niezawannsowanej")
        sys.exit(0)

window = tk.Tk()
window.title("zdałeś?")

label = tk.Label(window, text="wynik:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=submit)
button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
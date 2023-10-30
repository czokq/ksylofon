import tkinter as tk

def submit():
    cm = entry.get()
    label.config(text="twoj wzrost to: " + cm)

window = tk.Tk()
window.title("ile cm bratku?")

label = tk.Label(window, text="wprowadz wzrost:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=submit)
button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
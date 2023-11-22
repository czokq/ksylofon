import tkinter as tk

def submit():
    gender = entry.get()
    label.config(text="Your gender is: " + gender)

window = tk.Tk()
window.title("Gender Input Program")

label = tk.Label(window, text="Enter your gender:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=submit)
button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
import tkinter as tk

window = tk.Tk()
window.geometry("300x500")
logo = tk.PhotoImage(file="1.gif")


def img():
    tk.Label(window, image=logo).pack()

btn = tk.Button(window, text="向阳", command=img).pack()

window.mainloop()


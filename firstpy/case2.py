import tkinter as tk

win = tk.Tk()
win.title("Python Gui")
win.geometry("400x400")
aLabel = tk.Label(win, text="A Lable", font=("Arial", 12))
aLabel.pack()


def clickMe():
    global action
    action.configure(text="**Thinks!**")
    aLabel.configure(foreground="red")


action = tk.Button(win, text="Hit Me", command=clickMe)

action.pack()
win.mainloop()
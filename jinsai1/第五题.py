import tkinter as tk
import random
win = tk.Tk()
win.title("tk")
win.geometry("500x400")

input_lab = tk.Label(win, text="Enter a Number:")
input_lab.pack()

entry_box = tk.Entry(win)
entry_box.pack()


def hit_bt():
    i = 0
    while i < int(entry_box.get()):
        result = random.randint(0, 100000)
        txt_box.insert("end", str(result)+"\n")
        i += 1


hit_but = tk.Button(win, text="GENERATE THE RANDOM NUMBERS", command=hit_bt)
hit_but.pack()

txt_box = tk.Text(win)
txt_box.pack()

win.mainloop()
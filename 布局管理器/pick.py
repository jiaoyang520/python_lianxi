import tkinter as tk
win = tk.Tk()
win.geometry("500x500")

entry = tk.Entry(win, width=17, font=("Arial", 20))
entry.pack()


def hit():
    text.insert("end", str(entry.get()) + "\n")


bt = tk.Button(win, text="按钮", command=hit)
bt.pack()

text = tk.Text(win, width=50, bg="pink")
text.pack()

win.mainloop()
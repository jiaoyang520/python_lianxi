import tkinter as tk
win = tk.Tk()
win.title("tk")
win.geometry("500x300")
show_lab = tk.Label(win, text="展示区\n-----------------------------")
show_lab.pack()


def hit_bt():
    show_txt.insert("end", "老师1\n老师2\n老师3\n老师4\n老师5")


hit_but = tk.Button(win, text="hit", command=hit_bt)
hit_but.pack()

show_txt = tk.Text(win, width=60, height=10)
show_txt.pack()

win.mainloop()
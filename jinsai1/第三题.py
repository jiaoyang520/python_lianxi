import tkinter as tk
win = tk.Tk()
win.title("tk")
win.geometry("500x300")

lab_num1 = tk.Label(win, text="第一个数字")
lab_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(win, width=10)
entry_num1.grid(row=0, column=1)

lab_num2 = tk.Label(win, text="第二个数字")
lab_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(win, width=10)
entry_num2.grid(row=1, column=1)


# 定义按钮函数
def jia():
    jia_lab = tk.Label(win, text=(int(entry_num1.get())+int(entry_num2.get())))
    jia_lab.grid(row=2, column=1)


def jian():
    jian_lab = tk.Label(win, text=(int(entry_num1.get()) - int(entry_num2.get())))
    jian_lab.grid(row=2, column=2)


def cheng():
    cheng_lab = tk.Label(win, text=(int(entry_num1.get()) * int(entry_num2.get())))
    cheng_lab.grid(row=2, column=3)


def chu():
    chu_lab = tk.Label(win, text=(int(entry_num1.get()) / int(entry_num2.get())))
    chu_lab.grid(row=2, column=4)


# 定义按钮
jia_but = tk.Button(win, text="+", width=10, command=jia)
jia_but.grid(row=3, column=1)

jian_but = tk.Button(win, text="-", width=10, command=jian)
jian_but.grid(row=3, column=2)

cheng_but = tk.Button(win, text="*", width=10, command=cheng)
cheng_but.grid(row=3, column=3)

chu_but = tk.Button(win, text="/", width=10, command=chu)
chu_but.grid(row=3, column=4)


win.mainloop()
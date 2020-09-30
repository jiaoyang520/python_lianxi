import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("tk")
# 设置窗口大小
win.geometry("500x300")
# 设置第一个输入框名称和输入框
Lab1 = tk.Label(win, text="第一个数字", borderwidth=10)
Lab1.grid(row=1, column=0)
entry1 = tk.Entry(win, width=10, fg="black")
entry1.grid(row=1, column=1)
# 设置第二个输入框名称和输入框
Lab2 = tk.Label(win, text="第二个数字")
Lab2.grid(row=2, column=0)
entry2 = tk.Entry(win, width=10, fg="black")
entry2.grid(row=2, column=1)


def jia():
    et1 = int(entry1.get())
    et2 = int(entry2.get())
    result = tk.Label(win, text=et1+et2)
    result.grid(row=3, column=1)


def jian():
    et1 = int(entry1.get())
    et2 = int(entry2.get())
    result = tk.Label(win, text=et1-et2)
    result.grid(row=3, column=2)


def cheng():
    et1 = int(entry1.get())
    et2 = int(entry2.get())
    result = tk.Label(win, text=et1*et2)
    result.grid(row=3, column=3)


def chu():
    et1 = int(entry1.get())
    et2 = int(entry2.get())
    result = tk.Label(win, text=et1/et2)
    result.grid(row=3, column=4)


# 定义加减乘除四个按钮
but1 = tk.Button(win, text="+", width=10, command=jia)
but1.grid(row=4, column=1)

but2 = tk.Button(win, text="-", width=10, command=jian)
but2.grid(row=4, column=2)

but3 = tk.Button(win, text="*", width=10, command=cheng)
but3.grid(row=4, column=3)

but4 = tk.Button(win, text="/", width=10, command=chu)
but4.grid(row=4, column=4)



win.mainloop()

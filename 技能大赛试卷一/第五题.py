import tkinter as tk
import random
# 实例化窗口
win = tk.Tk()
# 设置窗口大小
win.geometry("400x400")
# 定义窗口标题
win.title("My Random Number")
# 定义输入框和输入框名称
Lab1 = tk.Label(win, text="Enter a Number")
Lab1.pack()
entry1 = tk.Entry(win, width=10, fg="black")
entry1.pack()


# 定义按钮回调的函数
def bt1():
    i = 0
    while (i < int(entry1.get())):
        ran = random.randint(0, 100000)
        text1.insert("end", ran)
        text1.insert("end", "\n")
        i += 1


but1 = tk.Button(win, text="Generate The Random Numbers", command=bt1)
but1.pack()

# 设置一个多行文本框
text1 = tk.Text(win)
text1.pack()

win.mainloop()
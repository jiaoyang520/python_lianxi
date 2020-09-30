import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口的标题
win.title("My Window")
# 设置窗口的尺寸
win.geometry("500x300")
# 声明字符串变量
var = tk.StringVar()
# 为变量赋值
var.set("Guess who i am?")
# 设置一个标签控件
Lab1 = tk.Label(win, textvariable=var, bg="pink", font=("Arial", 12), width=30, height=2)
# 将标签布局
Lab1.pack()


# 定义按钮的回调函数
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("national defense handsome boy")
    else:
        on_hit = False
        var.set("")


# 设置按钮
but1 = tk.Button(win, text="hit me", width=15, height=2, command=hit_me)
but1.pack()
# 循环显示
win.mainloop()
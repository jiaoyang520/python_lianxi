import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("身份展示器")
# 设置窗口大小
win.geometry("500x500")
# 定义一个字符串存储器
var = tk.StringVar()
# 设置给存储器赋标签的初始值
var.set("Guess who i am?")
# 定义显示标签
show_lab = tk.Label(win, textvariable=var, width=20, height=5, bg="pink", font=("Arial", 20))
show_lab.pack()


# 定义按钮的点击事件
on_hit = False
def hit_bt():
    global on_hit
    if on_hit == False:
        var.set("national defense handsome boy")
        on_hit = True
    else:
        var.set("")
        on_hit = False


# 定义按钮
hit_but = tk.Button(win, text="hit me", command=hit_bt)
hit_but.pack()

win.mainloop()
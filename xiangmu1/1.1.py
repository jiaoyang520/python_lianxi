import tkinter as tk
window = tk.Tk()
window.title("My Window")
window.geometry("500x500")
# 定义一个字符串变量
var = tk.StringVar()
# 设置字符串内容
var.set("点击前")
la = tk.Label(window, textvariable=var, background="pink", font=("Arial", 12), width=60, height=10)
# 将标签对其放置
la.pack()
# 定义一个False的变量
on_hit = False
# 点击按钮事件，当点击按钮时，调用此函数


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("点击后")
    else:
        on_hit = False
        var.set("")


# 设置按钮，并设置文本。command关联一个函数，当按钮被点击时，调用函数
bu = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)
# pack组件布局管理器，调整控件的位置和大小(必须设置布局管理器，控件才会显示)(pack(),grid(),place())
bu.pack()
# 循环显示
window.mainloop()
import tkinter as tk   # 导包

window = tk.Tk()    # 实例化窗口
window.title("My Window")   # 设置窗口标题
window.geometry("200x300")  # 设置窗口尺寸
var = tk.StringVar()    # 字符串变量
var.set("Guess who i am")   # 赋值
l = tk.Label(window, textvariable=var, bg="pink", font=("Arial", 12), width=30, height=2)
l.pack()    # Label标签对齐
on_hit = False


# 点击事件方法
def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set("national defense handsome boy")
    else:
        on_hit = False
        var.set("")


b = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)    # 设置按钮

b.pack()    # 将Button对齐

window.mainloop()   # 循环显示



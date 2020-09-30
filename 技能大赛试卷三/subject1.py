import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("字符相等鉴别器")
# 设置窗口大小
win.geometry("400x400")
# 设置鉴别器标题
jbq_title = tk.Label(win, text="String Comparison on Python Gui", font=("Arial", 13))
jbq_title.pack()
# 设置两个输入框名及输入框
input_box_name1 = tk.Label(win, text="word1", font=("Arial", 12))
input_box_name1.place(x=70, y=50)
input_box1 = tk.Entry(win)
input_box1.place(x=30, y=80)

input_box_name2 = tk.Label(win, text="word2", font=("Arial", 12))
input_box_name2.place(x=250, y=50)
input_box2 = tk.Entry(win)
input_box2.place(x=210, y=80)

# 声明一个字符串变量并设置鉴别结果展示标签框
var = tk.StringVar()
result_box = tk.Label(win, textvariable=var, bg="blue", width=20, height=10)
result_box.place(x=210, y=150)


# == 两个字符串相等按钮的回调函数
def equality_string():
    if input_box1.get() == input_box2.get():
        var.set("True")
    else:
        var.set("False")


# != 两个字符串不相等按钮的回调函数
def no_equality_string():
    if input_box1.get() != input_box2.get():
        var.set("True")
    else:
        var.set("False")


# 定义相等比较按钮
equality_but = tk.Button(win, text=" == ", width=20, height=3, command=equality_string)
equality_but.place(x=30, y=150)

# 定义不相等比较按钮
no_equality_but = tk.Button(win, text=" != ", width=20, height=3, command=no_equality_string)
no_equality_but.place(x=30, y=260)

win.mainloop()
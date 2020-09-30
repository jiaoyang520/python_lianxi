import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("可交互简单计算器")
# 设置窗口大小
win.geometry("500x500")
# 设置窗口输入框名和输入框
input_name1 = tk.Label(win, text="第一个数字:")
input_name1.grid(row=0, column=0)
input_entry1 = tk.Entry(win, width=10)
input_entry1.grid(row=0, column=1)

input_name2 = tk.Label(win, text="第二个数字:")
input_name2.grid(row=1, column=0)
input_entry2 = tk.Entry(win, width=10)
input_entry2.grid(row=1, column=1)


# +按钮的点击事件
def jia():
    result_jia = tk.Label(win, text=int(input_entry1.get())+int(input_entry2.get()), width=10)
    result_jia.grid(row=3, column=1)


# -按钮的点击事件
def jian():
    result_jian = tk.Label(win, text=int(input_entry1.get())-int(input_entry2.get()), width=10)
    result_jian.grid(row=3, column=2)


# *按钮的点击事件
def cheng():
    result_cheng = tk.Label(win, text=int(input_entry1.get())*int(input_entry2.get()), width=10)
    result_cheng.grid(row=3, column=3)


# /按钮的点击事件
def chu():
    result_chu = tk.Label(win, text=int(input_entry1.get())/int(input_entry2.get()), width=10)
    result_chu.grid(row=3, column=4)


# 定义+按钮
jia_but = tk.Button(win, text="+", command=jia, width=10)
jia_but.grid(row=4, column=1)

# 定义-按钮
jian_but = tk.Button(win, text="-", command=jian, width=10)
jian_but.grid(row=4, column=2)

# 定义*按钮
cheng_but = tk.Button(win, text="*", command=cheng, width=10)
cheng_but.grid(row=4, column=3)

# 定义/按钮
chu_but = tk.Button(win, text="/", command=chu, width=10)
chu_but.grid(row=4, column=4)





win.mainloop()
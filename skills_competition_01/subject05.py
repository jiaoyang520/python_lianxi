import tkinter as tk
import random as ran
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("随机数生成器")
# 设置窗口大小
win.geometry("400x400")
# 设置输入框名和输入框
input_box_name = tk.Label(win, text="Enter a Number")
input_box_name.pack()
entry_box = tk.Entry(win, width=15)
entry_box.pack()


# 设置函数的点击事件
def hit_bt():
    num = 0
    while num < int(entry_box.get()):
        result = ran.randint(0, 100000)
        ran_txt.insert("end", str(result)+"\n")
        num += 1


# 设置按钮
ran_but = tk.Button(win, text="GENERATE THE RANDOM NUMBERS", command=hit_bt)
ran_but.pack()

# 设置多行文本框用来接收信息
ran_txt = tk.Text(win)
ran_txt.pack()

# 循环显示
win.mainloop()
import tkinter as tk
from tkinter import *
win = tk.Tk()
win.title("进制转换器1.1")
win.geometry("800x200")
# 设置项目标题标签
title = tk.Label(win, text="Declmal To Binary Conversion\n---------------------------------------")
title.grid(row=0, column=1)
# 输入框标签标签名
t1 = tk.Label(win, text="insert the number")
t1.grid(row=1, column=0)
# 创建输入框Entry，用来输入之前的数字
t1 = tk.Entry(win, bd=5, width=15)
t1.grid(row=2, column=0, sticky=W)
# 设置点击事件
def Click_Me():
    """计算十进制转二进制"""
    # 从输入框中获取十进制数，转为整数，再使用bin函数转为二进制,在强转为字符串
    n = str(bin(int(t1.get())))
    # 删除转为二进制留下的"0b"
    m = n.replace("0b", "")
    if len(m) <= 8:
        """判断长度，不够8位在前面添加相应的0"""
        m = (8-len(m))*"0"+m
        b7.insert(END, m)


# 设置二进制每位的显示框及其名称
b7 = tk.Text(win, bd=5, width=5, height=3)
# sticky 组件紧贴所在单元格的某一角，对应于东南西北中以及 4 个角
b7.grid(row=2, column=2, sticky=W)
Lb7 = tk.Label(win, text="bit7")
Lb7.grid(row=3, column=2)

b6 = tk.Text(win, bd=5, width=5, height=3)
b6.grid(row=2, column=3)
Lb6 = tk.Label(win, text="bit6")
Lb6.grid(row=3, column=3)

b5 = tk.Text(win, bd=5, width=5, height=3)
b5.grid(row=2, column=4)
Lb5 = tk.Label(win, text="bit5")
Lb5.grid(row=3, column=4)

b4 = tk.Text(win, bd=5, width=5, height=3)
b4.grid(row=2, column=5, sticky=W)
Lb4 = tk.Label(win, text="bit4")
Lb4.grid(row=3, column=5)

b3 = tk.Text(win, bd=5, width=5, height=3)
b3.grid(row=2, column=6, sticky=W)
Lb3 = tk.Label(win, text="bit3")
Lb3.grid(row=3, column=6)

b2 = tk.Text(win, bd=5, width=5, height=3)
b2.grid(row=2, column=7, sticky=W)
Lb2 = tk.Label(win, text="bit2")
Lb2.grid(row=3, column=7)

b1 = tk.Text(win, bd=5, width=5, height=3)
b1.grid(row=2, column=8, sticky=W)
Lb1 = tk.Label(win, text="bit1")
Lb1.grid(row=3, column=8)


but = tk.Button(win, Text="Click_Me", command=Click_Me)
but.grid(row=4, column=0, sticty=W)

win.mainloop()
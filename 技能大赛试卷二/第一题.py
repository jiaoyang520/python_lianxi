import tkinter as tk
# 窗口实例化
win = tk.Tk()
# 设置窗口标题
win.title("爱国表白神器")
# 设置窗口大小
win.geometry("400x400")
# 定义多行文本框
text1 = tk.Text(win)
text1.pack()


# 定义按钮回调函数
def bt1():
    for i in range(11):
        text1.insert("end", "i love china\n")


but1 = tk.Button(win, text="Dispiay", command=bt1)
but1.pack()

win.mainloop()
import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口大小
win.geometry("800x300")
# 定义标签用来显示  展示区   和横线
Lab1 = tk.Label(win, text="展示区")
Lab1.pack()
Lab2 = tk.Label(win, text="-----------------------")
Lab2.pack()


# 定义按钮的回调函数
def but_1():
    text1.insert("insert", "老师1\n老师2\n老师3\n老师4\n老师5")


# 定义按钮
but1 = tk.Button(win, text="hit", command=but_1)
but1.pack()
# 定义一个多行文本框，显示多行文字
text1 = tk.Text(win, height="10")
text1.pack()

# 页面循环调用
win.mainloop()
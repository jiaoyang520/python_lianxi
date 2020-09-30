import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("无交互讲师展示器")
# 设置窗口大小
win.geometry("500x300")
# 设置交互器标题
name_lab = tk.Label(win, text="展示区\n------------------------------")
name_lab.pack()


# 定义按钮的点击事件
def hit_bt():
    hit_tet.insert("end", "老师1\n老师2\n老师3\n老师4\n老师5")


# 设置按钮
hit_but = tk.Button(win, text="hit", command=hit_bt)
hit_but.pack()

# 设置文本框
hit_tet = tk.Text(win, height=10, width=50)
hit_tet.pack()


# 循环显示
win.mainloop()
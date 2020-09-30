import tkinter as tk

# 窗口实例化
win = tk.Tk()
# 定义窗口标题
win.title("图像展示器")
# 定义窗口大小
win.geometry("500x400")
# 初始化图片
img = tk.PhotoImage(file="timg.gif")


# 定义按钮的点击事件
def img_bt():
    img_Label = tk.Label(win, image=img)
    img_Label.pack()


# 定义按钮
img_but = tk.Button(win, text="Hit Me", command=img_bt)
img_but.pack()

# 循环显示
win.mainloop()

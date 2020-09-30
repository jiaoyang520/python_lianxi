import tkinter as tk

# 实例化窗口
win = tk.Tk()
win.geometry("500x380")
# 初始化图片
photo = tk.PhotoImage(file="timg.gif")


# 定义函数
def img():
    Lab1 = tk.Label(win, image=photo)
    Lab1.pack()


# 定义按钮并回调函数
but1 = tk.Button(win, text="Hit me", command=img)
but1.pack()

win.mainloop()

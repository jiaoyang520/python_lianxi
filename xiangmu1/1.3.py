import tkinter as tk

# 实例化窗口
window = tk.Tk()
window.title("案例1.3")
window.geometry("500x900")
# 初始化图片
pho = tk.PhotoImage(file="timg.gif")


def img():
    lab1 = tk.Label(window, image=pho, activebackground="#C71585")
    lab1.pack()


bu1 = tk.Button(window, text="按钮1", command=img, background="#f56565", width="5", height="2")
bu1.pack()

window.mainloop()

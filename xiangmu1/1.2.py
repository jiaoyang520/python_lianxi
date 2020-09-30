import tkinter as tk
window = tk.Tk()
window.title("案例 1.2")
window.geometry("500x500")
alab = tk.Label(window, text="向阳",background="#565665", font=("Arial", 20))
alab.pack()


# 设置按钮被点击的函数
def b1():
    action.configure(text="!!!!!!!!!!!")
    alab.configure(foreground="red")


action = tk.Button(window, text="按钮", command=b1, background="#125678")
action.pack()
window.mainloop()
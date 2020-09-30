import tkinter as tk
# 窗口实例化
win = tk.Tk()
# 设置窗口标题
win.title("爱国表白神器")
# 设置窗口大小
win.geometry("500x500")
# 设置一个多行文本框用来接收信息
receive_txt = tk.Text(win, bg="lightgreen")
receive_txt.pack()


# 设置按钮的点击事件
def hit_bt():
    for i in range(11):
        receive_txt.insert("end", "i love china\n")


# 设置按钮
show_txt_but = tk.Button(win, text="Display", command=hit_bt)
show_txt_but.pack()



win.mainloop()


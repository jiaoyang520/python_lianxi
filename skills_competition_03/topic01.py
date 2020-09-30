import tkinter as tk
win = tk.Tk()
win.title("字符相等鉴别器")
win.geometry("600x600")
# 设置鉴别器标题
title_lab = tk.Label(win, text="STRING COMPARISON ON PYTHON GUI", font=("Arial", 18))
title_lab.pack()

# 设置第一个字符输入框名和输入框
input_word1 = tk.Label(win, text="Word1", font=("Arial", 13))
input_word1.place(x=120, y=80)
entry_word1 = tk.Entry(win, font=("Arial", 13))
entry_word1.place(x=50, y=120)

# 设置第二个字符输入框名和输入框
input_word2 = tk.Label(win, text="Word1", font=("Arial", 13))
input_word2.place(x=420, y=80)
entry_word2 = tk.Entry(win, font=("Arial", 13))
entry_word2.place(x=350, y=120)

# 设置结果显示面板
result_lab = tk.Label(win, text="", width=9, height=6, bg="#931DD6", font=("Arial", 27))
result_lab.place(x=350, y=200)


# 定义==按钮的回调函数
def dengyu_bt():
    if entry_word1.get() == entry_word2.get():
        result_lab.configure(text=str("True"))
    else:
        result_lab.configure(text=str("False"))


# 定义!=按钮的回调函数
def no_dengyu_bt():
    if entry_word1.get() == entry_word2.get():
        result_lab.configure(text=str("False"))
    else:
        result_lab.configure(text=str("True"))


# 定义==按钮
dengyu_but = tk.Button(win, text="==", width=20, height=4, command=dengyu_bt, font=("Arial", 13))
dengyu_but.place(x=50, y=230)

# 定义!=按钮
dengyu_but = tk.Button(win, text="!=", width=20, height=4, command=no_dengyu_bt, font=("Arial", 13))
dengyu_but.place(x=50, y=350)

win.mainloop()
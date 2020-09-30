import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("公民信息展示器")
# 设置窗口大小
win.geometry("400x400")
# 设置窗口标题
Lab0 = tk.Label(win, text="Citizen Data Form\n-----------------------", font=("Arial", 12))
Lab0.grid(row=0, column=1, padx=50)
# 设置id标签和输入框
Lab1 = tk.Label(win, text="id")
Lab1.grid(row=1, column=0, padx=20)
entry1 = tk.Entry(win)
entry1.grid(row=1, column=1)
# 设置Name标签和输入框
Lab2 = tk.Label(win, text="Name")
Lab2.grid(row=2, column=0)
entry2 = tk.Entry(win)
entry2.grid(row=2, column=1)
# 设置Title标签及输入框
Lab3 = tk.Label(win, text="Title")
Lab3.grid(row=3, column=0)
entry3 = tk.Entry(win)
entry3.grid(row=3, column=1)
# 设置PDB标签及输入框
Lab4 = tk.Label(win, text="PDB")
Lab4.grid(row=4, column=0)
entry4 = tk.Entry(win)
entry4.grid(row=4, column=1)
# 设置address标签及输入框
Lab5 = tk.Label(win, text="address")
Lab5.grid(row=5, column=0)
entry5 = tk.Entry(win)
entry5.grid(row=5, column=1)
# 设置enduction标签及输入框
Lab6 = tk.Label(win, text="enduction")
Lab6.grid(row=6, column=0)
entry6 = tk.Entry(win)
entry6.grid(row=6, column=1)

# 定义展示区名和横线
zn_lab = tk.Label(win, text="DETAIL\n--------------------", font=("Arial", 12))
zn_lab.grid(row=8, column=1)


# 定义展示区的六个标签的名称和显示区
z_lab1 = tk.Label(win, text="id")
z_lab1.grid(row=9, column=0)
n_lab1 = tk.Label(win, text="")
n_lab1.grid(row=9, column=1)

z_lab2 = tk.Label(win, text="Name")
z_lab2.grid(row=10, column=0)
n_lab2 = tk.Label(win, text="")
n_lab2.grid(row=10, column=1)

z_lab3 = tk.Label(win, text="Title")
z_lab3.grid(row=11, column=0)
n_lab3 = tk.Label(win, text="")
n_lab3.grid(row=11, column=1)

z_lab4 = tk.Label(win, text="PDB")
z_lab4.grid(row=12, column=0)
n_lab4 = tk.Label(win, text="")
n_lab4.grid(row=12, column=1)

z_lab5 = tk.Label(win, text="address")
z_lab5.grid(row=13, column=0)
n_lab5 = tk.Label(win, text="")
n_lab5.grid(row=13, column=1)

z_lab6 = tk.Label(win, text="eduction")
z_lab6.grid(row=14, column=0)
n_lab6 = tk.Label(win, text="")
n_lab6.grid(row=14, column=1)


# 定义按钮回调函数
def bt1():
    n_lab1.configure(text=str(entry1.get()))
    n_lab2.configure(text=str(entry2.get()))
    n_lab3.configure(text=str(entry3.get()))
    n_lab4.configure(text=str(entry4.get()))
    n_lab5.configure(text=str(entry5.get()))
    n_lab6.configure(text=str(entry6.get()))


# 定义一个按钮
but1 = tk.Button(win, text="pricess", command=bt1)
but1.grid(row=7, column=1)


win.mainloop()
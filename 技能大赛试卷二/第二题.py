import tkinter as tk
# 窗口实例化
win = tk.Tk()
# 设置窗口大小
win.geometry("400x400")
# 设置窗口标题
win.title("简单税务计算器")
# 设置计算器标题名称及横线隔开
Lab0 = tk.Label(win, text="Stego Store apps\n----------------------------------", font=("Arial", 12))
Lab0.grid(row=0, column=1)
# 项目名称及输入框
Lab1 = tk.Label(win, text="item")
Lab1.grid(row=1)
entry1 = tk.Entry(win, bd=5)
entry1.grid(row=1, column=1, padx=10, pady=5)
# 价格名称和输入框
Lab2 = tk.Label(win, text="Unit Price")
Lab2.grid(row=2, column=0)
entry2 = tk.Entry(win, bd=5)
entry2.grid(row=2, column=1, padx=10, pady=5)
# 数量名称和输入框
Lab3 = tk.Label(win, text="Quantity")
Lab3.grid(row=3, column=0)
entry3 = tk.Entry(win, bd=5)
entry3.grid(row=3, column=1, padx=10, pady=5)
# 总付款名称和显示
Lab4 = tk.Label(win, text="Price")
Lab4.grid(row=4, column=0)
Lab_p = tk.Label(win, text="")
Lab_p.grid(row=4, column=1, padx=10, pady=5)
# 税名称和显示
Lab5 = tk.Label(win, text="Tax")
Lab5.grid(row=6, column=0)
Lab_t = tk.Label(win, text="")
Lab_t.grid(row=6, column=1, padx=10, pady=5)


# 定义按钮回调函数并要执行的内容
def bt1():
    price = int(entry2.get())
    quantity = int(entry3.get())
    # 计算总税务
    totalprice = (price * quantity)*0.02
    Lab_t.configure(text=str(totalprice))
    
    # 计算总付款
    TotalPaid = price * quantity
    Lab_p.configure(text=str(TotalPaid))


# 定义按钮
but1 = tk.Button(win, text="Process", command=bt1)
but1.grid(row=5, column=1)

win.mainloop()
import tkinter as tk
win = tk.Tk()
win.title("税务计算器")
win.geometry("500x500")
# 设置计算器页面标题
title_tax_lab = tk.Label(win, text="STEGO STORE APPS\n-------------------------------------", font=("Arial", 18))
title_tax_lab.grid(row=0, column=1)

# 设置项目输入框名和输入框
item_name = tk.Label(win, text="item", font=("Arial", 15))
item_name.grid(row=1, column=0, padx=20)
item_entry = tk.Entry(win, font=("Arial", 15))
item_entry.grid(row=1, column=1, padx=20)

# 设置单价输入框名和输入框
unit_price_name = tk.Label(win, text="Unit Price", font=("Arial", 15))
unit_price_name.grid(row=2, column=0)
unit_price_entry = tk.Entry(win, font=("Arial", 15))
unit_price_entry.grid(row=2, column=1, pady=20)

# 设置数量输入框名和输入框
quantity_name = tk.Label(win, text="Quantity", font=("Arial", 15))
quantity_name.grid(row=3, column=0)
quantity_entry = tk.Entry(win, font=("Arial", 15))
quantity_entry.grid(row=3, column=1)

# 设置总价格输入框名华人输入框
price_name = tk.Label(win, text="Price", font=("Arial", 15))
price_name.grid(row=4, column=0)
price_txt = tk.Label(win, text="", font=("Arial", 15), width=10)
price_txt.grid(row=4, column=1, pady=10)

# 设置纳税输入框名和输入框
tax_name = tk.Label(win, text="Tax", font=("Arial", 15))
tax_name.grid(row=6, column=0)
tax_txt = tk.Label(win, text="", font=("Arial", 15), width=10)
tax_txt.grid(row=6, column=1)


# 设置按钮的回调函数
def process_bt():
    unit_price = int(unit_price_entry.get())
    quantity = int(quantity_entry.get())
    price_txt.configure(text=str(unit_price*quantity))
    tax_txt.configure(text=str((unit_price*quantity)*0.02))


# 设置按钮
process_but = tk.Button(win, text="Process", command=process_bt)
process_but.grid(row=5, column=1, pady=10)

win.mainloop()

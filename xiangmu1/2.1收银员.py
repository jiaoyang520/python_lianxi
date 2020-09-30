import tkinter as tk
window = tk.Tk()
window.title("收银员1.1")
window.geometry("500x400")
# row为行，column为列
lab0 = tk.Label(window, text="XiangYang STORE APPS\n -----------------------------------", font=('Arial', 18))
lab0.grid(row=0, column=1)
# 标签
lab1 = tk.Label(window, text="项目(item)")
lab1.grid(row=1)
lab2 = tk.Label(window, text="价格(Unit Price)")
lab2.grid(row=2)
lab3 = tk.Label(window, text="数量(Quantity)")
lab3.grid(row=3)
lab4 = tk.Label(window, text="折扣(Disconut)")
lab4.grid(row=4)
# 输入框
# padx:设置控件周围水平方向空白区域保留大小
# pady:设置控件周围垂直方向空白区域保留大小
# 项目输入框
item1 = tk.Entry(window, borderwidth=5)
item1.grid(row=1, column=1, padx=10, pady=5)
# 价格输入框
item2 = tk.Entry(window, borderwidth=5)
item2.grid(row=2, column=1, padx=10, pady=5)
# 数量输入框
item3 = tk.Entry(window, borderwidth=5)
item3.grid(row=3, column=1, padx=10, pady=5)
# 折扣输入框
item4 = tk.Entry(window, borderwidth=5, width=10)
item4.grid(row=4, column=1, padx=10, pady=5)
# 总折扣价显示标签和框
showToalDiscountname = tk.Label(window, text="总折扣")
showToalDiscountname.grid(row=6, column=0, padx=10, pady=10)
# 总付款显示标签和框
showToalPaidname = tk.Label(window, text="总付款")
showToalPaidname.grid(row=7, column=0, padx=10, pady=10)
def ClickMe():
    """点击计算总折扣和总付款"""
    # 获取价格输入框中的数据并转为int型
    price = int(item2.get())
    # 获取数量输入框中的数据
    quantity = int(item3.get())
    # 获取折扣输入框中的数据
    discount = int(item4.get()) * 0.1
    # 计算总折扣
    TotalDiscount = (price - price * discount) * quantity
    # 计算总付款价
    TotalPaid = price * quantity - TotalDiscount
    # 显示总折扣结果
    showToalDiscountresult = tk.Label(window, text=TotalDiscount, foreground="#9932CC", background="#ffb6c1")
    showToalDiscountresult.grid(row=6, column=1, padx=10, pady=10)
    # 显示总付款结果
    showToalPaidresult = tk.Label(window, text=TotalPaid, foreground="#9932CC", background="#ffb6c1")
    showToalPaidresult.grid(row=7, column=1, padx=10, pady=10)


butt = tk.Button(window, text="处理(process)", command=ClickMe)
butt.grid(row=5, column=1)
# 循环显示
window.mainloop()
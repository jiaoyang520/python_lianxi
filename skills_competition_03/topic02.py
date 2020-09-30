import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("城市人口统计器")
win.geometry("400x400")
# 创建城市列表
city_list = ["重庆市", "上海市", "北京市", "成都市", "天津市", "广州市", "深圳市", "武汉市", "南阳市", "西安市"]
# 创建人口数量列表
number_list = [3101, 2423, 2300, 1404, 1293, 1270, 1035, 910, 1026, 1000]
# 创建表格标题占位
columns_name = ("City", "Number")
# 创建表格对象
treeview = ttk.Treeview(win, height=13, show="headings", columns=columns_name)
treeview.place(x=70, y=80)
# 为表格占位设置参数
treeview.heading("City", text="City or District")
treeview.heading("Number", text="NUmber of Populatio")
# 设置表的宽度和居中对齐
treeview.column("City", width=120, anchor="center")
treeview.column("Number", width=120, anchor="center")


# 设置函数的回调
def tv_bt():
    for i in range(len(city_list)):
        treeview.insert("", i, values=(city_list[i], number_list[i]))


# 创建一个按钮
dispiay_but = tk.Button(win, text="Display Data", width=10, height=2, fg="pink", command=tv_bt)
dispiay_but.place(x=150, y=20)



win.mainloop()
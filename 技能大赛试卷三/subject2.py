import tkinter as tk
from tkinter import ttk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("my window")
# 设置窗口大小
win.geometry("400x400")
# 创建城市名称列表
city_name_list = ["重庆市", "上海市", "北京市", "成都市", "天津市", "广州市", "深圳市", "武汉市", "南阳市", "西安市"]
# 创建城市人口数量列表
city_people_num = [3101, 2423, 2300, 1404, 1293, 1270, 1035, 910, 1026, 1000]
# 创建表格标题的占位个数
columns_name = ("City", "Number")
# 创建表格对象
treeview = ttk.Treeview(win, height=10, show="headings", columns=columns_name)
treeview.place(x=80, y=100)
# 为表格标题占位设置参数   使用text属性设置
treeview.heading("City", text="City or District")
treeview.heading("Number", text="Number of Population")
# 设置表的宽度以及居中对齐    传的第一个参数是表格对象中给columns赋值的参数
treeview.column("City", width=120, anchor="center")
treeview.column("Number", width=120, anchor="center")


# 定义按钮的点击事件
def dispaly_bt():
    for i in range(0, len(city_people_num)):
        treeview.insert("", i, values=(city_name_list[i], city_people_num[i]))


# 创建一个按钮
dispaly_but = tk.Button(win, text="Display Date", width=13, height=2, fg="pink", command=dispaly_bt)
dispaly_but.place(x=160, y=20)


win.mainloop()

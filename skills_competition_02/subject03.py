import tkinter as tk
win = tk.Tk()
win.title("公民信息展示器")
win.geometry("500x600")
# 设置展示器页面标题
zhanshiqi_title = tk.Label(win, text="CITIZEM DATA FORM\n-----------------------------------", font=("Arial", 18))
zhanshiqi_title.grid(row=0, column=1)

# 设置id名和输入框
id_name = tk.Label(win, text="id", font=("Arial", 15))
id_name.grid(row=1, column=0, padx=35)
id_entry = tk.Entry(win, font=("Arial", 15))
id_entry.grid(row=1, column=1)

# 设置name名和输入框
name_name = tk.Label(win, text="name", font=("Arial", 15))
name_name.grid(row=2, column=0)
name_entry = tk.Entry(win, font=("Arial", 15))
name_entry.grid(row=2, column=1)

# 设置title名和输入框
title_name = tk.Label(win, text="title", font=("Arial", 15))
title_name.grid(row=3, column=0)
title_entry = tk.Entry(win, font=("Arial", 15))
title_entry.grid(row=3, column=1)

# 设置PDB名和输入框
PDB_name = tk.Label(win, text="PDB", font=("Arial", 15))
PDB_name.grid(row=4, column=0)
PDB_entry = tk.Entry(win, font=("Arial", 15))
PDB_entry.grid(row=4, column=1)

# 设置address名和输入框
address_name = tk.Label(win, text="address", font=("Arial", 15))
address_name.grid(row=5, column=0)
address_entry = tk.Entry(win, font=("Arial", 15))
address_entry.grid(row=5, column=1)

# 设置edution名和输入框
edution_name = tk.Label(win, text="edution", font=("Arial", 15))
edution_name.grid(row=6, column=0)
edution_entry = tk.Entry(win, font=("Arial", 15))
edution_entry.grid(row=6, column=1)

# 设置下半部分的页面标题
xiabanbu_title = tk.Label(win, text="DETAIL\n-----------------------------------", font=("Arial", 18))
xiabanbu_title.grid(row=8, column=1)

# 下半部分id
xia_id_name = tk.Label(win, text="id", font=("Arial", 15))
xia_id_name.grid(row=9, column=0)
xia_id_show = tk.Label(win, text="", font=("Arial", 15))
xia_id_show.grid(row=9, column=1, sticky="W")

# 下半部分name
xia_name_name = tk.Label(win, text="Name", font=("Arial", 15))
xia_name_name.grid(row=10, column=0)
xia_name_show = tk.Label(win, text="", font=("Arial", 15))
xia_name_show.grid(row=10, column=1, sticky="W")

# 下半部分title
xia_title_name = tk.Label(win, text="Title", font=("Arial", 15))
xia_title_name.grid(row=11, column=0)
xia_title_show = tk.Label(win, text="", font=("Arial", 15))
xia_title_show.grid(row=11, column=1, sticky="W")

# 下半部分PDB
xia_PDB_name = tk.Label(win, text="PDB", font=("Arial", 15))
xia_PDB_name.grid(row=12, column=0)
xia_PDB_show = tk.Label(win, text="", font=("Arial", 15))
xia_PDB_show.grid(row=12, column=1, sticky="W")

# 下半部分address
xia_address_name = tk.Label(win, text="address", font=("Arial", 15))
xia_address_name.grid(row=13, column=0)
xia_address_show = tk.Label(win, text="", font=("Arial", 15))
xia_address_show.grid(row=13, column=1, sticky="W")

# 下半部分eduction
xia_eduction_name = tk.Label(win, text="eduction", font=("Arial", 15))
xia_eduction_name.grid(row=14, column=0)
xia_eduction_show = tk.Label(win, text="", font=("Arial", 15))
xia_eduction_show.grid(row=14, column=1, sticky="W")


# 定义按钮的回调函数
def hit_bt():
    xia_id_show.configure(text=str(id_entry.get()))
    xia_name_show.configure(text=str(name_entry.get()))
    xia_title_show.configure(text=str(title_entry.get()))
    xia_PDB_show.configure(text=str(PDB_entry.get()))
    xia_address_show.configure(text=str(address_entry.get()))
    xia_eduction_show.configure(text=str(edution_entry.get()))


# 定义按钮
process_but = tk.Button(win, text="process", command=hit_bt, width=10, height=2)
process_but.grid(row=7, column=1, pady=10)



win.mainloop()
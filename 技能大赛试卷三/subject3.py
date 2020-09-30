import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("for循环累加器")
# 设置窗口大小
win.geometry("400x400")
# 设置一个frame容器
frame1 = tk.Frame(win)
frame1.grid(row=0, column=0, padx=10)
# 在容器中设置输入框名和输入框，结果显示框名和结果框
input_name_lab = tk.Label(frame1, text="Eenter the Number", font=("Arial", 13))
input_name_lab.grid(row=0, column=0, padx=10, pady=20)
input_entry = tk.Entry(frame1)
input_entry.grid(row=1, column=0)

result_name_box = tk.Label(frame1, text="TOTAL", font=("Arial", 13))
result_name_box.grid(row=2, column=0, pady=15)
result_box = tk.Text(frame1, width=16, height=10, font=("Arial", 13), bg="pink")
result_box.grid(row=3, column=0)

# 设置要累加的数的显示框
show_num = tk.Text(win, width=16, height=12, font=("Arial", 13))
show_num.grid(row=0, column=1)


# 设置按钮点击事件函数
def Click_Me_bt():
    result = 0
    for i in range(int(input_entry.get())+1):
        show_num.insert("end", i)
        show_num.insert("end", "\n")
        result = result + i
    result_box.insert("end", result)
    print(result)
    show_num.insert("end", "------------------------")
    show_num.insert("end", "\n")
    result_box.insert("end", "\n")


# 定义按钮
Click_Me_but = tk.Button(win, text="Click Me", command=Click_Me_bt)
Click_Me_but.grid(row=1, column=1)

win.mainloop()

import tkinter as tk
win = tk.Tk()
win.title("tk")
win.geometry("505x385")
img = tk.PhotoImage(file="timg.gif")


def hit_bt():
    img_lab = tk.Label(win, image=img)
    img_lab.pack()


hit_but = tk.Button(win, text="Hit me!", command=hit_bt)
hit_but.pack()



win.mainloop()
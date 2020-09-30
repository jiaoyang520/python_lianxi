import tkinter as tk
win = tk.Tk()
win.title("My window")
win.geometry("500x500")

var = tk.StringVar()
var.set("Guess who i am?")

show_lab = tk.Label(win, textvariable=var, width=40, height=3, bg="pink", font=("Arial", 13))
show_lab.pack()


hit_on = False
def hit_bt():
    global hit_on
    if hit_on == False:
        var.set("national defense handsome boy")
        hit_on = True
    else:
        var.set("")
        hit_on = False


hit_but = tk.Button(win, text="hit me", command=hit_bt, width=15, height=2)
hit_but.pack()




win.mainloop()
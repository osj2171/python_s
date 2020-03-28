import tkinter as tk
import random as r

root = tk.Tk()
root.geometry("400x200")

q_num = r.randint(1,20)

def check_num(num):
    global q_num
    if num == q_num:
        msg = "정답"
        txt.configure(state='readonly')
    elif num > q_num:
        msg = "아래"
    else:
        msg = "위"
    return  msg

def disp_msg():
    num = int(inum.get())
    msg = check_num(num)
    lbl.configure(text=msg)

inum = tk.StringVar()
lbl = tk.Label()
txt = tk.Entry(textvariable=inum)
btn = tk.Button(text="시도", command=disp_msg)

lbl.pack()
txt.pack()
btn.pack()
tk.mainloop()




import tkinter as tk
import random

def dis_label():
    num=list(range(1,46))
    random.shuffle(num)
    lbl.configure(text=num[:6])

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="")
btn = tk.Button(text="복권 번호", command=dis_label)

lbl.pack()
btn.pack()
tk.mainloop()
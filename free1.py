
import tkinter as tk
import random

root = tk.Tk()
root.geometry("200x100")

def dis_label():
    fortune = ['행복','보통','위험','매우 행복']
    lbl.configure(text="%s님 오늘은 %s이시군요." %(txt.get(), random.choice(fortune)))

name = tk.StringVar()
lbl = tk.Label(text="")
txt = tk.Entry(textvariable = name)
btn = tk.Button(text="오늘의 운세", command=dis_label)

lbl.pack()
txt.pack()
btn.pack()
tk.mainloop()


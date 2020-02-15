import tkinter as tk
import random

def dis_label():
    fortune = ['항복','보통','위험','매우 행복']
    lbl.configure(text=random.choice(fortune))

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="")
btn = tk.Button(text="오늘의 운세", command=dis_label)

lbl.pack()
btn.pack()
tk.mainloop()

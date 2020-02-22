
import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

def disp_Label():
    age = int(txt_age.get())
    lbl.configure(text="%s님, 내년에 %d살 입니다." %(txt_name.get(), age+1))

name = tk.StringVar()
age = tk.StringVar()

lbl = tk.Label(text="")
txt_name = tk.Entry(textvariable=name)
txt_age = tk.Entry(textvariable=age)
btn = tk.Button(text="PUSH", command=disp_Label)

lbl.pack()
txt_name.pack()
txt_age.pack()
btn.pack()
tk.mainloop()
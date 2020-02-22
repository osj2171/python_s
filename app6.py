
import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

def disp_Label():
    if int(txt.get()) == 20:
        lbl_recognize.configure(text="정답")
    else:
        lbl_recognize.configure(text="오답")

ans = tk.StringVar()

lbl_quiz = tk.Label(text="10+10=")
txt = tk.Entry(textvariable=ans)
btn = tk.Button(text="계산", command=disp_Label)
lbl_recognize = tk.Label(text="")

ans = tk.StringVar()

lbl_quiz.pack()
txt.pack()
btn.pack()
lbl_recognize.pack()
tk.mainloop()

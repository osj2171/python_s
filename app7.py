
import tkinter as tk
#윈도우 만들기
root = tk.Tk()
root.geometry("200x100")

height = tk.StringVar()
weight = tk.StringVar()

def disp_Label():
    h = int(txt_height.get())
    w = int(txt_weight.get())
    bmi = w / (h/100 * h/100)
    if bmi <= 18.5:
        msg = "저체중"
    elif bmi <= 23:
        msg = "정상"
    elif bmi <= 25:
        msg = "과체중"
    else:
        msg = "비만"

    lbl.configure(text="BMI 지수:%.2f, 판정: %s"% (bmi,msg))

txt_height = tk.Entry(textvariable=height)
txt_weight = tk.Entry(textvariable=weight)
btn = tk.Button(text="BMI측정", command=disp_Label)
lbl = tk.Label(text="")

txt_weight.pack()
txt_height.pack()
btn.pack()
lbl.pack()
tk.mainloop()


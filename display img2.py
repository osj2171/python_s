import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_img(path):
    newimage = PIL.Image.open(path).resize( (300,300) )
    imageData = PIL.ImageTk.PhotoImage(newimage)
    lbl_img.configure(image=imageData)
    lbl_img.image = imageData

def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        disp_img(fpath)


root = tk.Tk()
root.geometry("400x350")


btn = tk.Button(text="파일 열기", command=open_file)
lbl_img = tk.Label()

btn.pack()
lbl_img.pack()

tk.mainloop()

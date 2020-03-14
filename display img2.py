import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_img(path):
    newimage = PIL.Image.open(path).resize( (300,300) )
    imageData = PIL.ImageTk.PhotoImage(newimage)
    imageLabel.configure(image=imageData)
    imageLabel = imageData

    fpathLabel.configure(text=path)

def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        disp_img(fpath)


root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="파일 열기", command=open_file)
imageLabel.pack()
fpathLabel = tk.Label()
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
fpathLabel.pack()


tk.mainloop()

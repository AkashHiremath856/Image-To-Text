from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os

def UploadAction(event=None):
    filename = filedialog.askopenfilename(filetypes=[("", ".jpg .jpeg")])
    im = Image.open(filename)
    text = pytesseract.image_to_string(im, lang='eng')
    next
    a=simpledialog.askstring(title="File Name",prompt="Save file name as \n")+".txt"
    f = open('/home'+a, "w")
    f.write(text)
    f.close()

root = tk.Tk()
root.title('Image to Text Convertor')
root.geometry('800x400')
button = tk.Button(root, text='Select Image',
                   command=UploadAction, height=2, width=8)
button.place(x=365, y=200)
root.mainloop()

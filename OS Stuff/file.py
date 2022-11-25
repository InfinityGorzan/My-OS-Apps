from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file",
                                          filetypes= (("Text document","*.txt"),
                                          ("All files","*.*")))
    os.startfile(filepath)

def create():
    os.startfile("files/file-creater.cmd")

def delete():
    os.startfile("files/file-deleter.cmd")

def deldir():
    os.startfile("files/delete-dir.cmd")

def delmf():
    os.startfile("files/delete-files.cmd")

window = Tk()
window.title("File Manager")
window.geometry("250x170")
window.resizable(False, False)
button = Button(text="Open",command=openFile)
button.pack()

#Other options
l1 = Label(window, text="Other options:").pack()
l1

button1 = Button(text="Create File",command=create)
button1.pack()
button2 = Button(text="Delete File",command=delete)
button2.pack()
button3 = Button(text="Delete Files",command=delmf)
button3.pack()
button4 = Button(text="Delete Empty Directory",command=deldir)
button4.pack()

window.mainloop()
from tkinter import *
from tkinter import ttk

root=Tk()


Radiobutton(root).pack()
Checkbutton(root).pack()
Checkbutton(root).pack()


b=['python','php','java']
ca=ttk.Combobox(values=b).pack()
ca.set('python')


root.mainloop()
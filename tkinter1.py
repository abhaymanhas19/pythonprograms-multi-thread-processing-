from tkinter import *
import runpy

root=Tk()

def adddata():
    runpy.run_module('tkinter2')

root.geometry('400x300')

me=Menu(root,tearoff=0)
fl=Menu(me)
me.add_cascade(label="File",menu=fl,font=(' calibiri 12'))
fl.add_command(label="New")
fl.add_command(label='Open')
fl.add_command(label='Save')
fl.add_command(label='Save as')
fl.add_command(label='Close')

f2=Menu(me,tearoff=0)
me.add_cascade(label="Edit",menu=f2)
f2.add_command(label="Cut",background='black',foreground='white')
f2.add_command(label='Copy')
f2.add_command(label='Paste')
f2.add_command(label='Undo')
f2.add_command(label='Redo')
f2.add_command(label='Find')
f2.add_command(label='Replace')

f3=Menu(me,tearoff=0)
me.add_cascade(label='Shortcuts',menu=f3)
f3.add_command(label='Select all     Ctrl+A',font=('Arial 10  underline'))
f3.add_command(label='Cut            Ctrl+X')
f3.add_command(label='Paste          Ctrl+V')
f3.add_command(label='Save           Ctrl+S')
f3.add_command(label='Copy           Ctrl+C')
f3.add_command(label='Undo           Ctrl+Z')
f3.add_command(label='Redo           Ctrl+Y')

root.config(menu=me)

root.mainloop()
#! /usr/bin/env python3

''' Python script to use tkinter module '''

# import everything to keep things simple and clean
# Also importing ttk module
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()     # Main Pop-up window
root.title('First Test GUI')     # give the title of the main window
ttk.Button(root, text='Hello TkInter').grid()   # use to form button on the main (root) window with grid representation
root.mainloop()     # This keeps our main window or program open till we will not exit

#-------------- Multiple Components -------------------------
# Some of the different widgets: Button, Label, Canvas, Menu, Text, Scale, OptionMenu, Frame, CheckButton,
# LabelFrame, MenuButton, PanedWindow, Entry, ListBox, Message, RadioButton, ScrollBar, Bitmap, SpinBox, Image



root2 = Tk()
root2.title('Test2 - Frame')
frame = Frame(root2)
labelText = StringVar()
label = Label(frame, textvariable=labelText)
button = Button(frame, text='Click Me')
labelText.set('I am label')
label.pack()
button.pack()
frame.pack()
root2.mainloop()



# pack() - geometry manager
root3 = Tk()
root3.title('Test3 - pack geomerty manager')
frame = Frame(root3)
Label(frame, text='A bunch of Buttons').pack()

Button(frame, text='B1').pack(side=LEFT, fill=Y)
Button(frame, text='B2').pack(side=TOP, fill=X)
Button(frame, text='B3').pack(side=RIGHT, fill=X)
Button(frame, text='B4').pack(side=TOP, fill=X)

frame.pack()
root3.mainloop()



# grid() - geometry manager
root4 = Tk()
root4.title('Test4 - grid geometry manager')

Label(root4, text='First Name').grid(row=0, sticky=W, padx=4)
Entry(root4).grid(row=0, column=1, sticky=E, pady=4)

Label(root4, text='Last Name').grid(row=1, sticky=W, padx=4)
Entry(root4).grid(row=1, column=1, sticky=E, pady=4)

Button(root4, text='Submit').grid(row=3)
root4.mainloop()



# radio-button and check-button
root5 = Tk()
root5.title('Test5 - radio and check buttons')

Label(root5, text='Description').grid(row=0, column=0, sticky=W)
Entry(root5, width=50).grid(row=0, column=1)
Button(root5, text='Submit').grid(row=0, column=8)

Label(root5, text='Quality').grid(row=1, column=0, sticky=W)
Radiobutton(root5, text='New', value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root5, text='Good', value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root5, text='Poor', value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root5, text='Damaged', value=4).grid(row=5, column=0, sticky=W)

Label(root5, text='Benefits').grid(row=1, column=1, sticky=W)
Checkbutton(root5, text='Free Shipping').grid(row=2, column=1, sticky=W)
Checkbutton(root5, text='Bonus Gift').grid(row=3, column=1, sticky=W)

root5.mainloop()



# calling a function on clicking of a button
def get_sum(event):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    sum = num1 + num2
    sum_entry.delete(0, 'end')
    sum_entry.insert(0, sum)


root6 = Tk()
root6.title('Test6 - function calling')

num1_entry = Entry(root6)
num1_entry.pack(side=LEFT)

Label(root6, text='+').pack(side=LEFT)
num2_entry = Entry(root6)
num2_entry.pack(side=LEFT)

equal_button = Button(root6, text='=')
equal_button.bind('<Button-1>', get_sum)
equal_button.pack(side=LEFT)

sum_entry = Entry(root6)
sum_entry.pack(side=LEFT)

root6.mainloop()


# Variables
str_var = StringVar()
int_var = IntVar()
dbl_var = DoubleVar()
bool_var = BooleanVar()

str_var.set('Enter String')
int_var.set('Enter Intger')
dbl_var.set('Enter Double')
bool_var.set(True)

str_entry = Entry(root, textVariable=str_var)
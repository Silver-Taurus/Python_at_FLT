#! /usr/bin/env python3

''' Python Script for testing the sue of TkInter module '''

# Importing all the data from the tkinter module
from tkinter import *

# Initialising the Window
root = Tk()

# Labels
label1 = Label(root, text='This is our Tkinter window')      # we created a label (widget) but not added to window
label1.pack()   # puts it on your window
label2 = Label(root, text='This is our second sentence').pack()
# Normally placed widgets are placed one after the another

# Layouts
top_frame = Frame(root)
top_frame.pack()
# It creates an invisible layout, but we can put the objects inside it
bot_frame = Frame(root)
bot_frame.pack(side=BOTTOM)

# Buttons
button1 = Button(None, text='Click Me!', fg='Blue').pack(side=LEFT, fill=Y)      # In this the button does not belong to any frame
button2 = Button(top_frame, text='Hello!', fg='Red').pack(side=LEFT)     # This belongs to the top_frame
button3 = Button(top_frame, text='Click Me!', fg='Green').pack(side=LEFT)
button4 = Button(bot_frame, text='Nice!', fg='Violet').pack(side=LEFT)
button5 = Button(bot_frame, text='GoodBye!', fg='Cyan').pack(side=LEFT)
# Since button1 belongs to neither of the frame, so by default it will remain at the last of top frame
# or you can say where the top frame ends.
# By default the side is center.

# Grid Layouts

# Running the Window till the user exits
root.mainloop()


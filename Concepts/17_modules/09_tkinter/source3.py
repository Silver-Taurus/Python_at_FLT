#! /usr/bin/env python3

''' Python script for test use of tkinter '''

from tkinter import *

root = Tk()     # initialising the main window
root.geometry('800x600')    # setting up the geometry of the window ,i.e., the view on the window

c = Canvas(root, height=800, width=800)   # this creates a canvas inside the view area of the window

# Plotting a line
# l = c.create_line(5, 5, 100, 100, width=10)

# Plotting a square
# s = c.create_rectangle(0, 0, 800, 800, width=5)

# defining a genreal function for making the grid-world
pass

# Creates a grid world
p111 = c.create_polygon(0, 0, 100, 100, 200, 0, outline='white', width=2)
p112 = c.create_polygon(0, 0, 100, 100, 0, 200, outline='white', width=2)
p113 = c.create_polygon(0, 200, 100, 100, 200, 200, outline='white', width=2)
p114 = c.create_polygon(200, 200, 100, 100, 200, 0, outline='white', width=2)

p121 = c.create_polygon(200, 0, 300, 100, 400, 0, outline='white', width=2)
p122 = c.create_polygon(200, 0, 300, 100, 200, 200, outline='white', width=2)
p123 = c.create_polygon(200, 200, 300, 100, 400, 200, outline='white', width=2)
p124 = c.create_polygon(400, 200, 300, 100, 400, 0, outline='white', width=2)

p131 = c.create_polygon(400, 0, 500, 100, 600, 0, outline='white', width=2)
p132 = c.create_polygon(400, 0, 500, 100, 400, 200, outline='white', width=2)
p133 = c.create_polygon(400, 200, 500, 100, 600, 200, outline='white', width=2)
p134 = c.create_polygon(600, 200, 500, 100, 600, 0, outline='white', width=2)

s14 = c.create_rectangle(600, 0, 800, 200, fill='#00CD00', outline='white', width=4)

p211 = c.create_polygon(0, 200, 100, 300, 200, 200, outline='white', width=2)
p212 = c.create_polygon(0, 200, 100, 300, 0, 400, outline='white', width=2)
p213 = c.create_polygon(0, 400, 100, 300, 200, 400, outline='white', width=2)
p214 = c.create_polygon(200, 400, 100, 300, 200, 200, outline='white', width=2)

s22 = c.create_rectangle(200, 200, 400, 400, fill='grey')

p231 = c.create_polygon(400, 200, 500, 300, 600, 200, outline='white', width=2)
p232 = c.create_polygon(400, 200, 500, 300, 400, 400, outline='white', width=2)
p233 = c.create_polygon(400, 400, 500, 300, 600, 400, outline='white', width=2)
p234 = c.create_polygon(600, 400, 500, 300, 600, 200, outline='white', width=2)

s24 = c.create_rectangle(600, 200, 800, 400, fill='#8B0000', outline='white', width=4)

p311 = c.create_polygon(0, 400, 100, 500, 200, 400, outline='white', width=2)
p312 = c.create_polygon(0, 400, 100, 500, 0, 600, outline='white', width=2)
p313 = c.create_polygon(0, 600, 100, 500, 200, 600, outline='white', width=2)
p314 = c.create_polygon(200, 600, 100, 500, 200, 400, outline='white', width=2)

p321 = c.create_polygon(200, 400, 300, 500, 400, 400, outline='white', width=2)
p322 = c.create_polygon(200, 400, 300, 500, 200, 600, outline='white', width=2)
p323 = c.create_polygon(200, 600, 300, 500, 400, 600, outline='white', width=2)
p324 = c.create_polygon(400, 600, 300, 500, 400, 400, outline='white', width=2)

p331 = c.create_polygon(400, 400, 500, 500, 600, 400, outline='white', width=2)
p332 = c.create_polygon(400, 400, 500, 500, 400, 600, outline='white', width=2)
p333 = c.create_polygon(400, 600, 500, 500, 600, 600, outline='white', width=2)
p334 = c.create_polygon(600, 600, 500, 500, 600, 400, outline='white', width=2)

p341 = c.create_polygon(600, 400, 700, 500, 800, 400, outline='white', width=2)
p342 = c.create_polygon(600, 400, 700, 500, 600, 600, outline='white', width=2)
p343 = c.create_polygon(600, 600, 700, 500, 800, 600, outline='white', width=2)
p344 = c.create_polygon(800, 600, 700, 500, 800, 400, outline='white', width=2)

# Packing up the canvas
c.pack()

# running the mainloop
root.mainloop()

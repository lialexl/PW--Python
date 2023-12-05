from tkinter import *
from turtle import *
import math
#import numpy as np


def submit():
    B = float(B_Entry.get())
    S = float(S_Entry.get())
    w = float(w_Entry.get())
    draw(B, S, w)



def draw(B, S, w):
    #X line
    up() 
    goto(-200, 0)
    down()
    forward(400)
    #X arrow
    begin_fill()
    right(90)
    forward(3)
    left(120)
    forward(6)
    left(120)
    forward(6)
    left(120)
    forward(3)
    end_fill()
    #T text
    up()
    goto(203, 6)
    down()
    write('t')
    #Y line
    up()
    goto(-200, -200)
    down()
    left(180)
    forward(400)
    #Y arrow
    begin_fill()
    right(90)
    forward(3)
    left(120)
    forward(6)
    left(120)
    forward(6)
    left(120)
    forward(3)
    end_fill()
    #U text
    up()
    goto(-202, 210)
    down()
    write('U')
    #Sinusoidal wave
    up()
    goto(-200, 0)
    down()
    for x in range(-200, 200):
        y = 150 * math.sin((x * math.pi) / 100)  
        goto(x, y)
    #BSw text
    up()
    goto(-280, 145)
    down()
    write(f'BSw = {B*S*w}')
    #BSw dotted line
    up()
    goto(-200, 150)
    i=0
    while i <= 40:
        i+=1
        down()
        goto(i*10-200, 150)
        i+=1
        up()
        goto(i*10-200, 150)
    #-BSw text
    up()
    goto(-280, -145)
    down()
    write(f'-BSw = {-B*S*w}')
    #-BSw dotted line
    up()
    goto(-200, -150)
    i=0
    while i <= 40:
        i+=1
        down()
        goto(i*10-200, -150)
        i+=1
        up()
        goto(i*10-200, -150)




window = Tk()

B_Label = Label(text="Input B:")
B_Label.grid(row=0, column=0)
B_Entry = Entry(text="B_Entry")
B_Entry.grid(row=0, column=1)

S_Label = Label(text="Input S:")
S_Label.grid(row=1, column=0)
S_Entry = Entry(text="S_Entry")
S_Entry.grid(row=1, column=1)

w_Label = Label(text="Input w:")
w_Label.grid(row=2, column=0)
w_Entry = Entry(text="w_entry")
w_Entry.grid(row=2, column=1)

submit_Button = Button(text="Submit", command=submit)
submit_Button.grid(row=3, column=0, columnspan=2)




window.mainloop()
from turtle import *
shape("turtle")
speed(-1)
color('green')


for i in range (10): 
    begin_fill()
    for i in range (4):
        forward(100)
        left(90)
    end_fill()

    left(7)


mainloop()
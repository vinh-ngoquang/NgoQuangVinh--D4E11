from turtle import *


colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color(colors[0])
mau = 0
for edge in range(3,8):
    for i in range (edge):
        forward(100)
        left(360/edge)
        # print(edge)
    mau = mau + 1
    print(mau)
    color(colors[mau])
    # if edge == 4:
    #     color(colors[1])
    # elif edge == 5:
    #     color(colors[2])
    # elif edge == 6:
    #     color(colors[3])
    # else:
    #     color(colors[4]) 

mainloop()
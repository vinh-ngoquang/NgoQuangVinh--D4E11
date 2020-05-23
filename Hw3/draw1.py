from turtle import *


colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# color(colors[0])
mau = 0
for edge in range(3,8):
    color(colors[mau])
    mau = mau + 1
    for i in range (edge):
        forward(100)
        left(360/edge)
    print(mau)
    
mainloop()
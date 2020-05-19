from turtle import *
# speed(-1)
color('red')
forward(100)
left(120)
color('blue')
for i in range(2):
    forward(100)
    left(120)

#1
for i in range(4):
    color('red')
    forward(100)
    left(90)

color('red')
forward(100)
left(360/5)
for i in range (4):
    color('blue')
    forward(100)
    left(360/5)

for i in range(6):
    color('red')
    forward(100)
    left(360/6)

#2
from turtle import *

for edge in range(3, 6):
  for i in range (edge):
        forward(100)
        left(360/edge)
        if edge == 3 or edge == 5:
            color('blue')
        else:
            color('red')

color('red')
forward(100)

for j in range(5):
    left(360/6)
    forward(100)
    color('red')

left(60)    
mainloop()







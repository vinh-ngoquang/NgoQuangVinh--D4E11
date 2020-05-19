from turtle import *
# n= int(input('nhap n: '))
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

# from turtle import *
# speed(-1)

# for edge in range (3, 7):
#     for i in range (edge):
#         forward(100)
#         left(360/edge)
#         if edge == 3 or edge == 5:
#             color('blue')
#         else:
#             color('red')

# mainloop()
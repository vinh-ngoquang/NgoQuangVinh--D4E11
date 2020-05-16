from turtle import *
n= int(input("number"))
print(n)
shape("turtle")

for i in range (n):
    forward(100)
    left(360/n)

mainloop()
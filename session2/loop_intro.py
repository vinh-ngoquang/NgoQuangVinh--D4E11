
# # from turtle import *
# # n= int(input('nhap n: '))
# # for i in range (n):
# #     forward(100)
# #     left(360/n)
    

# # mainloop()
from getpass import getpass

count = 0
running = True
while running:
    if count >7:
        print('Het lan thu')
        break
    username= input('username: ')
    password= getpass('password: ')
    if username == 'mindx' and password == 'password':
        print('Success')
        break
    else:
        count += 1

    
        


    
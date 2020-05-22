a= int(input('nhap a: '))
b= int(input('nhap b: '))
c= int(input('nhap c: '))

delta= b**2 - 4*a*c
x1= ((-b) + (delta**(1/2))) / 2*a
x2= ((-b) - (delta**(1/2))) / 2*a
x= -b/2*a

if delta > 0:
    print(x1, x2) 
elif delta == 0:
    print(x)
else:
    print('Vo nghiem')
break

   
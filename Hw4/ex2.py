a = int(input('Enter your balance: '))
#chuyen thanh format $
print('${:,.0f}'.format(a).lstrip('0'))   #lstrip de xoa 0 dau dong.

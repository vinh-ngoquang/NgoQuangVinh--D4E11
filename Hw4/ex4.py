z = [1, 6, 7, 2, 8, 1, 9, 3, 5, 6, 7, 9, 2, 8, 8, 8]
number = int(input('Enter a number: '))
for i in range(len(z)):
    if number == z[i]:
        count = z.count(z[i])
print(number, 'appears',count,'times in my list')                 #code voi count.
    # print(z[i]) 
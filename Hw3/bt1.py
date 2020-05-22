sizeofsheep = [5, 7, 300, 90, 24, 50, 75]
# sizeofsheep1 = int([5, 7, 300, 90, 24, 50, 75])
for j in range(1,4):
    print('Month',j, "Hello, my name is Vinh and these are my ship sizes\n ",sizeofsheep)
    maxsize = max(sizeofsheep)
    print('Now my biggest sheep has size', maxsize, 'lets shear it')    #2.2
    sizeofsheep[sizeofsheep.index(max(sizeofsheep))] = 8
    print('After sharing, here is my flock\n' , sizeofsheep)     #2.3
    for i in range (len(sizeofsheep)):
        sizeofsheep[i] = sizeofsheep[i] + 50
    print('One month has passed, now here is my flock \n', sizeofsheep)

total = sum(sizeofsheep)
print('My flock has size in total: ', total)
print('I would get total * 2 $ = ', total*2,'$' )
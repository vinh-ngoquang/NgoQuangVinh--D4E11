from random import *
game = ['dam', 'la', 'keo']
shuffle(game)
select = input('Enter your select: ')
print('Computer choose: ', game[0])
if select == game[0]:
    print('draw')
else:
    if select == 'dam':
        if game[0] == 'keo':
            print('you win')
        else:
            print('you lose')

    if select == 'keo':
        if game[0] == 'dam':
            print('you lose')
        else:
            print('you win')

    if select == 'la':
        if game[0] == 'dam':
            print('you win')
        else:
            print('you lose')      

                 
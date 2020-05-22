from random import *
from getpass import getpass
running = True
while running:
    quizz = getpass('enter your quizz: ').lower()
    list_quizz = list(quizz)  #chuyen tu string sang list
    shuffle(list_quizz)
    for i in range(len(list_quizz)):
        print(list_quizz[i].upper(), end=' ')

    dapan = input('enter your guess: ').lower() 
    if quizz == dapan:
        print('bingo')
    else:
        print(':((')
break
        

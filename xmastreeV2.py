# sense gpt ni merdes
# vull fer un arbre de nadal
# el que vol dir això és una figura en forma de fletxa amb una base quadrada i una estrella a dalt, tot fet amb asteriscs, es printa de dalt a baix

import math

altura = int(input("Quina altura vols que tingui l'arbre? "))
amplada = altura

done = True
i = 0

while done:
    if(i == 0):
        asteriscs = 1
        print("")
        for j in range(amplada):
            if j < amplada - asteriscs:
                print(' ', end='')
        else:
            print('*', end='')
        i += 1
    elif i != altura:
        asteriscs = i
        print("")
        for j in range(amplada):
            if j < amplada - asteriscs:
                print(' ', end='')
            else:
                print('*', end='')
        for j in range(amplada):
            if j < asteriscs and j != 0:
                print('*', end='')
        i += 1
    else:
        print("")
        for j in range(amplada):
            if j < amplada - 1:
                print(' ', end='')
            else:
                print('*', end='')  
        print("")
        for j in range(amplada):
            if j < amplada - 1:
                print(' ', end='')
            else:
                print('*', end='')  
        done = False
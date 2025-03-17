# sense gpt ni merdes
# vull fer un arbre de nadal
# el que vol dir això és una figura en forma de fletxa amb una base quadrada i una estrella a dalt, tot fet amb asteriscs, es printa de dalt a baix

# s'han de fer tantes linees de print com altura tingui l'arbre
# a cada linia s'han de baixar tants com el ratio de altura-amplada
# i.e. si altura = 3 amplada = 6, cada linia augmenta amplada/altura = 2 asteriscs
# primera fila 1 asterisc, segona fila ceil(1 + amplada/altura*i) asteriscs, 
#1   *
#3  **
#5 ***
#    *
# i.e. si altura = 5 amplada = 2, cada linia augmenta amplada/altura = 0.4 asterisc, provarem a un ceil o amb floor
#   *
#  ***
#  ***
#  ***
#  ***
#   *

import math

altura = int(input("Quina altura vols que tingui l'arbre? "))
amplada = altura

for i in range(altura):
    # el punt central de l'imparell es ceil(amplada/2)
    print("")
    if(i == 0):
        asteriscs = 1
    else:
        asteriscs = math.ceil(i)
    for j in range(amplada):
        if j < amplada - asteriscs:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(amplada):
        if j < asteriscs and j != 0:
            print('*', end='')

print("")
for j in range(amplada):
    if j < amplada - 1:
        print(' ', end='')
    else:
        print('*', end='')
for j in range(amplada):
    if j < 1 and j != 0:
        print('*', end='')
print("")
for j in range(amplada):
    if j < amplada - 1:
        print(' ', end='')
    else:
        print('*', end='')
for j in range(amplada):
    if j < 1 and j != 0:
        print('*', end='')
print("\nja està l'arbre de nadal")


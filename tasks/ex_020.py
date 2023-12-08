# Class link: https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=29

from random import randint, shuffle

names = input('Digite o nome dos 4 alunos, separados por um espaço: ')
namesList = names.split()
shuffle(namesList)

# print(f'list: {len(namesList)}')
print('A ordem de apresentação será: ')
for name in namesList:
  print(name)

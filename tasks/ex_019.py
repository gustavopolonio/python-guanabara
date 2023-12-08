# Class link: https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=28

from random import randint, choice

names = input('Digite o nome dos 4 alunos, separados por um espaço: ')
namesList = names.split()

idStudent = randint(0, 3)
# print(idStudent)

print(f'O estudante escolhido foi: {namesList[idStudent]}')
print(f'O estudante escolhido foi: {choice(namesList)}')

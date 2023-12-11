# Class link: https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=39

from random import randrange

print('Vou pensar em um número entre 0 e 5! ')
print('Pensando...')

num = randrange(6)

print('Pensei!')
userNum = int(input('Tenta advinhar: '))

if num == userNum:
  print(f'Você acertou! Eu escolhi o num {num}')
else:
  print(f'Você errou! Eu escolhi o num {num}')
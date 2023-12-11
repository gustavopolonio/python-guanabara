# Class link: https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=32

name = input('Qual seu nome? ')

print(f'Com letras maiúsculas: {name.upper()}')
print(f'Com letras minúsculas: {name.lower()}')

nameSplitted = name.split()

nameCompleted = ''.join(nameSplitted)
print(f'Letras ao todo sem espaço: {len(nameCompleted)}')

print(f'O primeiro nome ({nameSplitted[0]}) tem {len(nameSplitted[0])} letras')
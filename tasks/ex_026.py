# Class link: https://www.youtube.com/watch?v=23UOVEetNPY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=36

phrase = input('Digite o nome da pessoa: ').strip().upper()

count = phrase.count('A')
first = phrase.find('A')
last = phrase.rfind('A')

print(f'A letra A aparece {count} vezes')
print(f'A letra A aparece na primeira vez na posição: {first + 1}')
print(f'A letra A aparece na última vez na posição: {last + 1}')
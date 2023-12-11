# Class link: https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=44

n1 = int(input('Digite o 1o num '))
n2 = int(input('Digite o 2o num '))
n3 = int(input('Digite o 3o num '))

if n1 > n2 and n1 > n3:
  if n2 > n3:
    print(f'Maior: {n1}, menor: {n3}')
  else:
    print(f'Maior: {n1}, menor: {n2}')
elif n2 > n1 and n2 > n3:
  if n1 > n3:
    print(f'Maior: {n2}, menor: {n3}')
  else:
    print(f'Maior: {n2}, menor: {n1}')
else:
  if n1 > n2:
    print(f'Maior: {n3}, menor: {n2}')
  else:
    print(f'Maior: {n3}, menor: {n1}')
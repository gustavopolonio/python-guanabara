# Class link: https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38

tempo = int(input('Quantos anos seu carro tem? '))

if tempo <= 3:
  print('Carro novo')
else:
  print('Carro velho')

print('Carro novo' if tempo <=3 else 'Carro velho')
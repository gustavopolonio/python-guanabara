# Class link: https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=42

dist = float(input('Qual é a distância da viagem em km? '))

if (dist <= 200):
  preco = dist * 0.5
else:
  preco = dist * 0.45

print(f'O preço total da viagem será R$ {preco :.2f}')
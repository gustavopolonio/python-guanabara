# Class link: https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=40

vel = float(input('Qual a velocidade do carro? '))

if (vel > 80):
  print('* VOCÊ FOI MULTADO *')
  valor = (vel - 80) * 7
  print(f'Você deve pagar R${valor}')
print('Tenha um bom dia!')
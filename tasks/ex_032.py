# Class link: https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=43

ano = int(input('Digite um ano para ver se ele é bissexto: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
  print('Bissexto')
else:
  print('Não')
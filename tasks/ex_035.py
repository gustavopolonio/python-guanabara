# Class link: https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=46

l1 = float(input('Digite o comprimento da reta 1 do triângulo: '))
l2 = float(input('Digite o comprimento da reta 2 do triângulo: '))
l3 = float(input('Digite o comprimento da reta 3 do triângulo: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
  print(True)
else:
  print(False)
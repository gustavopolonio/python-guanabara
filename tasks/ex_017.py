# Class link: https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=26

from math import sqrt

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h = sqrt((co ** 2) + (ca ** 2))

print(f'A hipotenusa é: {h:.2f}')
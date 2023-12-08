# Class link: https://www.youtube.com/watch?v=tHYxjJxtJko&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=11


var = input('Digite algo: ')
print(f'Algo é do tipo {type(var)}, Só tem espaços? {var.isspace()}, É um número? {var.isdecimal()}, É alfabético? {var.isalpha()}, É alfanumérico? {var.isalnum()}, Está em maiúsculas? {var.isupper()}, Está em minúsculas? {var.islower()}, Está capitalizada? {var.istitle()}')
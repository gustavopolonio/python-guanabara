# Class link: https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=31

frase = 'Curso em video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])   # Step (2)
print(frase[:5])   # Começa do início - posição 0
print(frase[15:])   # Quero do 15 até o final
print(frase[9::3])   # Começa no 9 e vai até o final, com step 3


# Analisar uma string
print(len(frase))   # Comprimento frase
print(frase.count('o'))   # Contar quantas vezes a letra 'o' aparece
print(frase.find('deo'))
print('Curso' in frase)


# Transformar uma string
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())


# Dividir uma string
print(frase.split())

28:20 / 46:46


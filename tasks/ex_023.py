# Class link: https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=33

# Resolvendo com strings
# Laços de repetição


# Matematicamente
num = int(input('Digite um número entre 0 e 9999: '))

unidade = num % 10
resto = num // 10

dezena = resto % 10
resto = resto // 10

centena = resto % 10
resto = resto // 10

milhar = resto % 10

print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')
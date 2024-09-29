###########################################################################

# Atividade 01

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# Atividade 02

soma = 0
numero = 1

while numero <= 100:
    soma += numero
    numero += 1
print(soma)

# Atividade 03

numero = int(input('Digite um numero: '))
contador = 0

while contador < 10:
    contador += 1
    resultado = contador * numero
    print(f'{numero} x {contador} = {resultado}')

# Atividade 04 

contador = 11
limite = 1

while limite < contador:
    contador -= 1
    print(contador)
print("Feliz ano novo!")

# Atividade 05

limite = int(input('Digite um numero: '))
contador = 1

while contador <= limite:
    print(contador)
    contador += 2

# Atividade 06

soma = 0
numero = None

while True:
    numero = int(input('Digite números a ser somados: '))
    if numero >= 0:
        soma += numero
    elif numero < 0:
        print(f'A soma de todos os número digitados é {soma}.')
        break
    else:
        print('Você digitou o numero zero')
    

# Atividade 07

numero = int(input('Digite um numero: '))
contador = 0

while contador < 10:
    contador += 1
    resultado = contador * numero
    if resultado % 3 == 0:
        print(f'{numero} x {contador} = {resultado}')

# Atividade 08

notas = None
quantidade_notas = 0
soma = 0

while True:
    notas = int(input('Digite suas notas. (para sair digite -1): '))
    if notas >= 0: 
        soma += notas
        print(notas)
        

# Atividade 09

contador = 1
soma = 0

while True:
    soma += contador
    print(f'Número {soma}')
    if soma == 10:
        break

# Atividade 10

soma = 0
contador = 1

while soma < 50:
    soma += contador
    contador += 1

print(f"A soma dos números consecutivos é {soma}.")

# Atividade 11

numero = None

while True:
    numero = int(input('Digite um número de 1 a 10: '))
    if numero <= 0:
        print(f'Você digitou {numero}, por favor digite um número entre 1 a 10.')
    elif numero > 10:
        print(f'Você digitou {numero}, por favor digite um número entre 1 a 10.')
    else:
        print(f'Você digitou {numero}, é um número valido.')
        break

# Atividade 12

senha = ''

while senha != '1234':
    senha = input('Digite a senha: ')
    if senha == '1234':
        print('Acesso concedido!')
    else:
        print('Senha incorreta, tente novamente.')
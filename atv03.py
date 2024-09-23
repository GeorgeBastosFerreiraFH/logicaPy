senha = ''
while senha != '12345':
    senha = input('Digite a senha: ')
    if senha == '12345':
        print('Acesso concedido!')
    else:
        print('Senha incorreta, tente novamente.')

opcao = ''

while opcao != '3':
    print('Menu:')
    print('1. Opção 1')
    print('2. Opção 2')
    print('3. Opção para sair do programa')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('Você escolheu a opção 1.')
    elif opcao == '2':
        print('Você escolheu a opção 2.')
    elif opcao == '3':
        print('Encerrando o programa')
    else:
        print('Opção inválida, tente novamente!')

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

# Atividade 05 - não consegui fazer a parte de só exibir os números impares!

limite = int(input('Digite um numero: '))
contador = 0

while contador < limite:
    contador += 1
    resultado = 
    print(resultado)

# Atividade 07 - não consegui fazer a parte de só mostrar os números multiplos de 3

numero = int(input('Digite um numero: '))
contador = 0

while contador < 10:
    contador += 1
    resultado = contador * numero
    if 
        print(f'{numero} x {contador} = {resultado}')

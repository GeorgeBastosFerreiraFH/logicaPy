# Desafio 1

contador = 1
soma = 0
resultado = 0

while soma < 100:
    soma += contador
    if soma % 2 == 0:
        resultado += soma

print(f'O resultado da soma dos números pares de 1 a 100 é {resultado}')


# Desafio 2

contador = 0
soma = 0

while contador < 50:
    contador += 1
    if contador % 2 == 1:
        # print(contador)
        soma += contador

print(f"A soma dos números ímpares de 1 a 50 é {soma}")


# Desafio 3

num1 = 1
num2 = 1
contador = 0
tentativas = 20

while contador < tentativas:
    print(num1)
    proximo = num1 + num2
    num1 = num2
    num2 = proximo
    contador += 1


# Desafio 4

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é {fatorial}")


# Desafio 5

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

contador = 0

while num1 != num2:
    contador += 1
    if contador <= num2 and contador % 2 == 0:
        print(contador)
    elif contador >= num2:
        break


# Desafio 6

contador = int(input('Digite um número: '))


while contador >= 0:    
    if contador % 2 == 0:
        print('Número par')
    elif contador % 2 == 1:
        print(contador)
    contador -= 1

# Desafio 7 - esse não deu

numero = int(input('Digite um número: '))

while True:
    if numero in 
    
# Desafio 8 

numero = int(input('Digite um número: '))

while numero != 1:
    print(numero)
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = 3 * numero + 1
resultado = numero
print(resultado)
contador = 0
soma = 0

for nota in range(1,5):
    contador += 1
    nota = float(input(f'Digite a {nota}º: '))
    soma += nota

media = soma / 4

if media >= 6:
    print(f'Você passou de ano, sua média é {media}')
else:
    print('Você foi reprovado')

# # --------------------------------------------------

produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))

calculo = (desconto / 100) * produto
produtoComDesconto = produto - calculo

print(f'O produto com desconto ficou por {produtoComDesconto}')

# # --------------------------------------------------

segundos = int(input('Digite a quantidade de segundos para conversão em horas minutos e segundo: '))

minutos = segundos // 60
horas = int(segundos // 3600)

print((f'A quantidade de minutos: {minutos}'))
print((f'A quantidade de horas: {horas}'))
print(f'A quantidade de segundos: {segundos}')

# # --------------------------------------------------

temperatura = float(input('Digite uma temperatura em Celsius para converter em Fahrenheit: '))

tempConvertida = temperatura * 1.8 + 32

print(f'A temperatura em Fahrenheit fica {tempConvertida}')

# # --------------------------------------------------

idade = int(input('Digite sua idade: '))
nome = input('Digite seu nome: ')

if idade >= 18:
    print(f'{nome} você é um adulto')
elif idade >= 12:
    print(f'{nome} você é um adolescente')
elif idade < 12:
    print(f'{nome} você é uma criança')

nota = float(input('Digite sua nota: '))

if nota < 20:
    print(f'{nome} você tirou um F')
elif nota > 20 and nota <= 40:
    print(f'{nome} você tirou um D')
elif nota > 40 and nota <= 60:
    print(f'{nome} você tirou um C')
elif nota > 60 and nota <= 80:
    print(f'{nome} você tirou um B')
elif nota > 80 and nota <= 100:
    print(f'{nome} você tirou um A')

# # --------------------------------------------------

dia = int(input('Digite o dia de nascimento no formato DD: '))
mes = int(input ('Digite o mes de nascimento no formato MM: '))

signo = dia + '/' + ano

if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
    print('Seu signo é áries')
elif dia >= 21 and mes == 4 or dia <= 20 and mes == 5:
    print('Seu signo é touro')
elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
    print('Seu signo é Gêmeos')
elif dia >= 21 and mes == 6 or dia <= 21 and mes == 7:
    print('Seu signo é Câncer')
elif dia >= 22 and mes == 7 or dia <= 22 and mes == 8:
    print('Seu signo é Leão')
elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
    print('Seu signo é Virgem')
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
    print('Seu signo é Libra')

# # # # --------------------------------------------------

contador1 = 10

while contador1 > 0:
    print(contador1)
    contador1 -= 1
    
print('Feliz Ano Novo!!!')

# # --------------------------------------------------

contador2 = 10

for i in range (1, 10):
   contador2 -= 1
   print(contador2)

print('Feliz Ano Novo!!!')


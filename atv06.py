# # --------------------------------------------------

# # Conversão de Unidades:

metros = int(input('Digite um valor em metros: '))

convMetros = metros * 100

print(f'O valor em centímetros é {convMetros}')

# # --------------------------------------------------

# # Cálculo de Área:

altura = float(input('Digite a altura de um retangulo para calcular sua área: '))
largura = float(input('Digite a largura de um retangulo para calcular sua área: '))

areaRetangulo = largura * altura

print(f'A área do retangulo é {areaRetangulo}')

# # --------------------------------------------------

# # Cálculo de IMC:

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

print(f'Seu IMC é {imc:.2f}')

# # --------------------------------------------------

# # Cálculo de Juros Simples:

capital = float(input('Digite o valor do capital inicial R$ '))
taxaJuros = float(input('Digite a taxa de juros mensal (em %): '))
tempoAplicacao = int(input('Digite o tempo de aplicação em meses: '))

juroSimples = capital * (taxaJuros / 100) * tempoAplicacao

print(f'O valor dos juros simples é R$ {juroSimples:.2f}')

# # --------------------------------------------------

# # Algoritmo de Cálculo de Media de Notas:

soma = 0

for contador in range(1,5):
    nota = float(input(f'Digite a {contador}º nota: '))
    soma += nota

media = soma / contador

if media >= 6:
    print(f'Você passou de ano, sua média foi {media}.')
else:
    print(f'Você foi reprovado, sua média foi {media}.')

# # --------------------------------------------------

# # Algoritmo de Cálculo de Desconto:

produto = float(input('Digite o valor do produto: '))
valorDesconto = float(input('Digite o valor do desconto: '))

desconto = (valorDesconto / 100) * produto
produtoComDesconto = produto - desconto

print(f'O produto com desconto ficou por {produtoComDesconto}')

# # --------------------------------------------------

# # Algoritmo de Conversão de Tempo:

segundos = int(input('Digite a quantidade de segundos para conversão em horas minutos e segundo: '))

minutos = segundos // 60
horas = int(segundos // 3600)

print((f'A quantidade de minutos: {minutos}'))
print((f'A quantidade de horas: {horas}'))
print(f'A quantidade de segundos: {segundos}')

# # --------------------------------------------------

# #  Algoritmo de Conversão de Temperatura:

temperatura = float(input('Digite uma temperatura em Celsius para converter em Fahrenheit: '))

tempConvertida = temperatura * 1.8 + 32

print(f'A temperatura em Fahrenheit fica {tempConvertida}')

# # --------------------------------------------------

# # Categoria de Idade:

idade = int(input('Digite sua idade: '))
nome = input('Digite seu nome: ')

if idade >= 18:
    print(f'{nome} você é um adulto')
elif idade >= 12:
    print(f'{nome} você é um adolescente')
elif idade < 12:
    print(f'{nome} você é uma criança')

# # Classificação de Notas:

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

# # Verificar Signo:

dia = int(input('Digite o dia de nascimento no formato DD: '))
mes = int(input ('Digite o mes de nascimento no formato MM: '))

if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
    print(f'Seu signo é Áries')
elif dia >= 21 and mes == 4 or dia <= 20 and mes == 5:
    print(f'Seu signo é Touro')
elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
    print(f'Seu signo é Gêmeos')
elif dia >= 21 and mes == 6 or dia <= 21 and mes == 7:
    print(f'Seu signo é Câncer')
elif dia >= 22 and mes == 7 or dia <= 22 and mes == 8:
    print(f'Seu signo é Leão')
elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
    print(f'Seu signo é Virgem')
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
    print(f'Seu signo é Libra')
elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
    print(f'Seu signo é Escorpião')
elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
    print(f'Seu signo é Sagitário')
elif dia >= 22 and mes == 12 or dia <= 19 and mes == 1:
    print(f'Seu signo é Capricórnio')
elif dia >= 20 and mes == 1 or dia <= 18 and mes == 2:
    print(f'Seu signo é Aquário')
elif dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
    print(f'Seu signo é Peixes')

# # --------------------------------------------------

# # Sistema de Login:

usuario = 'admin'
senha = 1234

for i in range(1, 4):
    usuarioDigitado = input('Digite seu usuário: ')
    senhaDigitada = int(input(f'Digite sua senha (tentativa {i}/3): '))

    if usuarioDigitado == usuario and senhaDigitada == senha:
        print('Login efetuado com sucesso')
        break
    elif i == 3:
        print('Usuário bloqueado')
    else:   
        print('Usuário ou senha inválidos')

# # --------------------------------------------------

# # Contagem Regressiva com While:

contador1 = 0

while contador1 <= 10:
    print(10 - contador1)
    contador1 += 1
    
print('Feliz Ano Novo!!!')

# # --------------------------------------------------

# # Contagem Regressiva com For::

contador2 = 0

for i in range (11):
   print(10 - i)

print('Feliz Ano Novo!!!')

# # --------------------------------------------------

# # Soma de Números Pares:

contador = 0
soma = 0

while contador <= 100:
    if contador % 2 == 0:
        soma += contador
    contador += 1
print(f'A soma de todos números pares de 1 a 100: {soma}')

# # --------------------------------------------------

# # Tabuada de um Número:

numero = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
    
# # --------------------------------------------------

# # Verificação de Palíndromo:

palavra = input('Digite uma palavra: ').lower()

while True:
    if palavra == palavra[::-1]:
        print('A palavra é um palíndromo')
        break
    else:
        print('A palavra não é um palíndromo')
        break

# # --------------------------------------------------

# # Sistema de Login com Tentativas Limitadas:

usuario = 'admin'
senha = 1234

numTentativas = 3
contador = 0

while contador < numTentativas:
    usuarioDigitado = input("Digite o usuário: ")
    senhaDigitada = int(input(f"Digite a senha (tentativa {contador + 1}/{numTentativas}): "))
    
    if usuarioDigitado == usuario and senhaDigitada == senha:
        print("Acesso permitido")
        break
    else:
        contador += 1
        tentativasRestantes = numTentativas - contador
        if tentativasRestantes > 0:
            print(f"Acesso negado, você tem mais {tentativasRestantes} tentativa(s)")
        else:
            print('Acesso bloqueado')

# # --------------------------------------------------

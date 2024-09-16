# saudacao  = 'Hello world'
# print(saudacao)

# Atividade Prática

# nome = input('Digite seu nome: ')
# idade = input('Digite sua idade: ')
# altura = input('Digite sua altura: ')

# print(f'Seu nome é {nome} você tem {idade} anos e {altura} metros!')



# Comparações de idade: 

idade1 = input('Digite a primeira idade: ')
idade2 = input('Digite a segunda idade: ')

if idade1 > idade2:
    print(f'A idade {idade1} é maior que a {idade2}')

elif idade1 < idade2:
    print(f'A idade {idade1} é menor que a {idade2}')

else:
    print(f'A idade {idade1} é igual a {idade2}')



# Verificar igualdade de Strings: 

palavra1 = str(input('Digita aqui a primeira palavra: '))
palavra2 = str(input('Digite aqui a segunda palavra: '))

resultado = (palavra1 == palavra2)

print(resultado)



# Verificação de Maioridade e Habilitação:

idade = int(input('Digite sua idade: '))
habilitacao = str(input('Você possui habilitação?'))

if idade < 18:
    print('Você não esta apto')

elif idade >= 18 and habilitacao == 'sim':
    print('Vocé é habilitado!')

else:
    print('Vocé não é habilitado')



# Verificação de Notas Aprovadas:

nota1 = int(input('Digite sua nota em historia: '))
nota2 = int(input('Digite sua nota em geografia: '))

if nota1 >= 6 and nota2 >= 6:
    print('Parabéns, suas notas estão dentro da média')
elif nota1 < 6 and nota2 >= 6:
    print(f'A sua nota {nota1} está abaixo da média e sua nota {nota2} está dentro da média!')
elif nota1 >= 6 and nota2 < 6:
    print(f'A sua nota {nota1} está dentro da média e sua nota {nota2} esta abaixo da média!')
else:
    print(f"Você está abaixo da média!")



# Desconto em Preço:

precoProduto = int(input('Digite o preço de um produto: '))

precoProduto -= (precoProduto * 0.05)

print(precoProduto)



# Dobro do valor: 

valor = int(input('Digite um número que será dobrado: '))
valor *= 2

print(valor)

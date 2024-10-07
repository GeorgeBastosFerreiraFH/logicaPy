# Atividade 11 - Verificar Múltiplos de 5 e Parar:

for numero in range(1, 30 + 1):
  if numero % 5 == 0:
    print(f'O número {numero} é múltiplo de 5.')

# Atividade 12 - Soma de Números com Desconto:

total = 0
contador = 0

for preco in range(1, 6):
  contador += 1
  preco = int(input(f'Digite o preço do produto {contador}: '))
  total += preco
  desconto = total * 0.1
  
if total >= 100:
  produtoComDesconto = total - desconto
    
  print(f'O valor total com desconto é de R$ {produtoComDesconto}: ')

else:
  print(f'O valor total é de R$ {total}: ')


  
    







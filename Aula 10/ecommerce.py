print('--- Block Ecommerce ---')
name = input('Digite seu nome >>')
cpf = input('Digite seu CPF >>')
welcome = input(f'Seja bem vindo ao Block {name }')
selection = int(input(f'{1}. Camisetas\n{2}. Calças\n{3}. Calçados\n'))

def selecao(): #colocar input, forma de pagamento, id etc.
  if selection == 1:
    print('----- Camisetas -----')
    print('1 - Camisa Polo Branca')
    print('2 - Camisa Polo Preta')
    print('3 - Camisa Polo Azul')
  elif selection == 2:
    print('----- Calças -----')
    print('1 - Calça Cargo')
    print('2 - Calça Jeans')
    print('3 - Calça rasgada')
  elif selection == 3:
    print('----- Calçados -----')
    print('1 - ')
    print('2 - ')
    print('3 - ')
selecao()


# DESENVOLVEDOR DE BACK-END, E PRECISA DESENVOLVER AS 
# ESTRUTURAS BÁSICAS DO FUNCIONAMENTO DE UM E-COMMERCE
# CRIAR UM SISTEMA DE E-COMMERCE,
# O USUÁRIO PRCISA VER QUAIS PRODUTOS EXISTEM
# ESCOLHER O PRODUTO 
# EXCOLHER A FORMA DE PAGAMENTO  
# MENSAGEM DE DESPEDIDA

# NOME DO USÁRIO
# ID CODIGO
# CPF DO USUÁRIO
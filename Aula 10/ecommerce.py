print('--- Block Ecommerce ---')
name = input('Digite seu nome >>')
cpf = input('Digite seu CPF >>')
welcome = input(f'Seja bem vindo ao Block {name }')
selection = int(input(f'{1}. Camisetas\n{2}. Cal�as\n{3}. Cal�ados\n'))

def selecao(): #colocar input, forma de pagamento, id etc.
  if selection == 1:
    print('----- Camisetas -----')
    print('1 - Camisa Polo Branca')
    print('2 - Camisa Polo Preta')
    print('3 - Camisa Polo Azul')
  elif selection == 2:
    print('----- Cal�as -----')
    print('1 - Cal�a Cargo')
    print('2 - Cal�a Jeans')
    print('3 - Cal�a rasgada')
  elif selection == 3:
    print('----- Cal�ados -----')
    print('1 - ')
    print('2 - ')
    print('3 - ')
selecao()


# DESENVOLVEDOR DE BACK-END, E PRECISA DESENVOLVER AS 
# ESTRUTURAS B�SICAS DO FUNCIONAMENTO DE UM E-COMMERCE
# CRIAR UM SISTEMA DE E-COMMERCE,
# O USU�RIO PRCISA VER QUAIS PRODUTOS EXISTEM
# ESCOLHER O PRODUTO 
# EXCOLHER A FORMA DE PAGAMENTO  
# MENSAGEM DE DESPEDIDA

# NOME DO US�RIO
# ID CODIGO
# CPF DO USU�RIO
def saque(saldo, valor_saque):
        result =  saldo -  valor_saque 
        print(f'SALDO R${result}')
 
def deposito(saldo, valor_deposito): 
        result  =  saldo  +  valor_deposito
        print(f'SALDO R$ {result}')

def visualizar(saldo): 
    print(f' Seu saldo é R$ {saldo}')


def parar(escolha):
    if escolha != '1' or '2' or '3':
       print('Escolha incorreta') 

def banco():
    saldo_randomico =  random.randint(100,1000)
    print('------ BANCO ------')
    print('Digite -> 1 para saldo| 2 para deposito | 3 para saque ') 
    escolha_operacao =   input('Digite sua escolha')
    if escolha_operacao ==  '1':
       visualizar(saldo_randomico) 
    elif escolha_operacao == '2': 
       print(f'Seu saldo  -  R${saldo_randomico},00') 
       dep =  float(input('Digite o valor do deposito')) 
       deposito(saldo_randomico, dep)    
    elif escolha_operacao == '3':
       print(f'Seu saldo  -  {saldo_randomico}') 
       saq =  float(input('Digite o valor do saque')) 
       saque(saldo_randomico,saq) 
    else: 
       parar(escolha_operacao)
       banco()


while True:
      banco()        


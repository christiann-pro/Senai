import random

'''n = [3,2,1]
for c in n:
      randomico  = random.randint(1,20)
      meu_numero  =  int(input('Digite seu número>>'))
      c = c - 1
      if randomico  == meu_numero:
         
         print(f'Você ecertou o número é: {randomico}')
         break
      elif randomico != meu_numero and randomico > 0:
           print(f'Você errou, o número é: {randomico}, você tem apenas {c} chances') 
           if c == 0:
              print(f'Você esgotou as possibilidades, total de chances >> {c}')
              break'''


'''
Pensar sobre o sistema: 
1 - criar numero aleatorio
2 - digitar nome dos jogadores
3 - comparar qual dos jogadores escolheu o nnumero certo
4 - mostra quem ganhou o jogo
5 - 3 chances

dividir em pedaços, criu resolução 
'''

print('Sejam bem vindos ao jogo aleatório:')
print('....................................')
print('Digitem seu usuarios e escolha um número:')
user1 =  input('User 1 >>')
user2 =  input('User 2 >>')
print(f'Sejam bem vindos(a) {user1} e {user2}')
a = int(input(f'{user1} Digite seu número>>'))
b = int(input(f'{user2} Digite seu número>>'))
print('Você criaram uma aleatoridade de ',  a, 'e', b -1) 
chances = [3,2,1]
for i in chances:
   rand =  random.randint(a,b)
   escolha_user1 =int(input(f'Escolha um número {user1}:'))
   escolha_user2 =int(input(f'Escolha um número {user2}:'))

   i -= 1
   if escolha_user1 == escolha_user2 == rand:
      print('Empataram!')
      break
   elif escolha_user1 == rand and escolha_user1 != escolha_user2:
        print('O jogador 1 ganhou jogo')
        break
   elif escolha_user2 == rand and escolha_user1 != rand:
        print('O jogador 2 ganhou jogo')
        break
   elif rand != escolha_user1 and rand != escolha_user2:
        print(f'Vocês erraram, o número sorteado foi >> {rand}!')
        if i <= 0:
             print(f'Esgotaram suas chances>> {i}')
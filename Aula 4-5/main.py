# 1
# concatene uma cidade e uma adjetivo para ela
cidade = input('Digite o nome da cidade: ')
adjetivo = input('Digite um adjetivo: ')
print('Bem vindo {}{}'.format(cidade, adjetivo))


# 2
#concatene uma viagem e quem vai participar dela
name = input('Digite seu name: ')
destino = input('Digite o nome do destino da viagem: ')
print('Eu, {} vou viajar para a {}' .format(name, destino))


# 3
# concatene função programador seu nome ou o nome do usuário
func = 'Analista de Dados '
nome = input("Selecione seu nome de usuário ")
print('{}{}' .format(func, nome))

# Exercicio 01
inteiro = int(input('Digite um número inteiro: '))
quadrado = inteiro **2
print('O Seu número inteiro é {} o resultado ao quadrado será: {}'.format(inteiro, quadrado))

# Exercicio 02
Nome = input('Digite seu nome: ')
Sobrenome = input('Digite seu sobrenome: ')
print('O seu nome completo é {} {}'.format(Nome, Sobrenome))

# Exercicio 03
n1 = input('Escolha um número: ')
n2 = input('Escolha outro número: ')
print('O primeiro number foi {} e o segundo foi {}'.format(n1,n2))

# Exercicio 04
lang = 'Python'
n = 7
print('{}{}'.format(lang, n))

# Exercicio 05
Frase = 'A vida é: '
palavra = input('Escolha uma palavra para completar a Frase: A vida é: ')
print('{}{}' .format(Frase,palavra))

# Desafio | Calculadora
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))

print("Soma: ", n1 + n2)
print("Subtracão: ", n1 - n2)
print("Multiplicação: ", n1 * n2)
print("Divisao: ", n1 / n2)
print("Divisao inteira: ", n1 // n2)
print("Exponenciação: ", n1 ** n2)

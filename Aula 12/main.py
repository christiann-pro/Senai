import statistics

note = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

print('--- Seja bem vindo ao SENAI ---\n')
selection = input(f'{1}. Acessar a m�dia de notas\n{2}. Acessar a moda\n\n')

def sel():
    if selection == '1':
      media = statistics.mean(note)
      print(f'A m�dia >> {media}')
      print(f'A menor nota da escola � >> {note[0]}')
      print(f'A maior nota da escola � >> {note[9]}')
    
    elif selection == '2':
      moda = statistics.mode(note)
      print(f'A nota que mais aparece entre a m�dia � >> {moda}')
    
    else:
      print(f'Sequ�ncia incorreta! Somente 1 - 2. :D')

# ------------------------------------------------------------------------------
# Chamando 
sel()
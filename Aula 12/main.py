import statistics

note = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

print('--- Seja bem vindo ao SENAI ---\n')
selection = input(f'{1}. Acessar a média de notas\n{2}. Acessar a moda\n\n')

def sel():
    if selection == '1':
      media = statistics.mean(note)
      print(f'A média >> {media}')
      print(f'A menor nota da escola é >> {note[0]}')
      print(f'A maior nota da escola é >> {note[9]}')
    
    elif selection == '2':
      moda = statistics.mode(note)
      print(f'A nota que mais aparece entre a média é >> {moda}')
    
    else:
      print(f'Sequência incorreta! Somente 1 - 2. :D')

# ------------------------------------------------------------------------------
# Chamando 
sel()
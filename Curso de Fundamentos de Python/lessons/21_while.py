# Cómo hacer un loop while en Python

'''
# Si se busca un loop que se ejecute en todo momento:
while True:
  print('Soy un loop infinito :O')
'''
counter = 0
'''
# Para que el loop termine en algún momento, ponemos una condición
while counter < 10:
  counter += 1
  print(counter)
'''
'''
# Para romper el loop antes, usamos la palabra reservada 'break'
while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
'''
'''
Para saltarnos bloques de código hasta tener una condición dada,
usamos la palabra reservada 'continue'
'''
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter) # Solo hasta que counter == 15 empezará a imprimir
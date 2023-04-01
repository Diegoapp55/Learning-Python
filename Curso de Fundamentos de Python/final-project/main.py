import random
# Aplicamos las tuplas para definir las tres opciones posibles
options = ('piedra', 'papel', 'tijera')
round = 1
user_score = 0
computer_score = 0

# Iniciamos solicitando el número de puntos para ganar el juego
print('Bienveni@ a piedra, papel o tijera')
player_name = input('Ingresa tu nickname: ')
'''
Para que la puntuación se imprima correctamente, el nickname debe ser
par... si no lo es, lo arreglamos
'''
if len(player_name) % 2 != 0:
  player_name = player_name + " "

# Para imprimir los puntajes centrados, debemos rellenar con " "
spaces = " " * (len(player_name) // 2)
comp_spaces = " " * (len("Computadora") // 2)
delimiter_spaces = (len(player_name) + len("Computadora") + 9)

max_rounds = int(input('¿A cuántos puntos será el juego?: '))

while user_score < max_rounds and computer_score < max_rounds:
  print("-" * delimiter_spaces)
  print(" " * (delimiter_spaces // 2 - 4) + "ROUND", round)
  print("-" * delimiter_spaces)
  print(f"| {player_name} | Computadora |")
  if user_score < 10:
    if computer_score < 10:
      print("| " + spaces + str(user_score) + spaces + "| " + comp_spaces +
            str(computer_score) + comp_spaces + " |")
    else:
      print("| " + spaces + str(user_score) + spaces + "| " + comp_spaces +
            str(computer_score) + comp_spaces + "|")
  else:
    if computer_score < 10:
      print("|" + spaces + str(user_score) + spaces + "| " + comp_spaces +
            str(computer_score) + comp_spaces + " |")
    else:
      print("|" + spaces + str(user_score) + spaces + "| " + comp_spaces +
            str(computer_score) + comp_spaces + "|")

  user_option = input('\n¿piedra, papel o tijera?: ').lower()
  round += 1
  '''
  Hacemos una comprobación de la entrada del usuario para evitar errores
  de funcionamiento del juego
  '''
  if not user_option in options:
    print('No es una opción válida, intenta otra vez')
    continue

  computer_option = random.choice(options)  #Elige aleatorio una de las 3

  print('\n -> La computadora elige: ', computer_option,'\n')

  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'papel':
      print('Papel le gana a piedra')
      print('Gana la computadora!')
      computer_score += 1
    else:
      print('Piedra le gana a tijera')
      print('Gana el usuario!')
      user_score += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel le gana a piedra')
      print('Gana el usuario!')
      user_score += 1
    else:
      print('Tijera le gana a papel')
      print('Gana la computadora!')
      computer_score += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera le gana a papel')
      print('Gana el usuario!')
      user_score += 1
    else:
      print('Piedra le gana a tijera')
      print('Gana la computadora!')
      computer_score += 1

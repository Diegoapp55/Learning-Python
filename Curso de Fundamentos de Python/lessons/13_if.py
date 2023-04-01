# Aprendiendo a programar el condicional if, else, else if en python

'''
En python ponemos : para indicar que ahí se abre una subrutina, luego
debemos dar enter y añadir una indentación. Si no se indenta, el
condicional queda esperando ese bloque y nos da error. Por esto es que
el código en python no se indenta... solo cuando se abren condicionales,
funciones, clases, etc.
'''
if True:
  print("Debería imprimir esto :o")

if False:
  print("Nunca imprimirá esto UnU")

pet = input('¿Cuál es la mejor mascota?')

if pet == 'perro':
  print('vete a la mierda amigo')
elif pet == 'gato':
  print('se necesitan más personas como tú <3')
else:
  print('jmmm, disculpa, yo no hablo taka taka :S')

'''
Este es el momento en el que no supero que else if se escriba como
elif... pobre niña jajsjs
'''
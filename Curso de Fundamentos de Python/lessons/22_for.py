# Cómo hacer un loop for en Python

'''
Esto es un poco distinto a Java, pues debemos usar el método range, el
cual nos genera un set de números de 0 a 19 para indicar los límites de
la iteración. Luego de la sentencia 'for', se indica el nombre de la
variable iteradora, la cual tomará valores enteros que están contenidos
en la lista que retorna range()
'''
'''
for element in range(20):
  print(element)
'''
# Si necesitamos que el iterador no inicie en 0:
'''
for element in range(1, 21):
  print(element)
'''
# Y, al igual que con las listas, podemos iterar 'saltando' valores:
'''
for element in range(1, 21, 2): # Recorre de 2 en 2 el rango
  print(element)
'''

'''
En Python, no necesitamos especificar si es un loop for o foreach,
basta con decirle que no itere sobre un range() sino sobre una colección
(Estructura de datos), para que actúe como el foreach de Java :D
'''
my_list = [23, 55, 25, 7, 343, 69]
for i in my_list:
  print(i) # Itera len(my_list) veces y nos imprime los elementos

my_tuple = ("Luz", "Diego", "Sofi", "Sammy")
for i in my_tuple:
  print(i) # Itera len(my_tuple) veces y nos imprime los elementos

# Con diccionarios, la interacción es interesante
product = {
  'name': 'Camisa',
  'price': 100,
  'in_stock': True
}
'''
for i in product:
  print(i) # Nos imprime solo los keys
'''
'''
for key in product:
  print(key, "=", product[key]) # Mucho mejor :)
'''
# Pero existe una forma más cómoda de hacer esto... Python moment
for key, value in product.items(): # Solo si cada elem. es una tupla
  print(key, "=", value)
# Esto es posible porque, recordar que items() retorna una tupla con la lista de pares (key,value), como si fuera una matriz

# Es muy común en el ámbito profesional encontrar listas de diccionarios
people = [
  {
    'name': 'Diego',
    'age': 22
  },
  {
    'name': 'Sammy',
    'age': 7
  },
  {
    'name': 'Sofi',
    'age': 7
  }
]
'''
Al trabajar con páginas web y bases de datos por ejemplo, es muy común
que el manejo de los datos se haga en ese formato, entonces, es
importante que sepamos cómo manipular estas estructuras de datos
'''
for person in people:
  print(person) # Nos imprime cada diccionario
  print('name:', person['name']) # Nos imprime solo los values de 'name'
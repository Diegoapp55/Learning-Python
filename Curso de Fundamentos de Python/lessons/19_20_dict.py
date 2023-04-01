# Aprendiendo a crear y trabajar con diccionarios

# Podemos crear un diccionario vacío con corchetes, así:
my_dict = {}
print(type(my_dict))

'''
Para inicializarlo, separamos sus elementos con ',' y recordando que
los diccionarios tienen un key y un value, separamos estos últimos con
':'
'''
my_dict = {
  'avión': 'Vehículo aéreo',
  'boliviano': 'Oriundo de Bolivia',
  'cartero': 'Oficio de repartir cartas'
}
print(my_dict)
print("Tamaño del diccionario:", len(my_dict))
# NOTA: No necesariamente son para construir un diccionario, por ejemplo
usuario_1 = {
  'Nombre': 'Diego Sánchez',
  'Edad': 22,
  'Fondos (US)': 193.75
}
print(usuario_1)

'''
Son más fáciles de leer que una lista o tupla, ya que no necesitamos
primero averiguar el índice de un elemento, sino únicamente preguntar
por el key que lo referencia
'''
print(usuario_1['Nombre'])
# Es una mejor práctica utilizar el método get()
print(usuario_1.get('Nombre'))
'''
El método get() hace lo mismo que indicar el key entre corchetes
cuadrados, pero se diferencia en el hecho de que, si se le indica un key
que no existe, get() tiene como manejar la excepción asociada, mientras
que buscando de la otra forma no, lo cual nos dará un error que frene la
ejecución de nuestros programas
'''
# print(usuario_1['Existo?']) # KeyError: 'Existo?'
print(usuario_1.get('Existo?')) # Retorna nulo (None)

# Podemos también validar si existe o no el key para evitar los None
print('Nombre' in usuario_1)
print('Existo?' in my_dict)
print('----' * 10)

# Podemos almacenar listas referenciadas por un key:
usuario_2 = {
  'name': 'Diego',
  'last_name': 'Sánchez',
  'age': 72,
  'hobbies': ['Guitar playing', 'Gaming', 'Watch series']
}
print(usuario_2)
print('----' * 10)

# Para agregar un nuevo par key:value lo hacemos así:
usuario_2['langs'] = ['Java', 'Python', 'C++', 'Git', 'Assembler']
print(usuario_2)
print('----' * 10)

# Para actualizar los datos de un key, lo hacemos así:
usuario_2['name'] = 'Diego Alejandro'
usuario_2['last_name'] = 'Sánchez Mendoza'
usuario_2['age'] -= 50
usuario_2['hobbies'].append('Crocheting')
print(usuario_2)
print('----' * 10)

'''
Para eliminar un key y por ende, todos sus elementos referenciados,
usamos la palabra reservada 'del' o el método pop(). La diferencia
radica en que, si usamos el método, este retorna el elemento eliminado,
pero si usamos 'del', solo se elimina y ya. En este caso, a diferencia
de en las listas, pop() no se puede pasar sin argumento, sí o sí se le
debe indicar un key; además, si se pasa un key que no existe, se
producirá un KeyError
'''
# del usuario_2['hobbies'] # Si solo queremos eliminar, usar este
lista_test = usuario_2.pop('hobbies')
print(usuario_2)
print("La lista de hobbies eliminada:", lista_test)
print('----' * 10)

'''
Existen 3 métodos esenciales al trabajar con diccionarios para poder
trabajar con su información almacenada
'''
# Retorna una tupla con la lista de pares de tuplas (key,value)
print('Items del diccionario: ', usuario_2.items())
# Retorna una tupla con la lista de keys
print('Keys del diccionario: ', usuario_2.keys())
# Retorna una tupla con la lista de values
print('Values del diccionario: ', usuario_2.values())

'''
NOTA: Ojo, si se desea manipular lo que retornan estas funciones, se
tiene que hacer un casting list() o de lo contrario se tendrá 1 tupla
con lo demás dentro
'''
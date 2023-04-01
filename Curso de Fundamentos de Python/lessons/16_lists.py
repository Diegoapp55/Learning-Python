# Cómo crear listas (arrays) en Python

# Separamos los elementos con coma y dentro de corchetes cuadrados
numbers = [1, 2, 3, 4]

# Las listas de Python pertenecen a la clase 'list'
print(numbers)
print(type(numbers))

tasks = ["aprender Python", "jugar al LoL", "Deutsch learnen"]
print(tasks)

'''
Al pertenecer a la clase 'list', no importa si los elementos son de
tipos de dato diferentes
'''
types = [1, True, "Hola"]
print(types)

# Podemos usar los mismos conceptos de indexación que vimos con strings
print(numbers[1])
print(tasks[2])
print(numbers[:2])

# En listas podemos "mutar" los contenidos de un índice en particular
print(types)
types[1] = 3.1416
print(types)

'''
Eso mismo no se puede hacer con strings... allí tocaría usar algún
método como replace()
'''
ejemplo = "Que mondá"
# ejemplo[2] = "é"
ejemplo = ejemplo.replace("e","é")
print(ejemplo)

'''
También podemos usar la operación 'in' para saber si un elemento está
contenido en una lista, independientemente de su índice. Tal y como lo
hace contains() en Java
'''
print("Deutsch learnen" in tasks)
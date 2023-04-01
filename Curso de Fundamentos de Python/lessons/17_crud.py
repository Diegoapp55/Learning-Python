'''
CRUD: Create, Read, Update, Delete. Operaciones básicas de cualquier
Lista
'''

numbers = [1, 2, 3, 4, 5] # Create
print(numbers[1]) # Read
numbers[-1] = 10 # Update
print(numbers)

'''
Podemos aumentar el tamaño de nuestra lista (array dinámico) gracias a
los métodos append() -> Agrega al final e insert() -> Agrega en el
índice que se le indique.
(Al profe Herrera no le gusta esta lección :v)
'''
numbers.append(700)
print(numbers)
numbers.insert(0, "Te me cuidas") # Agrega "Te me cuidas al principio"
print(numbers)
numbers.insert(3, "Buenos días") # Inserta "Buenos días" en el índice 3
print(numbers)
print("----" * 10)

# Podemos fusionar listas como si concatenásemos strings
pendientes = ["TODO 1", "TODO 2", "TODO 3"]
lista_mamadisima = numbers + pendientes
print(lista_mamadisima)

'''
Si necesitamos actualizar "TODO 2" por ejemplo, no necesitamos conocer
su índice (eso no siempre se va a poder), entonces, existe el método
index(), el cual retorna el índice del valor que se le pase de argumento
'''
indice_de_interes = lista_mamadisima.index("TODO 2")
print(indice_de_interes)
lista_mamadisima[indice_de_interes] = "Adelantar Señales II"
print(lista_mamadisima)
print("----" * 10)

# ¿Cómo hacemos el Delete?
'''
Para ello, usamos el método remove() -> Elimina el elemento
especificado (no el índice) ó pop() -> Elimina ell último elemento de la
lista si no se le pasa parámetro, o elimina el elemento del índice que
se le pase como argumento
'''
lista_mamadisima.remove("TODO 1")
print(lista_mamadisima)
lista_mamadisima.pop()
print(lista_mamadisima)
lista_mamadisima.pop(0) # Elimina el elemento del índice 0 (el primero)
print(lista_mamadisima)
print("----" * 10)

# Podemos invertir toda una lista con el método reverse()
lista_mamadisima.reverse()
print(lista_mamadisima)

# Para ordenar una lista, podemos usar el método sort()
prueba_sort = [2, 6, 1, 9, 9, 5, 0, 13]
print(prueba_sort)
prueba_sort.sort()
print(prueba_sort)

# También sirve con strings, como en Java :)
prueba_sort_strings = ["Cacatúa", "Colibrí", "Armadillo", "Panda", "Chigüiro", "Canguro"]
print(prueba_sort_strings)
prueba_sort_strings.sort()
print(prueba_sort_strings)

'''
OJO: El método sort() no se puede usar en listas que contengan tipos
de datos mezclados... hacerlo dará lugar a una excepción
'''
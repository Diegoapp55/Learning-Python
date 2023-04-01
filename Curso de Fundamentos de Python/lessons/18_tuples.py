# Cómo crear la Estructura de Datos "Tupla" en Python

'''
Una tupla se diferencia de una lista en tanto se declara con paréntesis
() y no con corchetes cuadrados []
'''
numbers = (1, 2, 3, 5, 2)
strings = ("Juanes", "Sergio", "David", "Diego", "Luz")
mixed = ("Hola", 1, True)
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))
print(mixed)
print(type(mixed))

# También podemos acceder a los elementos almacenados, como sabemos
print(numbers[0])
print(strings[1])
print(mixed[2])
print("----" * 10)

'''
Pero... la diferencia con las listas es que las tuplas son de solo
lectura, una vez creadas, no se pueden modificar ni se les pueden
agregar más elementos o eliminar los existentes
'''
# numbers[1] = "Se puede?" # Lanza una excepción

# Podemos consultar el índice de un elemento
print(strings.index("David"))
# NOTA: Si hay duplicados en la lista, retorna el índice del primero
print(numbers.index(2))

# Y podemos contar cuántas veces está un elemento en la lista
print(numbers.count(2))
print("----" * 10)

# Podemos hacer casting con tuplas hacia list para poder modificarlas :D
numbers = list(numbers)
print(numbers)
numbers.remove(2)
print(type(numbers))
print(numbers)

# Si queremos "volver a proteger la lista", hacemos el cast inverso :P
numbers = tuple(numbers)
print(type(numbers))
print(numbers)
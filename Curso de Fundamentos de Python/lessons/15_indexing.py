# Indexación y Slicing en strings

text = "Ella sabe Python"
# En Python, los arrays y demás se indexan desde 0
print(text[0])
print(text[1])
# print(text[999]) # Se lanza una excepción
# print(text[len(text)]) # Ojo, se indexa desde cero... excepción moment
print(text[len(text) - 1])
print("----" * 10) # Imprimimos un separador para ordenar mejor jaja

'''
En Python, podemos indicar índices negativos para recorrer el arreglo o string de derecha a izquierda :O. Así, no es necesario calcular la longitud y restarle 1 para obtener el último elemento :D
'''
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
print(text[-6])
print("----" * 10)

'''
Cuando queremos extraer una parte de un string o array, aplicamos el
concepto de Slicing.
NOTA: El segundo límite no es inclusivo, actua como un <. Por ejemplo, al hacer: 
'''
print(text[0:5]) # Se imprimen los índices 0 a 4, el 5 no

'''
Python nos permite omitir el primer y último índice para no poner
siempre "desde 0 hasta N", o "desde N hasta len() - 1". Solo debemos
omitir escribir ese índice y lo asumirá solito
'''
print(text[:10])
print(text[-6:])

# Esto implica que podemos omitir los 2 índices y el "Slicing" en realidad nos va a retornar el string completo

print(text[:])

'''
Al igual que en la sintaxis de Matlab, podemos indicar cada cuanto
extraer ítems de un string o array con un tercer argumento
'''
print(text[5::1])
print(text[5:10:2])
print(text[::2])

# Cortesía:
subliminal = "PsFf5WsAun256FSmt4rRr5sZo<'/oZ2&"
print(subliminal[::8])
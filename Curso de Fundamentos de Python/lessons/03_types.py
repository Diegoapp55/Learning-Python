# Tipos de datos en python

# String (Se puede con "" y con '')
texto = "Buenos días"
texto2 = 'Buenos días'
print("texto =>", texto, "y texto2 =>", texto2)
# Python nos permite conocer el tipo de dato con la sentencia type(var)
print("texto es de tipo", type(texto))
print("texto2 es de tipo", type(texto2))

# int
numero = 12
print("numero =>", numero)
print("numero es de tipo", type(numero))

# boolean
is_single = True
print("is_single =>", is_single)
print("is_single es de tipo", type(is_single))

# float
numero2 = 3.1416
print("numero2 =>", numero2)
print("numero2 es de tipo", type(numero2))
'''
NOTA: Siempre que usemos input(), este retornará un String, sin
importar si el dato ingresado es String, int, boolean o float
'''

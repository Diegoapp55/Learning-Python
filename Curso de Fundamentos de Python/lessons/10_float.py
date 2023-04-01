x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

# En python, debemos tener cuidado con la precisión decimal
print(x == y) # False porque 3.3 != 3.3000000000000003

# Para comparar 2 float, debemos especificar la precisión deseada
y_string = format(y, ".2g") # Limita "y" a 2 cifras => 3.3

# format() retorna un string
print(type(y_string))
print(x, y_string)

# Recordar que no se pueden comparar strings con int o float
print(str(x) == y_string)

'''
La forma "matemática" de comparar floats es decir que estos sean
"aproximadamente iguales"
'''
tolerancia = 0.00001
print(abs(x - y) < tolerancia) # Si la diferencia es pequeña => True
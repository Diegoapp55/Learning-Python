# Aprendiendo a usar variables y la entrada por consola

print("Variables mood")

# Variable con string
my_name = "Diego"
print(my_name)

# Variable con entero
my_age = 22
print(my_age)

my_name = "Alejandro"
'''
No hay necesidad de finalizar el string con " ", python
automáticamente le pone el espacio antes del valor de my_name
'''
print("He cambiado, ahora soy", my_name)

# Cómo pedir entradas al usuario
my_name = input("¿Cuál es tu nombre?")
print("Bienvenid@", my_name)
my_age = input("¿Cuántos años tienes?")
print(my_name, "tiene", my_age, "años")

# Operaciones con Strings

nombre = "Diego Alejandro"
apellido = "Sánchez Mendoza"
print(nombre)
print(apellido)

# Concatenación
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Poner "" y ' dentro de strings sin tener errores (Los alternamos)
quote = "I'm Diego"
quote2 = 'She said "Hello"'
print(quote)
print(quote2)

# Strings con formato
# La forma rudimentaria, con concatenaciones
v1 = "Hola, mi nombre es " + nombre + " y mi apellido es " + apellido
# La forma burgués pero más tediosa
v2 = "Hola, mi nombre es {} y mi apellido es {}".format(nombre, apellido)
# La forma elegante y sencilla (python literalmente xD)
v3 = f"Hola, mi nombre es {nombre} y mi apellido es {apellido}"
print('v1:', v1)
print('v2:', v2)
print('v3:', v3)
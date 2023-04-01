# Aprendiendo a hacer casting a otros tipos de datos

# En python podemos hacer casting de forma dinámica (implícita)
nombre = "Nicolas"
print(type(nombre))
nombre = 12
print(type(nombre))
nombre = False
print(type(nombre))

# Para hacer casting a string, lo podemos hacer de 3 formas:
# De la forma rudimentaria:
valor = 12
print(type(valor))
valor = "12"
print(type(valor))

# De la forma burgués:
valor = 12
print(type(valor))
valor = str(valor)
print(type(valor))

# De la forma pythonística :v
valor = 12
ejemplo = f"{valor}" #Cuando hacemos eso estamos haciendo casting

'''
Esto es importante, ya que no podemos hacer cosas como esta:
edad = 12
print("Hola, tengo " + edad + " años")
Pues se estaría intentando concatenar string con int... En cambio,
debemos hacer esto:
print("Hola, tengo " + str(edad) + " años")
o
print(f"Hola, tengo {edad} años")
'''

# Para hacer casting a int, lo podemos hacer de esta forma:
numeroXD = '1234'
print(type(numeroXD))
# Nos da error porque no se puede operar entre string e int
# print(numeroXD - 1234)

# Casteamos y volvemos a intentarlo
numeroXD = int(numeroXD)
print(type(numeroXD))
print(numeroXD - 1234)
# Otras operaciones interesantes con strings para manipularlos

text = "Ella sabe programar en Python"

# "in" permite buscar si esa cadena de caracteres está dentro del string
print("JavaScript" in text)
print("Python" in text)

# len() permite conocer la longitud de un string (en caracteres)
size = len(text)
print(size)

# Podemos convertir todo un texto a mayúsculas con el método upper()
print(text)
print(text.upper())
# Y a minúsculas con el método lower()
print(text.lower())
print(text.lower())

'''
Podemos contar el número de veces que aparece una serie de caracteres o
un solo caracter con el método count()
'''
print(text.count("a"))
print(text.count("Py"))

# Podemos invertir las mayúsculas y minúsculas con el método swapcase()
print(text.swapcase())

'''
Podemos comparar si el string comienza con una serie de caracteres con
el método startswith() o si finaliza con una serie de caracteres con el
método endswith()
'''
print(text.startswith("Ella"))
print(text.endswith("Java"))

# Podemos reemplazar partes de un string con el método replace()
print(text.replace("Python","Java"))
print(text) # replace() no altera permanentemente text si no se indica
text = text.replace("Python","Java")
print(text) # Ahora si

text_2 = "este ES UN Título"
print(text_2)

'''
Podemos obtener un texto que tenga solo la primera letra mayúscula y el
resto minúsculas con capitalize()
'''
print(text_2.capitalize())

'''
Podemos obtener un texto que tenga solo cada inicial con mayúscula y el resto en minúsculas con title()
'''
print(text_2.title())

'''
Finalmente, podemos averiguar si un string contiene solo números con el método isdigit(). Pero ojo, solo si es un número entero
'''
print(text_2.isdigit())
print("3.1416".isdigit())
print("31416".isdigit())

# NOTA: Existen muchos otros métodos con strings... revisar la documentación de Python :3
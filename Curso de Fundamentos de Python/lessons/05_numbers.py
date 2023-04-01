# Aprendiendo a diferenciar entre int y float y algunas op interesantes

lives = 3
# print(type(lives))
age = 22
budget = 100
temperature = 12.12
# print(type(temperature))
print("El jugador ha sido atacado")
lives -= 1
print(lives)
print("El jugador ha consumido un paquete de vidas")
lives += 1
print(lives)

'''
Para números muy grandes o muy pequeños, python los vuelve notación científica de forma automática
'''
print(3400000000000000000.1) # Para números grandes toca poner decimal
print(0.0000000000000000123) # Este si es automático
# Aprendiendo a realizar operaciones aritméticas en python

# Al igual que en otros lenguajes, tenemos +, -, *, /, %
print(15 + 5)
print(15 - 3)
print(15 * 4)
print(15 % 4)

# Como python hace casting automático, la división no retornará un antero
print(15 / 4)

# Si se quiere obtener solo la parte entera, no es necesario castear
print(15 // 4)

# Para obtener la potencia de un número:
print(2 ** 6) # 2 ^ 6 = 64

# En strings, además de la concatenación (+) existe la repetición (*)
print('Hola ' + 'Mundo!')
print('Hola' * 5)

'''
Precedencia de los operadores:Para ello, seguimos las siglas PEMDAS
Paréntesis
Exponentes
Multiplicación
División
Adición
Sustracción

Y siempre se evalúa de izq. a der.
'''
# Ejemplo:
print(2 ** 3 + 3 - 7 / 1 // 4)
# Aprendiendo a hacer loops anidados en Python

# Las matrices son "listas de listas" xd
matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(matriz[0]) # Imprime la primera fila
print(matriz[0][1]) # Imprime el segundo elemento de la primera fila
print('----' * 10)

# Podemos recorrer la matriz de la forma clásica
for i in range(0, 3):
  print(matriz[i]) # Solo para hacer explícita cada fila
  for j in range(0, 3):
    print(matriz[i][j]) # Recorre los elementos por fila

print('----' * 10)

'''
O de la forma Phytonística aprovechando que las matrices son "listas de
listas" con loops for que iteren sobre listas y no sobre rangos
'''
for row in matriz: # Iteramos por cada elemento de la lista (cada fila)
  print(row)
  for column in row: # Iteramos por cada sub-lista (elem. de cada fila)
    print(column)
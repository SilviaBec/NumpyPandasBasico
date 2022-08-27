
import numpy as np



#Suma matrices
mat1 = np.array([[1,2],[2,3]])
mat2= np.array([[1,2],[2,3]])
mat3= mat1 +mat2
print(mat3)

#Matriz de solo ceros
#2 filas vs 3 columnas, el shape
matriz= np.zeros((2,3))
print(matriz)

#matriz solo unos
matriz2=np.ones((4,3))
print(matriz2)

#Matriz de dato cualquiera
matriz3= np.full((3,3),9)
print(matriz3)

#Mat. Identidad
matriz4= np.eye(5)
print(matriz4)

matriz5 = np.random.random((4,4))
print(matriz5) 
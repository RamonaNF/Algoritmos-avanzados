"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 06 de noviembre del 2023
  
  Descripción: Pruebas de la implementación del
               algoritmo de Welsh-Powell para el 
               coloreo de grafos.
  
"""

from Welsh_Powell import welsh_powell
from UGraph import Ugraph

nodos = 0
flag = False
adyacencias = []

with open("inputs/input5.txt", 'r') as info:
    for linea in info:
        if not flag:
            nodos = int(linea.strip())
            flag = True

        else:
            adyacencias.append([int(conexion) for conexion in linea.strip().split(" ")])


print(nodos)
for row in adyacencias:
    print(row)
print()


grafo = Ugraph(False)
for i in range(len(adyacencias)):
    for j in range(len(adyacencias[i])):
        if adyacencias[i][j]:
            grafo.add_edge(i, j)

print(grafo)

nodos, colores = welsh_powell(grafo)

for i in range(len(colores)):
    print("Vértice:", nodos[i][0], "| Color asignado:", colores[i])

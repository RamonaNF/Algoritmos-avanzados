"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 22 de octubre del 2023
  
  Descripción: Casos prueba para las funciones
               de dijkstra y floyd.
  
"""

from Dijkstra import dijkstra
from Floyd import floyd

n = 0
flag = False
adyacencias = []

with open("inputs/input5.txt", 'r') as info:

    for linea in info:
        if not flag:
            n = int(linea.strip())
            flag = True

        else:
            adyacencias.append([])

            for num in linea.strip().split(" "):
                num = int(num)

                adyacencias[ len(adyacencias) - 1 ].append(num)

print("Mapa", n, "x", n)
for row in adyacencias:
    print(row)


# Grafo
graph = {}
for i in range(len(adyacencias)):
    graph[i] = []
    
    for j in range(len(adyacencias[i])):

        if adyacencias[i][j] != -1:
            graph[i].append((j, adyacencias[i][j])) # Nodo, costo


print("\nDijkstra")
for i in range(n):
    for j in range(n):
        if i != j:
            print("node", (i+1), "to node", str(j + 1) + ": ", dijkstra(i, j, graph))


print("\nFloyd")
resultadoFloyd = floyd(adyacencias)

for row in resultadoFloyd:
    print(row)

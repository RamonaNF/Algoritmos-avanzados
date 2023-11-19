from Graph import Wgraph
from MST import MST
from TSP import TSP
from Cercania import Coordenate, nearest_central
from Flujo_maximo import max_flow as max_flow_func
import copy

nodos = 0
coordenates = []
graphList = []
flujos = []
target = None
flag = 0

with open ("inputs/input1.txt", 'r') as info:
    for linea in info:
        if flag == 0:
            nodos = int(linea.strip())
            flag = flag + 1

        elif flag == 1:
            graphList.append([int(num) for num in linea.strip().split(' ')])
            if len(graphList) == nodos:
                flag = flag + 1

        elif flag == 2:
            flujos.append([int(num) for num in linea.strip().split(' ')])
            if len(flujos) == nodos:
                flag = flag + 1

        elif flag == 3:
            x, y = linea.strip().split(',')

            x = int(x[1:])
            y = int(y[0:len(y)-1])
            
            coordenates.append(Coordenate(x,y))

            if len(coordenates) == nodos:
                flag = flag + 1

        else:
            x, y = linea.strip().split(',')

            x = int(x[1:])
            y = int(y[0:len(y)-1])

            target = Coordenate(x,y)


copied = copy.deepcopy(graphList)

print("Punto 01: ÁRBOL DE EXTENSIÓN MÍNIMA")
print(MST(copied))


print("Punto 02: PROBLEMA DEL AGENTE VIAJERO")
origin, path, costo = TSP(graphList)

printStr = str(origin) + " -> "
for nodo in path:
    printStr = printStr + nodo + " -> "
printStr = printStr + origin

print(printStr)
print("El costo: ", costo)


print("\n\nPunto 03: FLUJO MÁXIMO")

max_flow = Wgraph(True)
for i in range(len(flujos)):
    for j in range(len(flujos[i])):
        if flujos[i][j]:
            max_flow.add_mutable_edge(chr(ord('A') + i), chr(ord('A') + j), flujos[i][j])

print("Flujo máximo: ", max_flow_func(max_flow, 'A', chr(ord('A') + len(flujos)-1)))


print("\nPunto 04: COORDENADA MÁS CERCANA")
central = nearest_central(coordenates, target)
print("La central más cercana a", target, "es", coordenates[central[1]], "con una distancia de", central[0])

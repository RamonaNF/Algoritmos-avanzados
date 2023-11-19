"""
  TRAVELING SALESMAN PROBLEM
    Pasando por las colonias no visitadas una
    vez y terminando en el punto de inicio.

  Complejidad: O( N² )
  
"""

from Graph import Wgraph
from collections import deque
import copy
import sys


def dfs(grafo: Wgraph, origin: str, destiny: str):
    i = 0
    stack = []

    visited = set()
    path = {}

    stack.append(origin)

    while len(stack) > 0:
        node = stack.pop()

        if node == destiny:
            break

        if node not in visited:
            visited.add(node)
            movements = grafo.get_connections_from(node)
            
            for in_node, cost in movements:
                if in_node == destiny and i == 0:
                    continue
                
                stack.append(in_node)


                if in_node not in path:
                    path[in_node] = node
                            
        i += 1
    
    minPath = [destiny]

    if destiny not in path.keys():
        return deque()
    
    node = path[destiny]

    while node != origin:
        minPath.insert(0, node)
        node = path[node]
        
    return deque(minPath)
        

def isCycled(grafo : Wgraph, begin : tuple) -> int:
    # Búsqueda en amplitud 
    visited = set()
    queue = deque([begin])

    while len(queue) > 0:
      nodo = queue.pop()
      visited.add(nodo)

      connections = grafo.get_connections_from(nodo)
      for connection, *_ in connections:
        if connection in queue: # Si la conexión ya está pendiente de visitar, está ciclado
              return 0 

        if connection not in visited: # Si la conexión no ha sido visitada
            queue.append(connection) # Se añade a las conexiones por visitar

    return len(visited)


def degree (grafo: Wgraph, nodo: str) -> int:
    return len(grafo.get_connections_from(nodo))

    
def TSP(grafo : list) -> Wgraph:
    original_graph = copy.deepcopy(grafo)

    visited = set()
    traveling = Wgraph(False)
    connected = 0

    while len(grafo) != connected: # Mientras no hayamos conectado todos los nodos
        current_min = []
        
        for i, row in enumerate(grafo): # Buscamos la conexión con el peso más pequeño
          local_min = [i, row.index(min(elem for elem in row if elem > 0))] # Almacenamos su posición en la matriz

          if len(current_min) == 0 or grafo[i][local_min[1]] < grafo[current_min[0]][current_min[1]]:
            current_min = local_min

        nodo1 = chr(ord('A') + current_min[0])
        nodo2 = chr(ord('A') + current_min[1])
        costo = grafo[current_min[0]][current_min[1]]

        # Añadimos la conexión más pequeña
        traveling.add_edge(nodo1, nodo2, costo)

        connected = isCycled(traveling, nodo1)
        if connected == 0 or degree(traveling, nodo1) > 2 or degree(traveling, nodo2) > 2: # Si está ciclado o ya es de un grado mayor a 2
            traveling.delete_connection(nodo1, nodo2, costo) # Eliminamos la conexión

        # Igualamos la conexión usada a inifinito para no volverla a usar
        grafo[current_min[0]][current_min[1]] = sys.maxsize
        
        # Marcamos los nodos visitados
        visited.add(nodo1)
        visited.add(nodo2)

    nodo1 = None
    nodo2 = None
    cost = 0
    
    for i in range(len(grafo)):
        if degree(traveling, chr(ord('A') + i)) == 1:
            if nodo1 == None:
                nodo1 = i

            else:
                nodo2 = chr(ord('A') + i)
                
                traveling.add_edge(chr(ord('A') + nodo1), nodo2, original_graph[nodo1][i])
                cost += original_graph[nodo1][i]
                break

    nodo1 = chr(ord('A') + nodo1)
    path = dfs(traveling, nodo1, nodo2)
    
    for i in range(len(path)):
        if i == 0:
            cost += traveling.get_cost(nodo1, path[i])
        else:   
            cost += traveling.get_cost(path[i - 1], path[i])

    return nodo1, path, cost

"""
  MINIMUM SPANNING TREE
    Conectando colonias para que compartan
    información usando fibra óptica.

  Complejidad: O(  )
  
"""

from Graph import Wgraph
from collections import deque
import sys


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


def MST(grafo : list) -> Wgraph:
    visited = set()
    minimum_spanning_tree = Wgraph(False)
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
        minimum_spanning_tree.add_edge(nodo1, nodo2, costo)

        connected = isCycled(minimum_spanning_tree, nodo1)
        if connected == 0: # Si está ciclado
            minimum_spanning_tree.delete_connection(nodo1, nodo2, costo) # Eliminamos la conexión

        # Igualamos la conexión usada a inifinito para no volverla a usar
        grafo[current_min[0]][current_min[1]] = sys.maxsize
        
        # Marcamos los nodos visitados
        visited.add(nodo1)
        visited.add(nodo2)
        

        
    return minimum_spanning_tree
      
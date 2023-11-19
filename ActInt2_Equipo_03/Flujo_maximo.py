"""
  FLUJO MÁXIMO
    Capacidad máxima de transmisión
    de datos entre colonias.

  Complejidad: O( N² )
  
"""
from Graph import Wgraph
from collections import deque
import heapq
import sys


class Node(object):
  def __init__(self, node: str, cost : int) -> None:
      self.node = node
      self.cost = cost

  def __repr__(self):
      return f"Node value: {self.node}\tCost: {self.cost}"

  def __lt__(self, other):
      return other.cost < self.cost

  def __eq__(self, other):
      return self.node == other.node and self.cost == other.cost


def dijkstra(start:str, end:str, graph: Wgraph) -> list :
    """
    La función dijkstra recibe dos puntos y un modelo y regresa
    el camino con mayor flujo a seguir para llegar del punto de 
    inicio al punto final
    """
    visited = set()
    path = {}

    pending = [Node(start,0)]
    heapq.heapify(pending)

    while(len(pending) > 0):
        front = heapq.heappop(pending)
        v = front.node
        c = front.cost

        if v == end:
            break

        if v not in visited:
            visited.add(v)

            for connection in graph.get_connections_from(v):
                if connection.cost > 0:
                    if c < connection.cost:
                        heapq.heappush(pending, Node(connection.node, c))
                    else:
                        heapq.heappush(pending, Node(connection.node, connection.cost))
            
                    if connection.node not in path:
                        path[connection.node] = v
                    
    maxPath = [end]
    min_cost = sys.maxsize
    
    if end not in path.keys():
        return deque()
    
    node = path[end]

    while node != start:
        maxPath.insert(0, node)
        node = path[node]
        
    return deque(maxPath)


def max_flow(graph : Wgraph, inicio: chr, final : chr) -> int :
    total_flow = 0
    path = dijkstra(inicio, final, graph)
    
    while len(path) > 0:
        print(path)
        min_cost = sys.maxsize

        for i in range(len(path)):
            if i == 0:
                aux_cost = graph.get_mutable_cost('A', path[i])
            else:   
                aux_cost = graph.get_mutable_cost(path[i-1], path[i])

            if aux_cost < min_cost:
                min_cost = aux_cost
                
        total_flow += min_cost
        print(min_cost)

        for i in range(len(path)):
            if i == 0:
                graph.edit_mutable_cost('A', path[i], graph.get_mutable_cost('A', path[i]) - min_cost)
            else:   
                graph.edit_mutable_cost(path[i-1], path[i], graph.get_mutable_cost(path[i-1], path[i]) - min_cost)
            
        path = dijkstra(inicio, final, graph)
    
    return total_flow

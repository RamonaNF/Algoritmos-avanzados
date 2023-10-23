"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 22 de octubre del 2023
  
  Descripción: Algoritmo para encontrar la ruta 
               más corta entre dos nodos.

  Complejidad: O ( N^2 )
  
"""
import heapq



class Node(object):
  def __init__(self, pos: int, steps : int) -> None:
      self.pos = pos
      self.steps = steps

  def __repr__(self):
      return f"Node value: {self.pos}\tSteps: {self.steps}"

  def __lt__(self, other):
      return self.steps < other.steps

  def __eq__(self, other):
      return self.pos == other.pos and self.steps == other.steps



def dijkstra(origin: int, destiny: int, graph: dict) -> int:
  visited = set()
  xVisit = [Node(origin, 0)]

  heapq.heapify(xVisit)
  

  while len(xVisit) > 0:
    node = heapq.heappop(xVisit)

    v = node.pos
    e = node.steps

    if v == destiny:
      return e

    if v not in visited:
      visited.add(v)

      for vertex, cost in graph[v]:
        heapq.heappush(xVisit, Node(vertex, e + cost))


  return -1


"""
  CENTRAL MAS CERCANA
    Capacidad máxima de transmisión
    de datos entre colonias.

  Complejidad: O( N )
  
"""

import math
import sys

class Coordenate:
    def __init__(self, x: int, y : int):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2))
    
    def __str__(self):
        return '(x: ' + str(self.x) + '), (y: ' + str(self.y)+ ')'

def nearest_central(coordenadas : list, objetivo: Coordenate):
    min_distance = [sys.maxsize, -1]

    for i, coordenada in enumerate(coordenadas):
        aux = objetivo.distance(coordenada) 
        if aux < min_distance[0]:
            min_distance[0] = round(aux, 3)
            min_distance[1] = i
    
    return min_distance
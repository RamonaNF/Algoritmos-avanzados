"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 10 de septiembre del 2023
  
  Descripción: .

  Complejidad: O (  ) 

"""

import sys 
import copy

movimientos = [[1, 0], [0, -1], [-1, 0], [0, 1]] # Derecha - Abajo - Izquierda - Arriba


def inBounds(mapa: list, movement: tuple) -> bool:
    if 0 <= movement[0] < len(mapa):
        if 0 <= movement[1] < len(mapa[0]):
            if mapa[movement[0]][movement[1]] == 1:
                return True
    
    return False


def isNeighbor(one: tuple, two: tuple):
    for mov in movimientos:
        if (one[0] + mov[0], one[1] + mov[1]) == two:
            return True
    
    return False


def back_tracking(mapa : list, target: tuple):
    visited = set()
    xVisit = [(0, 0)]
    prev = []

    camino = [[0 for i in range(len(mapa[0]))] for j in range(len(mapa))]
    steps = 1

    while len(xVisit) > 0:
        x, y = xVisit.pop()
        visited.add((x, y))

        camino[x][y] = steps
        steps += 1

        if (x, y) == target: 
            break
        
        
        get_back = True
        for mov in movimientos:
            if inBounds(mapa, (x + mov[0], y + mov[1])):  
                if (x + mov[0], y + mov[1]) not in visited:

                    if (x + mov[0], y + mov[1]) in xVisit:
                        xVisit.remove((x + mov[0], y + mov[1]))

                    xVisit.append((x + mov[0], y + mov[1]))
                    get_back = False


        if get_back:
            
            while len(prev) > 0 and len(xVisit) > 0 and not isNeighbor(prev[-1], xVisit[-1]):
                camino[prev[-1][0]][prev[-1][1]] = 0
                prev.pop()
                steps -= 1

            if len(prev) > 0: # isNeighbor
                camino[x][y] = 0
                steps -= 1
            
        else:     
            prev.append((x, y))
    
    return camino



def ramificacion_y_poda(mapa : list, target: tuple):
    visited = set()
    xVisit = [(0, 0)]
    prev = []

    camino = [[0 for i in range(len(mapa[0]))] for j in range(len(mapa))]
    mejorRuta = [[0 for i in range(len(mapa[0]))] for j in range(len(mapa))]
    
    steps = 1
    best = sys.maxsize

    while len(xVisit) > 0:
        x, y = xVisit.pop()
        visited.add((x, y))

        camino[x][y] = steps
        steps += 1

        if steps == best and (x, y) != target:
            while len(prev) > 0 and len(xVisit) > 0 and not isNeighbor(prev[-1], xVisit[-1]):
                camino[prev[-1][0]][prev[-1][1]] = 0
                prev.pop()
                steps -= 1

            if len(prev) > 0: # isNeighbor
                camino[x][y] = 0
                steps -= 1
            
            continue

        if (x, y) == target: 
            best = steps
            mejorRuta = copy.deepcopy(camino)
            visited.clear()
            
            while len(prev) > 0 and len(xVisit) > 0 and not isNeighbor(prev[-1], xVisit[-1]):
                camino[prev[-1][0]][prev[-1][1]] = 0
                prev.pop()
                steps -= 1

            if len(prev) > 0: # isNeighbor
                camino[x][y] = 0
                steps -= 1

            continue


        get_back = True
        for mov in movimientos:
            if inBounds(mapa, (x + mov[0], y + mov[1])):  
                if (x + mov[0], y + mov[1]) not in visited and camino[x + mov[0]][y + mov[1]] == 0:
                    
                   # if (x + mov[0], y + mov[1]) in xVisit:
                      #  xVisit.remove((x + mov[0], y + mov[1]))

                    xVisit.append((x + mov[0], y + mov[1]))
                    get_back = False


        if get_back:

            while len(prev) > 0 and len(xVisit) > 0 and not isNeighbor(prev[-1], xVisit[-1]):
                camino[prev[-1][0]][prev[-1][1]] = 0
                prev.pop()
                steps -= 1

            if len(prev) > 0: # isNeighbor
                camino[x][y] = 0
                steps -= 1
            
        else:     
            prev.append((x, y))
        
    return mejorRuta

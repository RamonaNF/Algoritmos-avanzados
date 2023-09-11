"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 10 de septiembre del 2023
  
  Descripción: Solucionando un laberinto 
               backtracking vs ramificación y poda.

  Complejidad: O( x^n )
  
"""
import sys
import copy

movimientos = [[1, 0], [0, -1], [-1, 0], [0, 1]] # Derecha - Abajo - Izquierda - Arriba

success = False
target = None
mapa = []

camino_backtracking = []

camino_poda = []
mejor_camino = []
best = sys.maxsize

def inBounds(movement: tuple, camino: list) -> bool:
    if 0 <= movement[0] < len(mapa):
        if 0 <= movement[1] < len(mapa[0]):
            if mapa[movement[0]][movement[1]] == 1 and camino[movement[0]][movement[1]] == 0:
                return True
    
    return False


def maze_solver(m : list, t: tuple):
    global target, mapa, camino_backtracking, mejor_camino, camino_poda
    
    target = t
    mapa = m
    
    camino_poda = [[0 for col in range(len(mapa[0]))] for row in range(len(mapa))]
    camino_backtracking = [[0 for col in range(len(mapa[0]))] for row in range(len(mapa))]
    mejor_camino = [[0 for col in range(len(mapa[0]))] for row in range(len(mapa))]

    camino_poda[0][0] = 1
    camino_backtracking[0][0] = 1
    mejor_camino[0][0] = 1

    back_tracking(2, (0,0))
    ramificacion_y_poda(2, (0,0))

    return camino_backtracking, mejor_camino


def back_tracking(steps: int, ini: tuple):
    global success, camino_backtracking
    
    k = 0 # Índice del movimiento
    
    while True:
        new_pos = (ini[0] + movimientos[k][0], ini[1] + movimientos[k][1])

        if inBounds(new_pos, camino_backtracking):
            camino_backtracking[new_pos[0]][new_pos[1]] = steps

            if camino_backtracking[target[0]][target[1]] == 0:
                back_tracking(steps + 1, new_pos)
                
                if not success:
                    camino_backtracking[new_pos[0]][new_pos[1]] = 0
            
            else:
                success = True
        
        k += 1
        
        if k > 3 or success:
            break


def ramificacion_y_poda(steps: int, ini: tuple):
    global success, camino_poda, mejor_camino, best
    
    k = 0 # Índice del movimiento
    
    while True:
        new_pos = (ini[0] + movimientos[k][0], ini[1] + movimientos[k][1])

        if inBounds(new_pos, camino_poda) and steps < best:
            camino_poda[new_pos[0]][new_pos[1]] = steps

            if camino_poda[target[0]][target[1]] == 0:
                ramificacion_y_poda(steps + 1, new_pos)
                
                camino_poda[new_pos[0]][new_pos[1]] = 0
            
            else:
                if best > steps:
                    mejor_camino = copy.deepcopy(camino_poda)
                    best = steps
                    
                    camino_poda[target[0]][target[1]] = 0
        
        k += 1
        
        if k > 3:
            break

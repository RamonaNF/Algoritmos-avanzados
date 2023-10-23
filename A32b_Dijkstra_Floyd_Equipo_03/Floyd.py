"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 22 de octubre del 2023
  
  Descripción: Algoritmo para encontrar el 
               camino mínimo de un grafo.

  Complejidad: O ( N^3 )
  
"""

def floyd(distancias: list) -> list:
    n = len(distancias)
    
    for k in range(n): # Nodo en el que se forma la cruz

        for i in range(n):
            if i != k: # No estás parado en la fila de la cruz

                for j in range(n): 
                    if j != k: # No estás parado en la columna de la cruz

                        if distancias[i][k] != -1 and distancias[k][j] != -1: # Si no hay valores infinitos
                            nueva = distancias[i][k] + distancias[k][j] 

                            if distancias[i][j] == -1 or nueva < distancias[i][j]: 
                                distancias[i][j] = nueva

    return distancias

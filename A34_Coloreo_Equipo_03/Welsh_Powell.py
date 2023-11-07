"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 06 de noviembre del 2023
  
  Descripción: 

  Complejidad: O (  )
  
"""

from UGraph import Ugraph

# 1. Ordenamos los vértices por grado
# 2. Seleccionamos un color y se lo asignamos al primer nodo no coloreado
# 3. Por cada nodo no adyacente al actual, le asignamos el mismo color (si no tiene un vecino con el mismo)

def welsh_powell(grafo: Ugraph):
  nodos = [] # (Vértice, Grado)
 
  for i in range(len(grafo.get_vertexes())):
    nodos.append((i, len(grafo.get_connections_from(i))))

  # Ordenamos los vértices por grado
  nodos.sort(key = lambda  vertice : vertice[1], reverse = True)
  
  colores = [0 for i in range(len(nodos))]
  
  color = 1
  nodo_actual = 0

  while nodo_actual < len(colores):
    if colores[nodo_actual] > 0: # Si ya está coloreado
      nodo_actual += 1 # Seguimos buscando nodos no coloreados
      continue

    # Sino, le asignamos un color
    colores[nodo_actual] = color

    adyacentes = grafo.get_connections_from(nodos[nodo_actual][0])

    for restante in range(nodo_actual + 1, len(colores)): # Para cada nodo que resta en la tabla
      if colores[restante] > 0: # Si está coloreado, continuamos
        continue

      if nodos[restante][0] in adyacentes: # Si es mi vecino, continuamos
        continue

      vecinos = grafo.get_connections_from(nodos[restante][0])
      
      flag = False
      for v in vecinos: # Sino, verifico que mis vecinos no tengan el color que quiero tener
        if colores[v] == color:
          flag = True
          break
      
      if flag:
        continue

      colores[restante] = color
    
    color += 1
    nodo_actual += 1



  for row in nodos:
    print(row)
  print(colores)

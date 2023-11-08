"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 06 de noviembre del 2023
  
  Descripción: Algoritmo para el coloreo de grafos.

  Complejidad: O ( N² )
  
"""

from UGraph import Ugraph

# 1. Ordenamos los vértices por grado
# 2. Seleccionamos un color y se lo asignamos al primer nodo no coloreado
# 3. Por cada nodo no adyacente al actual, le asignamos el mismo color (si no tiene un vecino con el mismo)

def welsh_powell(grafo: Ugraph):
  nodos = [] # (Vértice, Grado)
 
  for i in range(len(grafo.get_vertexes())):
    nodos.append((i, len(grafo.get_connections_from(i))))

  # Ordenamos los nodos por grado
  nodos.sort(key = lambda  vertice : vertice[1], reverse = True)
  
  colores = [0 for i in range(len(nodos))]
  
  color = 1

  for i in range(len(colores)):
    nodo = nodos[i][0] # (Vértice, Grado)

    if colores[i] > 0: # Si ya está coloreado, continuamos
      continue

    colores[i] = color

    adyacencias = grafo.get_connections_from(nodo) # Obtenemos sus vecinos

    # Para cada nodo restante en la lista, asignamos el color a los no adyacentes candidatos
    for j in range(i + 1, len(colores)):
      if colores[j] > 0: # Si está coloreado, continuamos
        continue

      if nodos[j][0] in adyacencias: # Si es adyacente, continuamos
        continue
      
      # Sino, verificamos que ninguno de sus vecinos tenga el color usado actualmente
      conexiones = grafo.get_connections_from(nodos[j][0])

      flag = False
      for c in conexiones: # Checo mis adyacentes para ver si el color está disponible
        # Bucamos el índice del nodo adyacente
        index = next(i for i, (v, *_) in enumerate(nodos) if v == c)
        
        if colores[index] == color: 
          flag = True
          break

      if not flag: # Si el color no está ocupado, se me asigna
        colores[j] = color 
        
    color += 1 

  #print("  Nodos", nodos) 
  #print("Colores", colores)
  return nodos, colores

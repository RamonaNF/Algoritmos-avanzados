"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 03 de septiembre del 2023
  
  Descripción: Cambio de monedas usando una aproximación greedy.

  Complejidad: O ( N ) 

"""

import numpy as np

def greedy_change(monedas:list, precio:int, pago:int):
  cambio = pago - precio
  monedas.sort(reverse = True) # Ordenamos las monedas de mayor a menor

  if cambio < 0:
    print("Te falta dinero")
    return

  den = 0 # denominación
  cantidad = {}
  
  while cambio > 0 and den < len(monedas):
    if monedas[den] > cambio:
      den += 1
      continue

    if monedas[den] in cantidad:
      cantidad[monedas[den]] += 1
    else:
        cantidad[monedas[den]] = 1
    
    cambio -= monedas[den]
  
  return cantidad

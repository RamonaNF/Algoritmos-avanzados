"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 29 de octubre del 2023
  
  Descripción: Solución del problema de la mochila
               mediante la programación dinámica

  Complejidad: O ( N² )
  
"""

def dp_knapsack(beneficios: list, pesos: list, capacidad: int) -> list:
  mochila = [[0 for j in range(capacidad + 1)] for i in range(len(beneficios) + 1)]

  pesos = [0] + pesos
  beneficios = [0] + beneficios
  
  for i in range(1, len(mochila)):
    for j in range(1, len(mochila[i])):
      if pesos[i] > j: # Si el elemento pesa más que lo que la mochila soporta
        mochila[i][j] = mochila[i - 1][j] # Permanece el máximo que se tenía
        continue
          
      mochila[i][j] = max(mochila[i - 1][j], beneficios[i] + mochila[i - 1][j - pesos[i]])
      
  return mochila

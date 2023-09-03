"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 03 de septiembre del 2023
  
  Descripción: Cambio de monedas usando una aproximación dinámica.

  Complejidad: O ( N2 ) 

"""

def dp_change(monedas:list, precio:int, pago:int):
    cambio = pago - precio
    monedas.sort()

    if cambio < 0:
      print("Te falta dinero")
      return

    matriz_dinamica = [[0 for cambio in range(cambio + 1)] for row in range(len(monedas))]

    for i in range(len(monedas)): # Para cada denominación de moneda (m)
      for j in range(cambio + 1): # Iteramos sobre la cantidad a devolver (c)
          
          if monedas[i] == min(monedas): 
              if j // monedas[i] != 0:
                matriz_dinamica[i][j]  = j // monedas[i] # El cambio [m, cantidad] = cantidad

          elif j < monedas[i]: # Si el cambio es menor al valor de la moneda
              matriz_dinamica[i][j] = matriz_dinamica[i - 1][j] # cambio [m, c] = cambio [m - 1, c]

          else: # cambio[m, c] = min (cambio [m - 1, c], 1 + cambio [m, c - v[m]])
              matriz_dinamica[i][j] = min(matriz_dinamica[i - 1][j], 1 + matriz_dinamica[i][j - monedas[i]])
    
    cantidad = {}

    # cambio [M, c] contiene cuántas monedas ocupamos
    i = len(matriz_dinamica) - 1
    j = cambio

    while matriz_dinamica[i][j] > 0:
      if i > 0 and matriz_dinamica[i][j] == matriz_dinamica[i - 1][j]:
        i -= 1

      else:
        if monedas[i] in cantidad:
          cantidad[monedas[i]] += 1
        else:
           cantidad[monedas[i]] = 1
        
        j -= monedas[i]
  
    return cantidad

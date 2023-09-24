"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 24 de septiembre del 2023
  
  Descripción: Suffix array.

  Complejidad: O( N log(N) )
  
"""

def suffix_array(palabra: str) -> list: 
    suffix_arr = {}
    
    for i in range(len(palabra) - 1, -1, -1):
        suffix_arr[palabra[i:]] = i

    return sorted(suffix_arr.items())

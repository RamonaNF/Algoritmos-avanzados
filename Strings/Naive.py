"""
  NAIVE STRING MATCHER
    Buscando coincidencias mediante la fuerza bruta

  Complejidad: O( m * (n - m) )   m: longitud de la cadena de búsqueda
                                  n: longitud de la cadena a buscar
  
"""
from time import time

def naive_matching(text: str, pattern: str):
  iterations = 0
  start_timer = time()
  
  coincidences = []
  candidates = len(text) - len(pattern) + 1

  for i in range(candidates):
    coincidence = True

    for j in range(len(pattern)):
      if pattern[j] != text[i + j]:
        coincidence = False
        break

      iterations += 1

    if coincidence:
      coincidences.append(i)

  end_time = time() - start_timer

  return iterations, coincidences, end_time

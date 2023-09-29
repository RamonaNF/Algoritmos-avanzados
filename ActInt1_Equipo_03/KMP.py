"""
  KNUTH-MORRIS-PRATT
    Buscando coincidencias mediante máquinas de estados finitos

  Complejidad: O( m + n )   m: longitud de la cadena de búsqueda
                            n: longitud de la cadena a buscar
  
"""

# Longest Prefix Suffix
def lps(pattern: str) -> list:
  pi = [0] * len(pattern)
  
  for i in range(1, len(pi)):
    # si P[π(i-1)] == P[i] entonces π(i) = π(i-1) + 1 
    if pattern[pi[i - 1]] == pattern[i]:
      pi[i] = pi[i - 1] + 1
    
    # sino π(i) = 0
    else:
      pi[i] = 0
    
  return pi


def kmp(text: str, pattern: str):
  pi = lps(pattern)
  i = 0
  j = 0

  coincidences = []
  
  while i < len(text):
    # Si j está dentro de los límites del patrón y coinciden
    if j < len(pattern) and text[i] == pattern[j]:   
      j += 1 
      
      if j == len(pattern): # Se encontró una coincidencia
        coincidences.append(i - j)
        
    elif j > 0: # Si j supera los límites del patrón o no hay coincidencia
        j = pi[j - 1] # Accedemos al valor del LPS anterior al fallo
        i -= 1 # Evitamos avanzar en el texto
    
    i += 1

  return coincidences

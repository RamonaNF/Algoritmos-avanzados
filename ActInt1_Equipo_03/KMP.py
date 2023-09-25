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
  pass


print(lps("10010001"))

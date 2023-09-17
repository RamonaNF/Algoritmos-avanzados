"""
  KNUTH-MORRIS-PRATT
    Buscando coincidencias mediante máquinas de estados finitos

  Complejidad: O( m + n )   m: longitud de la cadena de búsqueda
                            n: longitud de la cadena a buscar
  
"""
import numpy as np

# Longest Prefix Suffix
def lps(pattern: str) -> list:
  #"""
  pi = [0] * len(pattern)

  for i in range (1, len(pattern)):
    # si P[π(i-1)] == P[i] entonces π(i) = π(i-1) + 1 
    if pattern[i] == pattern[pi[i - 1]]: 
      pi[i] = pi[i - 1] + 1
    
    else: # sino π(i) = 0
      pi[i] = 0

  return pi

def kmp(text: str, pattern: str):
  iterations = 0
  coincidences = []
  pi = lps(pattern) # Prefix table

  i = 0
  j = 0
  
  while i < len(text):
    iterations += 1

    if j < len(pattern) and text[i] == pattern[j]:
      j = j + 1
      
      if j == len(pattern): # Coincidencia
        coincidences.append(i - (len(pattern) - 1))
            
    elif j > 0:
      j = pi[j - 1]
      i = i - 1        
  
    i = i + 1
  
  return iterations, coincidences

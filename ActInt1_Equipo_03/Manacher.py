"""
  MANACHER
    Buscando el palíndromo más largo

  Complejidad: O( n )
  
"""

def Manacher(text : str) -> str:
  mutated = [' '] * (len(text) * 2 + 3)
  mutated[0], mutated[-1], mutated[1]= '@', '$', '#'

  j = 2
  for i in range(len(text)):
    mutated[j] = text[i]
    mutated[j + 1] = '#'

    j += 2
  
  p = [0] * len(mutated)

  c, mirror = 1, 0
  leftbound, rightbound = 1, 1
  
  for i in range(1, len(mutated) - 1):

    p[i] = 1
    
    if leftbound < i < rightbound:
      mirror = c - (i - c)
      p[i] = min(p[mirror], rightbound - i)
      
    l = i - p[i]
    r = i + p[i]

    while mutated[l] == mutated[r]:
      l -= 1
      r += 1
      p[i] += 1
      

    l += 1
    r -= 1

    if p[i] + i > rightbound:
      rightbound = p[i] + i
      leftbound = p[i] - i 
      c = i

  m_val = max(p)
  m_index = p.index(max(p))
  palindrome = ''

  for i in range(m_index - m_val + 1, m_index + m_val):
    if mutated[i] != '#':
      palindrome += mutated[i]

  index = 0
  for i in range(0, m_index - m_val + 1):
    if mutated[i] != '#' and mutated[i] != '@' and mutated[i] != '$':
      index += 1
  
  return (palindrome, index)

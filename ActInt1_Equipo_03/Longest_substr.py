"""
  LONGEST COMMON SUBSTRING

  Complejidad: O( n * m )
  
"""

def longest_substr(text1: str, text2: str) -> str:
    coincidences = [[0 for col in range(len(text1))] for row in range(len(text2))]
    tup = [-1, -1] # index, len
    
    for row in range(len(text2)):
        for col in range(len(text1)):
            if text1[col] == text2[row]:
                if row > 0 and col > 0:
                    coincidences[row][col] = 1 + coincidences[row - 1][col - 1]

                else:
                    coincidences[row][col] = 1
                
                if coincidences[row][col] > tup[1]:
                    tup[0] = col
                    tup[1] = coincidences[row][col]
            
            else:
                coincidences[row][col] = 0
    
    return text1[tup[0] - tup[1] + 1 : tup[0] + 1]

"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 25 de agosto del 2023
  
  Descripción: Archivo de prueba para las implementaciones de merge sort.
  
"""

from MergeSort import mergeSort as sort1
from MergeSort_indices import mergeSort as sort2
from copy import copy
import numpy as np 

print("\nEjecutando casos prueba...")

for i in range(4): # Casos prueba aleatorios
    randomArray = list(np.random.rand(5)*100)
    randomArray2 = copy(randomArray)
    
    print("Array: ", randomArray, "\n")

    print("Primer método ", end="")
    sort1(randomArray)
    print(randomArray)
    
    print("Segundo método ", end="")
    sort2(randomArray2, 0, len(randomArray2) - 1)
    print(randomArray2, "\n")

from MergeSort import mergeSort as sort1
from MergeSort_indices import mergeSort as sort2
from copy import copy
import numpy as np 

print("\nEjecutando casos prueba...")

for i in range(4): # Casos prueba aleatorios
    randomArray = list(np.random.rand(5)*100)
    #randomArray2 = copy(randomArray)
    
    print("Array: ", randomArray, "\n")

   # print("Primer método\n")
   # sort1(randomArray)
   # print("Array Ordenado", randomArray, "\n")
    
    print("Segundo métodoo\n")
    sort2(randomArray, 0, len(randomArray) - 1)
    print("Array Ordenado", randomArray, "\n")

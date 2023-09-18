from KMP import kmp
from Naive import naive_matching
from time import time

with open("./Inputs/input4.txt", 'r') as input:
    pattern, text = [linea.strip() for linea in input]



start = time()
iterations, coincidences = naive_matching(text, pattern)
end = time() - start

print("-- Naive Algorithm --")
print("\nIterations: ", iterations)
print("Coincidences: ", len(coincidences))
#print("Coincidences: ", coincidences)
print("Execution time: ", end, " ms")



start = time()
iterations, coincidences = kmp(text, pattern)
end = time() - start

print("\n\n-- KMP Algorithm --")
print("\nIterations: ", iterations)
print("Coincidences: ", len(coincidences))
#print("Coincidences: ", coincidences)
print("Execution time: ", end, " ms")

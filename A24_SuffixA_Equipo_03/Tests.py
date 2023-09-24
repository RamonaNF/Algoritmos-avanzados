"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 24 de septiembre del 2023
  
  Descripción: Archivo de prueba para la
               implementación de suffix array.
  
"""
import sys
from Suffix_array import suffix_array

if len(sys.argv) != 2:
    print("No escribiste ninguna palabra")
    sys.exit()
    
palabra = sys.argv[1]

print("Sufijos")
print("\nPalabra: ", palabra)

i = 0
for suffix, index in suffix_array(palabra):
    print(i, " ", index, ": ", suffix)
    i += 1

print()
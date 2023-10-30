"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 29 de octubre del 2023
  
  Descripción: Casos prueba para el problema
               de la mochila.
  
"""

from Knapsack import dp_knapsack

beneficios = []
pesos = []

elementos = 0
capacidad_mochila= 0


with open("inputs/input4.txt", 'r') as info:
  lines = info.readlines()
  elementos = int(lines[0])
  
  beneficios = [int(b) for b in lines[1:elementos+1]]
  pesos = [int(p) for p in lines[elementos + 1: elementos + elementos + 1]]
  
  capacidad_mochila = int(lines[-1])


mochila = dp_knapsack(beneficios, pesos, capacidad_mochila)

print("\nCapacidad máxima: ", capacidad_mochila)
print("\nBeneficios: ", beneficios)
print("Pesos: ", pesos, "\n")

for row in mochila:
    for col in row:
      print(col, end=" ")
    print()

print("\nBeneficio máximo: ", mochila[-1][-1])

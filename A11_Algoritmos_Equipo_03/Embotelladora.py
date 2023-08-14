"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 14 de agosto del 2023
  
  Descripción: 
    Resulta que ha llegado una nueva máquina embotelladora de refrescos, 
    el contenedor principal de la máquina tiene forma cilíndrica. 

    Se sabe que cada envase de refresco debe contener M mililitros. 
    Se desea saber cuántos refrescos puede llenar la máquina de una sola vez, sin recargar el contenedor. 
    Solo se tienen los datos del radio de la base y la altura medidos en metros.
"""

# Librería para generar números aleatorios
import numpy as np
import random
from math import pi, pow

def aleatorio():
    """
      La función aleatorio retorna tres números 
      que representan los mililitros de los envases
      del refresco, el radio y altura del contenedor
    """
    a = np.random.choice([300.0, 500.0, 600.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0])
    b = round(random.uniform(0.5, 1), 2)
    c = round(random.uniform(1, 3), 2)

    return a, b, c

def calcularEnvases(capacidad, radio, altura):
    """
      La función calcularEnvases recibe tres parámetros:
      capacidad, radio y altura. 

      Retorna el número de envases de refresco que se
      pueden llenar dadas las capacidades del contenedor
    """
    volumen = (pi * (pow(radio, 2)) * altura)
    volumen *= 1000000 # Conversión de metros cúbicos a mililitros
    volumen = round(volumen, 2)

    print("Capacidad en mililitros del contenedor: ",  volumen)

    refrescos = volumen // capacidad

    return refrescos
    
capacidad = float(input("Capacidad de un envase (mililitros): "))

print("\nDatos del contenedor principal (metros)")

radio = float(input("Radio: "))
altura = float(input("Altura: "))
print()

print("La cantidad de botellas que se pueden llenar son ", calcularEnvases(capacidad, radio, altura))

for i in range(4):  # Casos prueba aleatorios
    capacidad, radio, altura = aleatorio()
    print("\nCapacidad de un envase (mililitros): ", capacidad)
    print("Radio: ", radio)
    print("Altura: ", altura)
    print("La cantidad de botellas que se pueden llenar son ", calcularEnvases(capacidad, radio, altura), end="\n\n")

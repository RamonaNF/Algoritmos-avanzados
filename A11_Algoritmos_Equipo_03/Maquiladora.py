"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 14 de agosto del 2023
  
  Descripción: 
    En una maquila, un supervisor de producción registra la cantidad de producto terminado 
    (camisas) que cada línea de producción genera durante un día completo de trabajo. 

    Se tienen 2 líneas de producción que, por diversas razones, 
    no necesariamente producen la misma cantidad diaria del producto.

    Se desea tener un programa que permita saber en cuantos días es posible surtir un pedido de N camisas. 
    Con la intención de mejorar la planeación de los tiempos de entrega y de los insumos necesarios
    para producirlas ya que últimamente se han registrado retrasos en los tiempos de entrega.
"""

# Librería para generar números aleatorios
from random import randint

def aleatorio():
    """
      La función aleatorio retorna dos números 
      aleatorios entre 5 y 50
    """
    a = randint(5, 50)
    b = randint(5, 50)

    return a, b

def calcularDias(camisas):
    """
      La función calcularDias(camisas) recibe un parámetro entero 
      que representa el número de camisas a producir

      Retorna el número de días necesarios para completar la entrega
    """
    dias = 0
    produccion1 = []
    produccion2 = []
    
    while camisas > 0:
        linea1, linea2 = aleatorio()
        
        produccion1.append(linea1)
        produccion2.append(linea2)

        camisas -= (linea1 + linea2) 
        dias += 1
        
    print("Producción línea 1: ", produccion1)
    print("Producción línea 2: ", produccion2)
        
    return dias
    

print("Ejecutando programa interactivo...\n")

camisas = int(input("Camisas a entregar: "))
print()

print("Se requirieron ", calcularDias(camisas), " días para realizar la entrega\n")

print("\nEjecutando casos prueba...\n")

for i in range(4): # Casos prueba aleatorios
    camisasPrueba = randint(10, 1000)
    print("Camisas a entregar: ", camisasPrueba)
    print("Se requirieron ", calcularDias(camisasPrueba), " días para realizar la entrega\n")

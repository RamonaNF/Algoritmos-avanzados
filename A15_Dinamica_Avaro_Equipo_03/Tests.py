"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 03 de septiembre del 2023
  
  Descripción: Archivo de prueba para las implementaciones de cambio de monedas.
  
"""

from CambioMonedas_Avaro import greedy_change as g_change
from CambioMonedas_Dinamica import dp_change

import os
import platform

flag = 's'

while flag == 's':
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    n = int( input("Ingresa la cantidad de deniminaciones de moneda que tienes: ") )
    monedas = []

    for i in range(n):
        moneda = int( input("Ingresa el valor de la moneda: ") )
        monedas.append(moneda)

    costo = int( input("Ingresa el costo total del producto: ") )
    dinero = int( input("Ingresa la cantidad con la que pago el cliente: ") )

    print()
    print("-- Algoritmo Greedy --")

    resultado = g_change(monedas, costo, dinero)
    aux = 0
    
    if resultado != None:
        for key in resultado.keys():
            print("Monedas de ", key, " ---> ", resultado[key])
            aux += key * resultado[key]

    if aux != dinero - costo:
        print("Faltó entregar ", (dinero - costo) - aux) 
    print()

    print("-- Algoritmo DP --")

    resultado = dp_change(monedas, costo, dinero)

    aux = 0
    if resultado != None:
        for key in resultado.keys():
            print("Monedas de ", key, " ---> ", resultado[key])
            aux += key * resultado[key]
    
    if aux != dinero - costo:
        print("Faltó entregar ", (dinero - costo) - aux) 
    
    print()
    
    flag  = input("Quieres realizar otro cálculo (s/n): ")

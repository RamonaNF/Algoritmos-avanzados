"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 25 de agosto del 2023
  
  Descripción: 
    
"""

def split(ini: int, fin: int) -> list: 
    """ La función split recibe como parametros
    limite inferior y un limite superior y 
    obtiene el numero medio"""
    
    return (ini + fin) // 2 


def merge(arr: list, ini: int, mid: int, fin : int) -> None:
    """ La función merge ordena los subarreglos de menor a
      mayor y los vuelve a unir"""
      
    helper = []
    
    i = ini
    j = mid + 1
  
    while i < mid + 1 and j < fin + 1:
        if arr[i] < arr[j]:
            helper.append(arr[i])
            i += 1
        else:
            helper.append(arr[j])
            j += 1
        
    if i < mid + 1:
        helper += arr[i: mid + 1]
    
    if j < fin + 1:
        helper += arr[j: fin + 1]

    arr[ini : fin  + 1] = helper


def mergeSort(arr: list, ini: int, fin: int) -> None: 
    
    if ini < fin:
        mid = split(ini, fin)

        mergeSort(arr, ini, mid)
        mergeSort(arr, mid + 1, fin)
        merge(arr, ini, mid, fin)


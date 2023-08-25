"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 25 de agosto del 2023
  
  Descripción: 
    
"""

def split(arr: list) -> list: 
  """ La función  split divide el arrelgo en dos subarreglos
      y posteriormente regresa esos dos subarreglos"""
  
  mid = len(arr) // 2
  
  return mid


def merge(arr: list, arr1: list, arr2: list, mid : int) -> None:
  """ La función merge ordena los subarreglos de menor a
      mayor y los vuelve a unir"""
  helper = []

  i = 0
  j = 0
  
  while i < len(arr1) and j < len(arr2):
      if arr1[i] < arr2[j]:
          helper.append(arr1[i])
          i += 1
      else:
          helper.append(arr2[j])
          j += 1
    
  if i < len(arr1):
      helper += arr1[i:]
  
  if j < len(arr2):
      helper += arr2[j:]

  arr[mid - len(arr1) : mid + len(arr2)] = helper


def mergeSort(arr : list) -> None: 
  if len(arr) == 0:
      return
  
  if len(arr) == 1:
      return
  
  mid = split(arr)
  arr1 = arr[ : mid]
  arr2 = arr[mid : ]
  
  mergeSort(arr1)
  mergeSort(arr2)

  merge(arr, arr1, arr2, mid)

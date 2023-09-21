"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 21 de septiembre del 2023
  
  Descripción: Hashing strings.

  Complejidad: O( N )
  
"""

file = input("Por favor ingresa el archivo de texto: ") # datos.txt
n = int(input ("Ingresa el número de columnas: ")) # Múltiplo de 4 (16 <= n <= 64)

SPACE = '?'
NEW_LINE = '-'
MISSING = '$' #§

matrix = []

def put_on_matrix(li : list, c : str, i: int) -> None:
    if c == ' ':
        li[i] = SPACE
    
    elif c == '\n':
        li[i] = NEW_LINE
    
    else:
        li[i] = c


with open(file, 'r') as input_file:
    i = 0
    aux = [MISSING] * n
    
    for linea in input_file:
        for char in linea:
            put_on_matrix(aux, char, i)

            if i == n - 1:
                matrix.append(aux)
                aux = [MISSING] * n 
                i = -1
            
            i += 1

    if i != 0:
        matrix.append(aux)


print("\nMatriz generada")        
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()


ascii_sum = [0] * n

for row in matrix:
    for j, char in enumerate(row):
        if char == SPACE: 
            ascii_sum[j] += 32
            
        elif char == NEW_LINE:
            ascii_sum[j] += 10
        
        else:
            ascii_sum[j] += ord(char)


ascii_sum = [total % 256 for total in ascii_sum]
print("\nSuma de las columnas módulo 256")
print(ascii_sum)


hex_values = [hex(total).upper()[2:] for total in ascii_sum]
hashed = []

for i in range(0, len(hex_values), 4):
    group = ""
    
    for j in range(4):
        group += hex_values[i + j]
    
    hashed.append(group)


print("\nRepresentación hexadecimal")
print(hashed)

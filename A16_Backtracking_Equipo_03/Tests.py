"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 10 de septiembre del 2023
  
  Descripción: Archivo de prueba para -------------------------.
  
"""
import sys
from Maze import back_tracking as maze_solver1
from Maze import ramificacion_y_poda as maze_solver2

n = 0
m = 0
i = 0
mapa = []
flag = False

with open("inputs/input7.txt", 'r') as maze:

    for linea in maze:
        if not flag:
            try:
                n, m = [int(num) for num in linea.strip().split(" ")]
            
            except ValueError:
                print("Caracter no válido")

            flag = True

        else:
            mapa.append([])
            num = None

            try:
                for num in linea.strip().split(" "):
                    num = int(num)

                    if num != 0 and num != 1:
                        raise ValueError

                    else:
                        mapa[i].append(num)
            
            except ValueError:
                print("Caracter no válido: ", num)
                sys.exit(1)

            if len(mapa[i]) != m:
                print("Las dimensiones dadas son erróneas")
                sys.exit(1)
    
            i += 1


if len(mapa) is not n:
    print("Las dimensiones dadas son erróneas")
    sys.exit(1)


print("--- Mapa ---")
for row in mapa:
    for col in row:
        print(col, end= " ")
    print()


camino = maze_solver1(mapa, (len(mapa) - 1, len(mapa[0]) - 1))
print("\n--- Solución Backtracking ---")

if camino[n - 1][m - 1] == 0:
    print("No hay camino")
    sys.exit(1)

for row in camino:
    for col in row:
        if col // 10 > 0:
            print(col, end= " ")
        else:
            print(col, end= "  ")
    print()


camino = maze_solver2(mapa, (len(mapa) - 1, len(mapa[0]) - 1))
print("\n--- Solución Ramificacion y Poda ---")

if camino[n - 1][m - 1] == 0:
    print("No hay camino", camino)
    sys.exit(1)

for row in camino:
    for col in row:
        if col // 10 > 0:
            print(col, end= " ")
        else:
            print(col, end= "  ")
    print()

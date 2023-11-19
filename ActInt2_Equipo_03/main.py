from Graph import Wgraph
from MST import MST
from Flujo_maximo import max_flow as max_flow_func

nodos = 0
graphList = []
flujos = []
flag = 0

with open ("inputs/input0.txt", 'r') as info:
    for linea in info:
        if flag == 0:
            nodos = int(linea.strip())
            flag = flag + 1

        elif flag == 1:
            graphList.append([int(num) for num in linea.strip().split(' ')])
            if len(graphList) == nodos:
                flag = flag + 1

        elif flag == 2:
            flujos.append([int(num) for num in linea.strip().split(' ')])


print("MSP connections")
for row in graphList:
    print(row)
print("\n")

print(MST(graphList))


print("\nFlujos")

for row in flujos:
    print(row)
print("\n")

max_flow = Wgraph(True)
for i in range(len(flujos)):
    for j in range(len(flujos[i])):
        if flujos[i][j]:
            max_flow.add_mutable_edge(chr(ord('A') + i), chr(ord('A') + j), flujos[i][j])

print(max_flow_func(max_flow, 'A', chr(ord('A') + len(flujos)-1)))

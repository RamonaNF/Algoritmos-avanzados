from Graph import Wgraph
from MST import MST

""" #isCycled tests
grafo.add_edge('A', 'B', 0)
grafo.add_edge('A', 'C', 0)
grafo.add_edge('E', 'B', 0)
grafo.add_edge('E', 'D', 0)
grafo.add_edge('D', 'B', 0)

print(isCycled(grafo, ('A', 0)))
"""

nodos = 0
graphList = []
flag = False

with open ("inputs/input0.txt", 'r') as info:
    for linea in info:
        if not flag:
            nodos = int(linea.strip())
            flag = True

        else:
            graphList.append([int(num) for num in linea.strip().split(' ')])


for row in graphList:
    print(row)
print("\n")


minimum_spanning_tree = MST(graphList)
print(minimum_spanning_tree)
print()

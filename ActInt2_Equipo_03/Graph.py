"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 18 de noviembre del 2023
  
  Descripción: Clase para un grafo con peso.
  
"""

class Wgraph:
    def __init__(self, direction : bool) -> None:
        self.__direction = direction
        self.__vertexes = set()
        self.__edges = {}

    def contains_vertex (self, vertex) -> bool:
        return vertex in self.__vertexes
    
    def add_edge (self, origin, destiny, cost) -> None:
        if origin not in self.__vertexes:
            self.__vertexes.add(origin)
            self.__edges[origin] = set()
        
        if destiny not in self.__vertexes:
            self.__vertexes.add(destiny)
            self.__edges[destiny] = set()

        self.__edges[origin].add((destiny, cost))
        self.__edges[destiny].add((origin, cost))


    def get_connections_from(self, vertex) -> set :
        return self.__edges[vertex]
    
    def get_vertexes(self) -> int:
        return self.__vertexes
    
    def delete_connection(self, first_node, second_node, cost) -> None:
        self.__edges[first_node].remove((second_node, cost))
        self.__edges[second_node].remove((first_node, cost))


    def __str__(self) -> str:
        string = "Grafo\n"
        for key in self.__edges.keys():
            string += str(key) + ": "
            string += str(self.__edges[key]) + '\n'
            
        return string


class Ugraph:
    def __init__(self, direction : bool) -> None:
        self.__direction = direction
        self.__vertexes = set()
        self.__edges = {}

    def contains_vertex (self, vertex) -> bool:
        return vertex in self.__vertexes
    
    def add_edge (self, origin, destiny) -> None:
        if origin not in self.__vertexes:
            self.__vertexes.add(origin)
            self.__edges[origin] = set()
        
        if destiny not in self.__vertexes:
            self.__vertexes.add(destiny)
            self.__edges[destiny] = set()

        self.__edges[origin].add(destiny)
        self.__edges[destiny].add(origin)


    def get_connections_from(self, vertex) -> set :
        return self.__edges[vertex]
    
    def get_vertexes(self) -> int:
        return self.__vertexes
    

    def __str__(self) -> str:
        string = "Grafo\n"
        for key in self.__edges.keys():
            string += str(key) + ": "
            string += str(self.__edges[key]) + '\n'
            
        return string

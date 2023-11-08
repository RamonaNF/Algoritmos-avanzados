"""
  Autores: José Armando Rosas Balderas, a01704132@tec.mx
           Diego Perdomo Salcedo, a01709150@tec.mx
           Ramona Najera Fuentes, a01423596@tec.mx

  Creación: 06 de noviembre del 2023
  
  Descripción: Clase para un grafo sin peso.
  
"""

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

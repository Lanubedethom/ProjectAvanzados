"""
dijkstra.py

Autores:
Ian Logan Will Quispe Ventura 211359
Jhon Esau Pumachoque Choquenaira 210940
Ciro Gabriel Callapi˜na Castilla 134403
Luis Manuel Tinoco Ccoto 204807
Jorge Enrique Zegarra Rojas 161534

"""

import sys


class Vertex:
    """
    Clase que representa un vertice en un grafo.
    Key: int, La clave unica que identifica al vertice.
    D: int, La distancia minima desde el vertice de origen en el algoritmo de Dijkstra.
    Pi: Vertex, El vertice predecesor en el camino mas corto desde el vertice de origen.
    """
    def __init__(self, key):
        self.key = key
        self.d = sys.maxsize
        self.pi = None


class Edge:
    """
    Clase que representa una arista en un grafo.
    src: Vertex, El vertice de origen de la arista.
    dest: Vertex, El vertice de destino de la arista.
    weight: int, El peso de la arista.
    """

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, key):
        self.vertices.append(Vertex(key))

    def add_edge(self, src_key, dest_key, weight):
        src = self.find_vertex(src_key)
        dest = self.find_vertex(dest_key)
        self.edges.append(Edge(src, dest, weight))

    def find_vertex(self, key):
        for v in self.vertices:
            if v.key == key:
                return v
        return None


def initialize_single_source(graph, source):
    """
      Inicializa las distancias y predecesores de los vertices para el algoritmo de Dijkstra.
      :param graph: El grafo en el que se va a ejecutar el algoritmo.
      :param source: El vertice de origen.
    """

    for v in graph.vertices:
        v.d = sys.maxsize
        v.pi = None
    source.d = 0


def relax(u, v, weight):
    """
        Relaja una arista en el algoritmo de Dijkstra.
        :param u: El vertice de origen de la arista.
        :param v: El vertice de destino de la arista.
        :param weight: El peso de la arista.
    """

    if v.d > u.d + weight:
        v.d = u.d + weight
        v.pi = u


def dijkstra(graph, source):
    """
     Ejecuta el algoritmo de Dijkstra en un grafo.
     :param graph: El grafo en el que se va a ejecutar el algoritmo.
     :param source: El vertice de origen.
    """

    initialize_single_source(graph, source)
    q = [(v.d, v) for v in graph.vertices]
    q = sorted(q, key=lambda x: x[0])

    while q:
        u_d, u = q.pop(0)
        for edge in graph.edges:
            if edge.src == u:
                relax(u, edge.dest, edge.weight)
                q = sorted(q, key=lambda x: x[0])


if __name__ == "__main__":
    graph = Graph()

    for i in range(5):
        graph.add_vertex(i)

    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 1, 3)
    graph.add_edge(2, 3, 9)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 4)
    graph.add_edge(4, 3, 6)
    graph.add_edge(4, 0, 7)

    source = graph.find_vertex(0)
    dijkstra(graph, source)

    for v in graph.vertices:
        print(f"Vertex: {v.key}, Distance: {v.d}, Predecessor: {v.pi.key if v.pi else 'None'}")

import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.d = sys.maxsize
        self.pi = None


class Edge:
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
    for v in graph.vertices:
        v.d = sys.maxsize
        v.pi = None
    source.d = 0


def relax(u, v, weight):
    if v.d > u.d + weight:
        v.d = u.d + weight
        v.pi = u


def dijkstra(graph, source):
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

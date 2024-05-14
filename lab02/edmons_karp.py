from collections import deque

class Edge:
    def __init__(self, to, capacity, flow):
        self.to = to
        self.capacity = capacity
        self.flow = flow

def addEdge(graph, u, v, capacity):
    graph[u].append(Edge(v, capacity, 0))

def bfs(graph, parent, source, sink):
    n = len(graph)
    visited = [False] * n
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()

        for e in graph[u]:
            v = e.to
            if not visited[v] and e.capacity - e.flow > 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)

    return visited[sink]

def edmondsKarp(graph, source, sink):
    n = len(graph)
    parent = [-1] * n
    maxFlow = 0

    while bfs(graph, parent, source, sink):
        pathFlow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            for e in graph[u]:
                if e.to == v:
                    pathFlow = min(pathFlow, e.capacity - e.flow)
                    break
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            for e in graph[u]:
                if e.to == v:
                    e.flow += pathFlow
                    for backEdge in graph[v]:
                        if backEdge.to == u:
                            backEdge.flow -= pathFlow
                            break
                    break
            v = parent[v]

        maxFlow += pathFlow

    return maxFlow


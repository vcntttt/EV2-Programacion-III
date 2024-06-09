from nodo import NodoGrafo

class Edge: # Edge == Arista
    def __init__(self, nodo1, nodo2):
        # V1 Y V2 son los extremos de la arista
        self.v1 = nodo1
        self.v2 = nodo2

    def getV1(self):
        return self.v1
    
    def getV2(self):
        return self.v2
    
    def __str__(self):
        return self.v1.getInfo() + " -> " + self.v2.getInfo()
    
class Grafo: # Grafo dirigido
    def __init__(self):
        self.dict = {}

    def addVertice(self, vertice): # Vertice == Nodo
        if vertice not in self.dict:
            self.dict[vertice] = []

    def addEdge(self, edge):
        v1 = edge.getV1()
        v2 = edge.getV2()

        if v1 not in self.dict:
            raise ValueError(f"{v1.getInfo()} no existe en el grafo")
        if v2 not in self.dict:
            raise ValueError(f"{v2.getInfo()} no existe en el grafo")
        if v2 not in self.dict[v1]:
            self.dict[v1].append(v2)

    def getVertice(self, info):
        for v in self.dict:
            if v.getInfo() == info: 
                return v
        return None

    def getVecinos(self, vertice):
        return self.dict[vertice]
    
    def __str__(self):
        allEdges = ''
        for v1 in self.dict:
            for v2 in self.dict[v1]:
                allEdges += v1.getInfo() + " -> " + v2.getInfo() + "\n"
        return allEdges
    
    def findPath(self, start, end): # Algoritmo de dijkstra
        distancias = {vertice: float('infinity') for vertice in self.dict}
        distancias[start] = 0
        previos = {vertice: None for vertice in self.dict}
        vertices = list(self.dict.keys())

        while vertices:
            actual = min(vertices, key=lambda vertice: distancias[vertice])
            vertices.remove(actual)
            if distancias[actual] == float('infinity'):
                break

            for vecino in self.getVecinos(actual):
                alt = distancias[actual] + 1
                if alt < distancias[vecino]:
                    distancias[vecino] = alt
                    previos[vecino] = actual

        camino, actual = [], end
        while previos[actual] is not None:
            camino.insert(0, actual)
            actual = previos[actual]
        if camino:
            camino.insert(0,actual)
        return camino if camino else None
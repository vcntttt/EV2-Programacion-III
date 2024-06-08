class Nodo:
    def __init__(self, nombre):
        self.info = nombre
        self.next = None

class Edge:
    def __init__(self, nodo1, nodo2):
        self.nodo1 = nodo1
        self.nodo2 = nodo2

class Grafo: # Grafo dirigido
    def __init__(self):
        self.dict = {}

    def addVertice(self, vertice): # Vertice == Nodo
        if vertice in self.dict:
            return "Vertice ya existe"
        else:
            self.dict[vertice] = []

    def addEdge(self, vertice1, vertice2): # Edge == Arista
        pass

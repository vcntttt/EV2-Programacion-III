class NodoGrafo:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def getInfo(self):
        return self.info

class NodoBST:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None
        
class nodeAVL:
    def __init__(self, curso):
        self.curso = curso
        self.izquierda = None
        self.derecha = None
        self.altura = 0

class NodoGrafo:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def getInfo(self):
        return self.info

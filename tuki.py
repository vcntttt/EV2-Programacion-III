class NodoAVL:
    def __init__(self, clave, curso):
        self.clave = clave
        self.curso = curso
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, raiz, clave, curso):
        if not raiz:
            return NodoAVL(clave, curso)
        elif clave < raiz.clave:
            raiz.izquierda = self.insertar(raiz.izquierda, clave, curso)
        else:
            raiz.derecha = self.insertar(raiz.derecha, clave, curso)

        raiz.altura = 1 + max(self.get_altura(raiz.izquierda), self.get_altura(raiz.derecha))

        balance = self.get_balance(raiz)

        if balance > 1 and clave < raiz.izquierda.clave:
            return self.rotar_derecha(raiz)
        if balance < -1 and clave > raiz.derecha.clave:
            return self.rotar_izquierda(raiz)
        if balance > 1 and clave > raiz.izquierda.clave:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and clave < raiz.derecha.clave:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def get_balance(self, nodo):
        if not nodo:
            return 0
        return self.get_altura(nodo.izquierda) - self.get_altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        z.altura = 1 + max(self.get_altura(z.izquierda), self.get_altura(z.derecha))
        y.altura = 1 + max(self.get_altura(y.izquierda), self.get_altura(y.derecha))
        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self.get_altura(z.izquierda), self.get_altura(z.derecha))
        y.altura = 1 + max(self.get_altura(y.izquierda), self.get_altura(y.derecha))
        return y

    def preorden(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.clave), end="")
        self.preorden(raiz.izquierda)
        self.preorden(raiz.derecha)

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_curso(self, curso):
        if curso not in self.grafo:
            self.grafo[curso] = []

    def agregar_dependencia(self, curso_pre, curso_post):
        if curso_pre in self.grafo and curso_post in self.grafo:
            if curso_post not in self.grafo[curso_pre]:
                self.grafo[curso_pre].append(curso_post)

    def imprimir_grafo(self):
        for curso in self.grafo:
            print(f"{curso} -> {self.grafo[curso]}")

    def encontrar_camino_corto(self, inicio, fin, camino=[]):
        camino = camino + [inicio]
        if inicio == fin:
            return camino
        if inicio not in self.grafo:
            return None
        camino_corto = None
        for nodo in self.grafo[inicio]:
            if nodo not in camino:
                nuevo_camino = self.encontrar_camino_corto(nodo, fin, camino)
                if nuevo_camino:
                    if not camino_corto or len(nuevo_camino) < len(camino_corto):
                        camino_corto = nuevo_camino
        return camino_corto


# Ejemplo de uso de Árbol AVL
avl = ArbolAVL()
raiz = None
raiz = avl.insertar(raiz, 10, "Curso A")
raiz = avl.insertar(raiz, 20, "Curso B")
raiz = avl.insertar(raiz, 5, "Curso C")

print("Preorden del Árbol AVL:")
avl.preorden(raiz)

# Ejemplo de uso de Grafo
grafo = Grafo()
grafo.agregar_curso("Curso A")
grafo.agregar_curso("Curso B")
grafo.agregar_curso("Curso C")
grafo.agregar_dependencia("Curso A", "Curso B")
grafo.agregar_dependencia("Curso B", "Curso C")

print("\nGrafo de dependencias:")
grafo.imprimir_grafo()

camino = grafo.encontrar_camino_corto("Curso A", "Curso C")
print(f"\nCamino más corto de Curso A a Curso C: {camino}")

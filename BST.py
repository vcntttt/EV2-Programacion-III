from nodo import NodoBST

class Estudiante:
    def __init__(self, matricula, nombre):
        self.matricula = matricula
        self.nombre = nombre


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, estudiante):
        if self.raiz is None:
            self.raiz = NodoBST(estudiante)
        else:
            self._insertar(self.raiz, estudiante)

    def _insertar(self, nodo, estudiante):
        if estudiante.matricula < nodo.estudiante.matricula:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(estudiante)
            else:
                self._insertar(nodo.izquierda, estudiante)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(estudiante)
            else:
                self._insertar(nodo.derecha, estudiante)

    def buscar(self, matricula):
        return self._buscar(self.raiz, matricula)

    def _buscar(self, nodo, matricula):
        if nodo is None or nodo.estudiante.matricula == matricula:
            return nodo
        if matricula < nodo.estudiante.matricula:
            return self._buscar(nodo.izquierda, matricula)
        else:
            return self._buscar(nodo.derecha, matricula)

    def eliminar(self, matricula):
        self.raiz, _ = self._eliminar(self.raiz, matricula)

    def _eliminar(self, nodo, matricula):
        if nodo is None:
            return nodo, None

        if matricula < nodo.estudiante.matricula:
            nodo.izquierda, eliminado = self._eliminar(nodo.izquierda, matricula)
        elif matricula > nodo.estudiante.matricula:
            nodo.derecha, eliminado = self._eliminar(nodo.derecha, matricula)
        else:
            eliminado = nodo
            if nodo.izquierda is None:
                return nodo.derecha, eliminado
            elif nodo.derecha is None:
                return nodo.izquierda, eliminado

            temp = self._minimo(nodo.derecha)
            nodo.estudiante = temp.estudiante
            nodo.derecha, _ = self._eliminar(nodo.derecha, temp.estudiante.matricula)

        return nodo, eliminado

    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

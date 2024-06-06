class NodoArbol:
    def __init__(self, matricula, info_estudiante):
        self.matricula = matricula  # Número de matrícula del estudiante
        self.info_estudiante = info_estudiante  # Información del estudiante
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, matricula, info_estudiante):
        if self.raiz is None:
            self.raiz = NodoArbol(matricula, info_estudiante)
        else:
            self._insertar(self.raiz, matricula, info_estudiante)

    def _insertar(self, nodo, matricula, info_estudiante):
        if matricula < nodo.matricula:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(matricula, info_estudiante)
            else:
                self._insertar(nodo.izquierdo, matricula, info_estudiante)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(matricula, info_estudiante)
            else:
                self._insertar(nodo.derecho, matricula, info_estudiante)

    def buscar(self, matricula):
        return self._buscar(self.raiz, matricula)

    def _buscar(self, nodo, matricula):
        if nodo is None or nodo.matricula == matricula:
            return nodo
        if matricula < nodo.matricula:
            return self._buscar(nodo.izquierdo, matricula)
        else:
            return self._buscar(nodo.derecho, matricula)

    def eliminar(self, matricula):
        self.raiz, _ = self._eliminar(self.raiz, matricula)

    def _eliminar(self, nodo, matricula):
        if nodo is None:
            return nodo, None

        if matricula < nodo.matricula:
            nodo.izquierdo, eliminado = self._eliminar(nodo.izquierdo, matricula)
        elif matricula > nodo.matricula:
            nodo.derecho, eliminado = self._eliminar(nodo.derecho, matricula)
        else:
            eliminado = nodo
            if nodo.izquierdo is None:
                return nodo.derecho, eliminado
            elif nodo.derecho is None:
                return nodo.izquierdo, eliminado

            temp = self._minimo(nodo.derecho)
            nodo.matricula = temp.matricula
            nodo.info_estudiante = temp.info_estudiante
            nodo.derecho, _ = self._eliminar(nodo.derecho, temp.matricula)

        return nodo, eliminado

    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    

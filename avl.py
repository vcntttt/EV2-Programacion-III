class Curso:
    def __init__(self, nombre, requisitos, codigo, descripcion, semestre):
        self.nombre = nombre
        self.codigo = codigo
        self.requisitos = requisitos
        self.descripcion = descripcion
        self.semestre = semestre

    def getName(self):
        return self.nombre

    def getCode(self):
        return self.codigo 

    def getRequirements(self):
        return self.requisitos

    def getDescription(self):
        return self.descripcion
    
    def getSemestre(self):
        return self.semestre

    def setName(self, name):
        self.nombre = name

    def setCode(self, code):
        self.codigo = code

    def setRequirements(self, requirements):
        self.requisitos = requirements

    def setDescription(self, description):
        self.descripcion = description

class nodeAVL:
    def __init__(self, curso):
        self.curso = curso
        self.izquierda = None
        self.derecha = None
        self.altura = 0

class AVL:
    def __init__(self):
        self.root = None

    def minNodo(nodo):
        aux = nodo
        while aux.left is not None:
            aux = aux.left
        return aux

    def getAltura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def getBalance(self, nodo):
        if not nodo:
            return 0
        return self.getAltura(nodo.izquierda) - self.getAltura(nodo.derecha)
    
    def rotacionDere(self, nodo):
        Iz = nodo.izquierda
        De = Iz.derecha
        Iz.derecha = nodo
        nodo.izquierda = De

        nodo.altura = 1 + max(self.getAltura(nodo.izquierda), self.getAltura(nodo.derecha))
        Iz.altura = 1 + max(self.getAltura(Iz.izquierda), self.getAltura(Iz.derecha))
        return Iz
    
    def rotacionIzqui(self, nodo):
        De = nodo.derecha
        Iz = De.izquierda
        De.izquierda = nodo
        nodo.derecha = Iz

        nodo.altura = 1 + max(self.getAltura(nodo.izquierda), self.getAltura(nodo.derecha))
        De.altura = 1 + max(self.getAltura(De.izquierda), self.getAltura(De.derecha))
        return De
    
    def insertar(self, nodo, curso):
        if not nodo:
            return nodeAVL(curso)
        
        if curso.codigo < nodo.curso.codigo:
            nodo.izquierda = self.insertar(nodo.izquierda, curso)
        else:
            nodo.derecha = self.insertar(nodo.derecha, curso)

        nodo.altura = 1 + max(self.getAltura(nodo.izquierda), self.getAltura(nodo.derecha))
        balance = self.getBalance(nodo)

        if balance > 1 and curso.codigo < nodo.izquierda.curso.codigo:
            return self.rotacionDere(nodo)
        
        if balance < -1 and curso.codigo > nodo.derecha.curso.codigo:
            return self.rotacionIzqui(nodo)
        
        if balance > 1 and curso.codigo > nodo.izquierda.curso.codigo:
            nodo.izquierda = self.rotacionIzqui(nodo.izquierda)
            return self.rotacionDere(nodo)
        
        if balance < -1 and curso.codigo < nodo.derecha.curso.codigo:
            nodo.derecha = self.rotacionDere(nodo.derecha)
            return self.rotacionIzqui(nodo)
        
        return nodo
    
    def eliminar(self, nodo, curso):
        if not nodo:
            return nodo
        
        if curso.codigo < nodo.curso.codigo:
            nodo.izquierda = self.eliminar(nodo.izquierda, curso)
        elif curso.codigo > nodo.curso.codigo:
            nodo.derecha = self.eliminar(nodo.derecha, curso)
        else:
            if nodo.izquierda is None:
                aux = nodo.derecha
                node = None
                return aux
            elif nodo.derecha is None:
                aux = nodo.izquierda
                nodo = None
                return aux
            
            aux = self.minNodo(nodo.derecha)
            nodo.curso = aux.curso
            nodo.derecha = self.eliminar(nodo.derecha, aux.curso)

        if nodo is None:
            return nodo
        
        nodo.altura = 1 + max(self.getAltura(nodo.izquierda), self.getAltura(nodo.derecha))
        balance = self.getBalance(nodo)

        if balance > 1 and self.getBalance(nodo.izquierda) >= 0:
            return self.rotacionDere(nodo)
        
        if balance > 1 and self.getBalance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotacionIzqui(nodo.izquierda)
            return self.rotacionDere(nodo)
        
        if balance < -1 and self.getBalance(nodo.derecha) <= 0:
            return self.rotacionIzqui(nodo)
        
        if balance < -1 and self.getBalance(nodo.derecha) > 0:
            nodo.derecha = self.rotacionDere(nodo.derecha)
            return self.rotacionIzqui(nodo)
        
        return nodo
    
    def anadirCurso(self, curso):
        self.root = self.insertar(self.root, curso)

    def buscar(self, nodo, codigo):
        if nodo is None or nodo.curso.codigo == codigo:
            return nodo

        if codigo < nodo.curso.codigo:
            return self.buscar(nodo.izquierda, codigo)
        return self.buscar(nodo.derecha, codigo)

    def encontrarCurso(self, codigo):
        return self.buscar(self.root, codigo)
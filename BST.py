class NodoArbol:
    def __init__(self, matricula, info_estudiante):
        self.matricula = matricula  # Número de matrícula del estudiante
        self.info_estudiante = info_estudiante  # Información del estudiante
        self.izquierdo = None
        self.derecho = None


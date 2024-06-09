import tkinter as tk
from tkinter import ttk
from avl import AVL
from grafo import Grafo

class Interfaz():
    def __init__(self, root):
        self.root = root
        self.root.title("6 - Sistema de Administración Escolar")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        # self.bst = BST()
        self.avl = AVL()
        self.graph = Grafo()

        self.setup_ui()

    def addCourse(self):
        pass

    def setup_ui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, padx=10)

        self.student_tab = tk.Frame(self.notebook)
        self.course_tab = tk.Frame(self.notebook)
        self.dependency_tab = tk.Frame(self.notebook)

        self.notebook.add(self.student_tab, text="Estudiantes")
        self.notebook.add(self.course_tab, text="Cursos")
        self.notebook.add(self.dependency_tab, text="Dependencias")

        self.setup_student_ui(self.student_tab)
        self.setup_course_ui(self.course_tab)
        self.setup_dependency_ui(self.dependency_tab)

    def setup_student_ui(self, parent_frame):
        frame = tk.LabelFrame(
            parent_frame, text="Gestión de Estudiantes", padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        self.student_id_entry = tk.Entry(frame)
        self.student_id_entry.grid(row=0, column=1)
        self.student_name_entry = tk.Entry(frame)
        self.student_name_entry.grid(row=1, column=1)

        tk.Label(frame, text="ID del Estudiante").grid(row=0, column=0)
        tk.Label(frame, text="Nombre del Estudiante").grid(row=1, column=0)

        # tk.Button(frame, text="Agregar Estudiante",
        #           command=self.add_student).grid(row=2, column=0)
        # tk.Button(frame, text="Buscar Estudiante",
        #           command=self.search_student).grid(row=2, column=1)
        # tk.Button(frame, text="Eliminar Estudiante",
        #           command=self.delete_student).grid(row=2, column=2)

    def setup_course_ui(self, parent_frame):
        frame = tk.LabelFrame(
            parent_frame, text="Gestión de Cursos", padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        self.course_id_entry = tk.Entry(frame)
        self.course_id_entry.grid(row=0, column=1)
        self.course_name_entry = tk.Entry(frame)
        self.course_name_entry.grid(row=1, column=1)
        self.course_dependencies_entry = tk.Entry(frame)
        self.course_dependencies_entry.grid(row=2, column=1)

        tk.Label(frame, text="ID del Curso").grid(row=0, column=0)
        tk.Label(frame, text="Nombre del Curso").grid(row=1, column=0)
        tk.Label(frame, text="Curso Requerido").grid(row=2, column=0) # Nombre del curso requerido

        tk.Button(frame, text="Agregar Curso",
                  command=self.addCourse).grid(row=3, column=0)
        # tk.Button(frame, text="Buscar Curso",
        #           command=self.search_course).grid(row=2, column=1)

    def setup_dependency_ui(self, parent_frame):
        frame = tk.LabelFrame(
            parent_frame, text="Gestión de Dependencias", padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Curso Prerrequisito").grid(
            row=0, column=0, sticky="w")
        tk.Label(frame, text="Curso Dependiente").grid(
            row=1, column=0, sticky="w")
        self.course1_entry = tk.Entry(frame)
        self.course1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.course2_entry = tk.Entry(frame)
        self.course2_entry.grid(row=1, column=1, padx=5, pady=5)

        # tk.Button(frame, text="Agregar Dependencia",
        #           command=self.add_dependency).grid(row=2, column=0)
        # tk.Button(frame, text="Encontrar Ruta",
        #           command=self.find_path).grid(row=2, column=1)


root = tk.Tk()
app = Interfaz(root)
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from avl import AVL, Curso
from grafo import Grafo, Edge
from nodo import NodoGrafo
from BST import BST, Estudiante

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("6 - Sistema de Administración Escolar")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.bst = BST()
        self.avl = AVL()
        self.grafo = Grafo()
        self.setupUI()

    def addCourse(self):
        cursoID = self.course_id_entry.get()
        nombreCurso = self.course_name_entry.get()
        dependencias = self.course_dependencies_entry.get()
        dependenciasList = dependencias.split(",") if dependencias != "" else []

        if not cursoID.isdigit():
            messagebox.showerror("Error", "El ID del curso debe ser un número entero.")
            return
        
        cursoID = int(cursoID)
        if self.avl.encontrarCurso(cursoID):
            messagebox.showerror("Error", "El ID del curso ya existe.")
            return

        curso = Curso(cursoID, nombreCurso, dependenciasList)
        nodoCurso = NodoGrafo(curso.getInfo()) # nombre(codigo)

        self.avl.anadirCurso(curso)
        self.grafo.addVertice(nodoCurso)
        
        if dependenciasList:
            for d in dependenciasList:
                d = d.strip()
                nodo = self.grafo.getVertice(d)
                if nodo:
                    self.grafo.addEdge(Edge(nodo, nodoCurso))
                else:
                    messagebox.showerror("Error", f"No existe el curso {d}")
                    return
        self.actualizarCursos()
        self.actualizarDependencias()
        self.course_name_entry.delete(0, tk.END)
        self.course_id_entry.delete(0, tk.END)
        self.course_dependencies_entry.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Curso agregado")

    def buscarCurso(self):
        cursoID = self.course_id_entry.get()

        if not cursoID.isdigit():
            messagebox.showerror("Error", "El ID del curso debe ser un número entero.")
            return

        cursoID = int(cursoID)
        resultado = self.avl.encontrarCurso(cursoID)
        if resultado:
            info = f"ID: {resultado.curso.codigo}\nNombre: {resultado.curso.nombre}\nDependencias: {', '.join([dep for dep in resultado.curso.dependencias])}"
            messagebox.showinfo("Resultado", info)
        else:
            messagebox.showerror("Error", "Curso no encontrado")

    def encontrarCamino(self):
        cursoInicio = self.curso_inicio_entry.get().strip()
        cursoFin = self.curso_fin_entry.get().strip()
        nodoInicio = self.grafo.getVertice(cursoInicio)
        nodoFin = self.grafo.getVertice(cursoFin)

        if nodoInicio is None or nodoFin is None:
            messagebox.showerror("Error", "Uno o ambos cursos no existen.")
            return

        camino = self.grafo.findPath(nodoInicio, nodoFin)
        if camino:
            camino_str = " -> ".join([n.getInfo() for n in camino])
            messagebox.showinfo("Camino más corto", f"El camino más corto es: {camino_str}")
        else:
            messagebox.showinfo("Camino más corto", "No hay camino disponible entre los cursos seleccionados.")

    def setupUI(self):
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

    def setup_student_ui(self, tab):
        frame = tk.LabelFrame(tab, text="Gestión de Estudiantes", padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        self.student_id_entry = tk.Entry(frame)
        self.student_id_entry.grid(row=0, column=1)
        self.student_name_entry = tk.Entry(frame)
        self.student_name_entry.grid(row=1, column=1)

        tk.Label(frame, text="ID del Estudiante").grid(row=0, column=0)
        tk.Label(frame, text="Nombre del Estudiante").grid(row=1, column=0)

        tk.Button(frame, text="Agregar Estudiante", command=self.add_student).grid(row=2, column=0)
        tk.Button(frame, text="Buscar Estudiante", command=self.search_student).grid(row=2, column=1)
        tk.Button(frame, text="Eliminar Estudiante", command=self.delete_student).grid(row=2, column=2)

        self.treeStudents = ttk.Treeview(frame, columns=("ID", "Nombre"), show='headings')
        self.treeStudents.heading("ID", text="ID")
        self.treeStudents.heading("Nombre", text="Nombre")
        self.treeStudents.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        frame.grid_rowconfigure(3, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    def add_student(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()

        if not student_id.isdigit():
            messagebox.showerror("Error", "El ID del estudiante debe ser un número entero.")
            return

        student_id = int(student_id)

        if self.bst.buscar(student_id):
            messagebox.showerror("Error", "El ID del estudiante ya existe.")
            return

        if student_id and student_name:
            estudiante = Estudiante(student_id, student_name)
            self.bst.insertar(estudiante)
            self.treeStudents.insert("", tk.END, values=(student_id, student_name))
            self.student_id_entry.delete(0, tk.END)
            self.student_name_entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", "Estudiante agregado")
        else:
            messagebox.showerror("Error", "ID y Nombre del estudiante son requeridos")

    def search_student(self):
        student_id = self.student_id_entry.get()

        if not student_id.isdigit():
            messagebox.showerror("Error", "El ID del estudiante debe ser un número entero.")
            return

        student_id = int(student_id)
        result = self.bst.buscar(student_id)
        if result:
            messagebox.showinfo("Resultado", f"Estudiante encontrado: ID - {result.estudiante.matricula}, Nombre - {result.estudiante.nombre}")
        else:
            messagebox.showerror("Error", "Estudiante no encontrado")

    def delete_student(self):
        student_id = self.student_id_entry.get()

        if not student_id.isdigit():
            messagebox.showerror("Error", "El ID del estudiante debe ser un número entero.")
            return

        student_id = int(student_id)
        self.bst.eliminar(student_id)
        self.refresh_student_list()
        messagebox.showinfo("Éxito", "Estudiante eliminado")

    def refresh_student_list(self):
        for item in self.treeStudents.get_children():
            self.treeStudents.delete(item)
        estudiantes = self.bst.inorder()
        for estudiante in estudiantes:
            self.treeStudents.insert("", tk.END, values=(estudiante.matricula, estudiante.nombre))
        
    def setup_course_ui(self, tab):
        frame = tk.LabelFrame(tab, text="Gestión de Cursos", padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        self.course_id_entry = tk.Entry(frame)
        self.course_id_entry.grid(row=0, column=1)
        self.course_name_entry = tk.Entry(frame)
        self.course_name_entry.grid(row=1, column=1)
        self.course_dependencies_entry = tk.Entry(frame)
        self.course_dependencies_entry.grid(row=2, column=1)

        tk.Label(frame, text="ID del Curso").grid(row=0, column=0)
        tk.Label(frame, text="Nombre del Curso").grid(row=1, column=0)
        tk.Label(frame, text="Curso Requerido").grid(row=2, column=0)

        tk.Button(frame, text="Agregar Curso", command=self.addCourse).grid(row=3, column=0, pady=5)
        tk.Button(frame, text="Buscar Curso (ID)", command=self.buscarCurso).grid(row=3, column=1, pady=5)
        
        self.treeCourses = ttk.Treeview(frame, columns=("ID", "Curso"), show='headings')
        self.treeCourses.heading("ID", text="ID")
        self.treeCourses.heading("Curso", text="Curso")
        self.treeCourses.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        frame.grid_rowconfigure(4, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    def viewCursos(self):
        print(self.grafo)

    def setup_dependency_ui(self, tab):
        frame = tk.LabelFrame(tab, text="Dependencias de Cursos", padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame, columns=("Curso", "Dependencias"), show='headings')
        self.tree.heading("Curso", text="Curso")
        self.tree.heading("Dependencias", text="Dependencias")
        self.tree.pack(fill="both", expand=True)

        pathFrame = tk.LabelFrame(tab, text="Encontrar Camino Más Corto", padx=10, pady=10)
        pathFrame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(pathFrame, text="Curso Inicial").grid(row=0, column=0)
        self.curso_inicio_entry = tk.Entry(pathFrame)
        self.curso_inicio_entry.grid(row=1, column=0)

        tk.Label(pathFrame, text="Curso Final").grid(row=0, column=1)
        self.curso_fin_entry = tk.Entry(pathFrame)
        self.curso_fin_entry.grid(row=1, column=1)
        tk.Button(pathFrame, text="Mostrar", command=self.viewCursos).grid(row=1, column=4, pady=5, columnspan=2)

        tk.Button(pathFrame, text="Encontrar Camino", command=self.encontrarCamino).grid(row=2, column=0, pady=5, columnspan=2)

    def actualizarCursos(self):
        for i in self.treeCourses.get_children():
            self.treeCourses.delete(i)
        for curso in self.grafo.dict:
            data = curso.getInfo().split("(")
            nombre = data[0]
            code = data[1].strip("')")
            self.treeCourses.insert("", "end", values=(code, nombre))

    def actualizarDependencias(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for curso in self.grafo.dict:
            dependientes = [dep.getInfo() for dep in self.grafo.dict[curso]]
            for dep in dependientes:
                self.tree.insert("", "end", values=(dep, curso.getInfo()))

root = tk.Tk()
app = Interfaz(root)
root.mainloop()

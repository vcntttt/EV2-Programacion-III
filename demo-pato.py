import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from collections import defaultdict

class Node:
    def __init__(self, key, data):
        self.key = key  # El valor clave del nodo (usado para ordenar en el BST
        self.data = data  # La información que almacena el nodo
        self.left = None  # Referencia al hijo izquierdo (inicialmente vacío)
        self.right = None  # Referencia al hijo derecho (inicialmente vacío)


class BST:
    def insert(self, root, key, data):
        if root is None:
            # Si no hay raíz, se crea un nuevo nodo como raíz
            return Node(key, data)
        if key < root.key:
            # Si la clave es menor, se inserta en el subárbol izquierdo (recursivamente)
            root.left = self.insert(root.left, key, data)
        else:
            # Si la clave es mayor o igual, se inserta en el subárbol derecho (recursivamente)
            root.right = self.insert(root.right, key, data)
        return root  # Se devuelve la raíz modificada

    def search(self, root, key):  # Busca un nodo con la clave dada
        if root is None or root.key == key:
            return root  # Si la raíz es nula o la clave coincide, se devuelve la raíz
        if key < root.key:
            # Si la clave es menor, se busca en el subárbol izquierdo (recursivamente)
            return self.search(root.left, key)
        # Si la clave es mayor, se busca en el subárbol derecho (recursivamente)
        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root  # Si la raíz es nula, no hay nada que borrar
        if key < root.key:
            # Si la clave es menor, se borra en el subárbol izquierdo
            root.left = self.delete(root.left, key)
        elif key > root.key:
            # Si la clave es mayor, se borra en el subárbol derecho
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right  # Caso 1: Nodo a borrar no tiene hijo izquierdo
            elif root.right is None:
                return root.left  # Caso 2: Nodo a borrar no tiene hijo derecho
            # Caso 3: Nodo a borrar tiene dos hijos
            # Se busca el nodo con el valor mínimo en el subárbol derecho
            temp = self.minValueNode(root.right)
            root.key = temp.key  # Se reemplaza el valor de la raíz con el valor mínimo encontrado
            # Se reemplaza el dato de la raíz con el dato del valor mínimo encontrado
            root.data = temp.data
            # Se elimina el nodo con el valor mínimo encontrado
            root.right = self.delete(root.right, temp.key)
        return root  # Se devuelve la raíz modificada

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        # Devuelve el nodo más a la izquierda (el que tiene el valor mínimo)
        return current


class AVLNode:
    def __init__(self, key, data):
        # El valor clave del nodo (usado para ordenar en el AVL)
        self.key = key
        self.data = data  # La información que almacena el nodo
        # La altura del nodo (inicialmente 1, ya que es un nodo hoja)
        self.height = 1
        self.left = None  # Referencia al hijo izquierdo (inicialmente vacío)
        self.right = None  # Referencia al hijo derecho (inicialmente vacío)


class AVL:
    def getHeight(self, root):
        if not root:
            return 0
        # Calcula la altura de un nodo dado. Si el nodo es None, devuelve 0 (caso base para nodos vacíos).
        return root.height

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        # Realiza una rotación a la derecha sobre el nodo y. Esto implica reordenar los nodos x, T2 e y, y actualizar sus alturas.
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        # Realiza una rotación a la izquierda sobre el nodo x, similar a la rotación derecha pero en sentido opuesto.
        return y

    def getBalance(self, root):
        if not root:
            return 0
        # Calcula el factor de equilibrio de un nodo, que es la diferencia
        return self.getHeight(root.left) - self.getHeight(root.right)
# de altura entre su subárbol izquierdo y derecho. Un factor de equilibrio de -1, 0 o 1 indica que el árbol está balanceado en ese nodo.

    def insert(self, root, key, data):
        if not root:
            return AVLNode(key, data)
        if key < root.key:
            root.left = self.insert(root.left, key, data)
        else:
            root.right = self.insert(root.right, key, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root  # Inserta un nuevo nodo con la clave y los datos dados. Después de la inserción, verifica el factor
# de equilibrio y realiza rotaciones (si es necesario) para mantener el árbol balanceado.

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        # Busca un nodo con la clave dada en el árbol AVL. La lógica es idéntica a la búsqueda en un BST, ya que la estructura básica del árbol es la misma.
        return self.search(root.right, key)


class Graph:
    def __init__(self):
        # El constructor inicializa un diccionario vacío llamado graph usando defaultdict(list).
        self.graph = defaultdict(list)
        # Esto significa que cada clave del diccionario tendrá por defecto una lista vacía como valor.
        # Esta lista vacía representará los nodos adyacentes (vecinos) a un nodo dado en el grafo.

    def add_edge(self, u, v):
        # Este método agrega una arista (conexión) entre los nodos u y v al grafo.
        self.graph[u].append(v)
        # Agrega v a la lista de nodos adyacentes de u.

    # Este método encuentra el camino más corto entre los nodos start y end utilizando una búsqueda en profundidad (DFS) recursiva.
    def find_shortest_path(self, start, end, path=[]):
        # Inicialmente, path es una lista vacía que se irá llenando con los nodos visitados en el camino.
        path = path + [start]
        if start == end:
            # Si el nodo start es igual al nodo end, se ha encontrado el destino y se devuelve el camino actual (path).
            return path
        if start not in self.graph:
            # Si el nodo start no está en el diccionario graph, significa que no tiene vecinos y no hay camino posible, por lo que se devuelve None.
            return None
        shortest = None
        # En caso contrario, se itera sobre los nodos adyacentes de start
        for node in self.graph[start]:
            if node not in path:
                # Si el nodo vecino aún no ha sido visitado (no está en path), se realiza una llamada recursiva a find_shortest_path para explorar ese camino.
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        # Si la llamada recursiva devuelve un camino válido (newpath), se compara su longitud con el camino más corto encontrado hasta el momento (shortest). Si es más corto, se actualiza shortest.
                        shortest = newpath
        # Finalmente, se devuelve el camino más corto encontrado (shortest).
        return shortest


class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Administración Escolar")
        self.bst = BST()
        self.bst_root = None
        self.avl = AVL()
        self.avl_root = None
        self.graph = Graph()

        # Interfaz de usuario
        self.setup_ui()

    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, padx=10)

        student_tab = tk.Frame(notebook)
        course_tab = tk.Frame(notebook)
        dependency_tab = tk.Frame(notebook)

        notebook.add(student_tab, text="Estudiantes")
        notebook.add(course_tab, text="Cursos")
        notebook.add(dependency_tab, text="Dependencias")

        self.setup_student_ui(student_tab)
        self.setup_course_ui(course_tab)
        self.setup_dependency_ui(dependency_tab)

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

        tk.Button(frame, text="Agregar Estudiante",
                  command=self.add_student).grid(row=2, column=0)
        tk.Button(frame, text="Buscar Estudiante",
                  command=self.search_student).grid(row=2, column=1)
        tk.Button(frame, text="Eliminar Estudiante",
                  command=self.delete_student).grid(row=2, column=2)

    def setup_course_ui(self, parent_frame):
        frame = tk.LabelFrame(
            parent_frame, text="Gestión de Cursos", padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        self.course_id_entry = tk.Entry(frame)
        self.course_id_entry.grid(row=0, column=1)
        self.course_name_entry = tk.Entry(frame)
        self.course_name_entry.grid(row=1, column=1)

        tk.Label(frame, text="ID del Curso").grid(row=0, column=0)
        tk.Label(frame, text="Nombre del Curso").grid(row=1, column=0)

        tk.Button(frame, text="Agregar Curso",
                  command=self.add_course).grid(row=2, column=0)
        tk.Button(frame, text="Buscar Curso",
                  command=self.search_course).grid(row=2, column=1)

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

        tk.Button(frame, text="Agregar Dependencia",
                  command=self.add_dependency).grid(row=2, column=0)
        tk.Button(frame, text="Encontrar Ruta",
                  command=self.find_path).grid(row=2, column=1)

    def add_student(self):
        student_id = int(self.student_id_entry.get())
        student_name = self.student_name_entry.get()
        self.bst_root = self.bst.insert(
            self.bst_root, student_id, student_name)
        self.student_id_entry.delete(0, tk.END)
        self.student_name_entry.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Estudiante agregado")

    def search_student(self):
        student_id = int(self.student_id_entry.get())
        result = self.bst.search(self.bst_root, student_id)
        if result:
            messagebox.showinfo(
                "Resultado", f"Estudiante encontrado: {result.data}")
        else:
            messagebox.showerror("Error", "Estudiante no encontrado")

    def delete_student(self):
        student_id = int(self.student_id_entry.get())
        self.bst_root = self.bst.delete(self.bst_root, student_id)
        messagebox.showinfo("Éxito", "Estudiante eliminado")

    def add_course(self):
        course_id = int(self.course_id_entry.get())
        course_name = self.course_name_entry.get()
        self.avl_root = self.avl.insert(self.avl_root, course_id, course_name)
        self.course_id_entry.delete(0, tk.END)
        self.course_name_entry.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Curso agregado")

    def search_course(self):
        course_id = int(self.course_id_entry.get())
        result = self.avl.search(self.avl_root, course_id)
        if result:
            messagebox.showinfo(
                "Resultado", f"Curso encontrado: {result.data}")
        else:
            messagebox.showerror("Error", "Curso no encontrado")

    def add_dependency(self):
        course1 = self.course1_entry.get()
        course2 = self.course2_entry.get()
        self.graph.add_edge(course1, course2)
        self.course1_entry.delete(0, tk.END)
        self.course2_entry.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Dependencia agregada")

    def find_path(self):
        course1 = self.course1_entry.get()
        course2 = self.course2_entry.get()
        path = self.graph.find_shortest_path(course1, course2)
        if path:
            messagebox.showinfo("Ruta", f"Ruta más corta: {' -> '.join(path)}")
        else:
            messagebox.showerror("Error", "No se encontró una ruta")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()

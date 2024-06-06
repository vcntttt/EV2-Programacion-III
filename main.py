import tkinter as tk

class Interfaz():
    def __init__(self, root):
        self.root = root
        self.root.title("8 - Gestor de Tareas con Lista Enlazada")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

root = tk.Tk()
app = Interfaz(root)
root.mainloop()
import tkinter as tk

class Interfaz():
    def __init__(self, root):
        self.root = root
        self.root.title("6 - Sistema de Administración Escolar")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

root = tk.Tk()
app = Interfaz(root)
root.mainloop()

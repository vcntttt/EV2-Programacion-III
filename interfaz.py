        tk.Button(frame, text="Agregar Curso", command=self.anadirCurso()).grid(row=2, column=0)
        tk.Button(frame, text="Buscar Curso", command=self.buscarCurso()).grid(row=2, column=1)

def anadirCurso(self):
        cursoID = int(self.cursoNombreEntry.get())
        nombreCurso = self.cursoNombreEntry.get()
        self.rootAVL = self.avl.insertar(self.rootAVL, cursoID, nombreCurso)
        self.cursoIdEntry.delete(0, tk.END)
        self.cursoIdEntry.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Curso agregado")

def buscarCurso(self):
        cursoID = int(self.cursoIdEntry.get())
        resultado = self.avl.buscar(self.rootAVL, cursoID)
        if resultado:
            messagebox.showinfo("Resultado", f"Curso encontrado: {resultado.curso}")
        else:
            messagebox.showerror("Error", "Curso no encontrado")
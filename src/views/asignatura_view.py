import customtkinter as ctk
from tkinter import messagebox
from src.controllers.asignatura_controller import AsignaturaController

class AsignaturaView(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Gestión de Asignaturas")
        self.geometry("450x500")
        self.controller = AsignaturaController()

        ctk.CTkLabel(self, text="NUEVA ASIGNATURA", font=("Roboto", 20, "bold")).pack(pady=20)

        self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Nombre de la Asignatura", width=300)
        self.nombre_entry.pack(pady=10)

        self.depto_entry = ctk.CTkEntry(self, placeholder_text="Departamento (ej. Ciencias, Lengua)", width=300)
        self.depto_entry.pack(pady=10)

        self.btn_guardar = ctk.CTkButton(self, text="Añadir Asignatura", command=self.guardar)
        self.btn_guardar.pack(pady=30)



    # Función guardar
    def guardar(self):
        nombre = self.nombre_entry.get()
        depto = self.depto_entry.get()

        resultado = self.controller.registrar_asignatura(nombre, depto)
        if "Éxito" in resultado:
            messagebox.showinfo("Confirmación", resultado)
            self.nombre_entry.delete(0, 'end')
            self.depto_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", resultado)
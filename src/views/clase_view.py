import customtkinter as ctk
from tkinter import messagebox
from src.controllers.clase_controller import ClaseController

class ClaseView(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Programación de Clases")
        self.geometry("450x600")
        self.controller = ClaseController()

        ctk.CTkLabel(self, text="ASIGNAR NUEVA CLASE", font=("Roboto", 20, "bold")).pack(pady=20)

        self.prof_id = ctk.CTkEntry(self, placeholder_text="ID del Profesor", width=300)
        self.prof_id.pack(pady=10)

        self.aula_id = ctk.CTkEntry(self, placeholder_text="ID del Aula", width=300)
        self.aula_id.pack(pady=10)

        self.asig_id = ctk.CTkEntry(self, placeholder_text="ID de la Asignatura", width=300)
        self.asig_id.pack(pady=10)

        self.anio = ctk.CTkEntry(self, placeholder_text="Año Académico (ej. 2023-24)", width=300)
        self.anio.pack(pady=10)

        ctk.CTkButton(self, text="Crear Clase", fg_color="green",
                      command=self.crear).pack(pady=30)



    def crear(self):
        res = self.controller.programar_clase(
            self.prof_id.get(), self.aula_id.get(), self.asig_id.get(), self.anio.get()
        )
        messagebox.showinfo("Sistema", res)
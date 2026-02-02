import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.controllers.material_controller import MaterialController

class MaterialView(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Gestión de Materiales e Inventario")
        self.geometry("500x550")
        self.controller = MaterialController()

        ctk.CTkLabel(self, text="INVENTARIO DE AULAS", font=("Roboto", 20, "bold")).pack(pady=20)

        # Sección Manual
        self.frame_manual = ctk.CTkFrame(self)
        self.frame_manual.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.frame_manual, text="Registro Manual").pack(pady=5)
        self.mat_nombre = ctk.CTkEntry(self.frame_manual, placeholder_text="Nombre del material")
        self.mat_nombre.pack(pady=5, padx=10)

        self.aula_id = ctk.CTkEntry(self.frame_manual, placeholder_text="ID del Aula")
        self.aula_id.pack(pady=5, padx=10)

        ctk.CTkButton(self.frame_manual, text="Añadir Manualmente",
                      command=self.añadir_manual).pack(pady=10)

        # SECCIÓN IMPORTAR (Punto 6.e)
        self.frame_import = ctk.CTkFrame(self, fg_color="transparent", border_width=2)
        self.frame_import.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(self.frame_import, text="Importación Masiva (Archivo)").pack(pady=5)
        ctk.CTkButton(self.frame_import, text="Seleccionar Archivo y Cargar",
                      fg_color="#2c3e50", command=self.importar_archivo).pack(pady=10)

    def añadir_manual(self):
        res = self.controller.añadir_material_manual(self.mat_nombre.get(), self.aula_id.get())
        messagebox.showinfo("Info", res)

    def importar_archivo(self):
        ruta = filedialog.askopenfilename(title="Seleccionar archivo de materiales",
                                          filetypes=(("Archivos de texto", "*.txt"), ("Todos", "*.*")))
        if ruta:
            id_aula = self.aula_id.get()
            if not id_aula:
                messagebox.showwarning("Atención", "Escribe primero el ID del aula a la que asignar el archivo.")
                return

            res = self.controller.cargar_materiales_desde_fichero(ruta, id_aula)
            messagebox.showinfo("Resultado", res)
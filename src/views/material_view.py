import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.controllers.material_controller import MaterialController


class MaterialView(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana secundaria
        self.title("Gestión de Materiales e Inventario")
        self.geometry("500x550")

        # Instanciamos el controlador para comunicar la vista con el modelo de materiales
        self.controller = MaterialController()

        # Título principal de la sección
        ctk.CTkLabel(self, text="INVENTARIO DE AULAS", font=("Roboto", 20, "bold")).pack(pady=20)

        # --- SECCIÓN 1: REGISTRO MANUAL ---
        # Creamos un frame para agrupar visualmente el formulario de registro único
        self.frame_manual = ctk.CTkFrame(self)
        self.frame_manual.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.frame_manual, text="Registro Manual").pack(pady=5)

        # Entrada para el nombre del objeto (ej. "Proyector", "Pizarra")
        self.mat_nombre = ctk.CTkEntry(self.frame_manual, placeholder_text="Nombre del material")
        self.mat_nombre.pack(pady=5, padx=10)

        # Entrada para el ID del Aula donde se ubicará el material (Clave Foránea)
        self.aula_id = ctk.CTkEntry(self.frame_manual, placeholder_text="ID del Aula")
        self.aula_id.pack(pady=5, padx=10)

        # Botón para ejecutar el registro individual
        ctk.CTkButton(self.frame_manual, text="Añadir Manualmente",
                      command=self.añadir_manual).pack(pady=10)

        # --- SECCIÓN 2: IMPORTACIÓN MASIVA ---
        # Este frame destaca visualmente la funcionalidad de carga desde archivo
        self.frame_import = ctk.CTkFrame(self, fg_color="transparent", border_width=2)
        self.frame_import.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(self.frame_import, text="Importación Masiva (Archivo .txt)").pack(pady=5)

        # Botón que dispara el selector de archivos del sistema operativo
        ctk.CTkButton(self.frame_import, text="Seleccionar Archivo y Cargar",
                      fg_color="#2c3e50", command=self.importar_archivo).pack(pady=10)

    # --- LÓGICA DE LA VISTA ---

    def añadir_manual(self):
        res = self.controller.añadir_material_manual(self.mat_nombre.get(), self.aula_id.get())
        messagebox.showinfo("Info", res)

    def importar_archivo(self):

        # Abrimos el diálogo para que el usuario busque el archivo
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de materiales",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos", "*.*"))
        )

        if ruta:

            # Validamos que el usuario haya indicado a qué aula van esos materiales
            id_aula = self.aula_id.get()
            if not id_aula:
                messagebox.showwarning("Atención", "Escribe primero el ID del aula a la que asignar el archivo.")
                return

            # El controlador procesa el archivo y devuelve el resultado de la importación
            res = self.controller.cargar_materiales_desde_fichero(ruta, id_aula)
            messagebox.showinfo("Resultado", res)
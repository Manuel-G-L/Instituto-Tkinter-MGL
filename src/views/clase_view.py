from tkinter import messagebox
import customtkinter as ctk
from src.controllers.clase_controller import ClaseController


class ClaseView(ctk.CTkToplevel):
    def __init__(self):

        # Inicialización de la clase padre
        super().__init__()

        # Configuración estética y de dimensiones de la ventana
        self.title("Programación de Clases")
        self.geometry("450x600")

        # Instanciamos el controlador para procesar la creación de la clase
        self.controller = ClaseController()

        # --- ELEMENTOS DE LA INTERFAZ (UI) ---

        # Título de la ventana
        ctk.CTkLabel(self, text="ASIGNAR NUEVA CLASE", font=("Roboto", 20, "bold")).pack(pady=20)

        # Entrada para el ID del Profesor (Clave foránea hacia la tabla personas)
        self.prof_id = ctk.CTkEntry(self, placeholder_text="ID del Profesor", width=300)
        self.prof_id.pack(pady=10)

        # Entrada para el ID del Aula (Clave foránea hacia la tabla aulas)
        self.aula_id = ctk.CTkEntry(self, placeholder_text="ID del Aula", width=300)
        self.aula_id.pack(pady=10)

        # Entrada para el ID de la Asignatura (Clave foránea hacia la tabla asignaturas)
        self.asig_id = ctk.CTkEntry(self, placeholder_text="ID de la Asignatura", width=300)
        self.asig_id.pack(pady=10)

        # Entrada para el periodo escolar
        self.anio = ctk.CTkEntry(self, placeholder_text="Año Académico (ej. 2023-24)", width=300)
        self.anio.pack(pady=10)

        # Botón de acción destacado en color verde para diferenciarlo
        ctk.CTkButton(self, text="Crear Clase", fg_color="green",
                      command=self.crear).pack(pady=30)

    # --- LÓGICA DE PROCESAMIENTO ---

    def crear(self):

        # Llamamos al metodo programar_clase del controlador pasando los 4 parámetros
        res = self.controller.programar_clase(
            self.prof_id.get(),
            self.aula_id.get(),
            self.asig_id.get(),
            self.anio.get()
        )

        # Mostramos una ventana emergente con el resultado (éxito o error de integridad)
        messagebox.showinfo("Sistema", res)
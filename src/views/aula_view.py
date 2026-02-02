import customtkinter as ctk
from tkinter import messagebox
from src.controllers.aula_controller import AulaController

class AulaView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana secundaria
        self.title("Gestión de Aulas")
        self.geometry("400x500")
        self.grab_set()  # Hace que la ventana sea modal (enfoca la atención aquí)

        self.controller = AulaController()

        # UI
        self.label = ctk.CTkLabel(self, text="REGISTRO DE AULAS", font=("Roboto", 20, "bold"))
        self.label.pack(pady=30)

        # Contenedor del formulario
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Campo: Número de Aula
        self.num_label = ctk.CTkLabel(self.form_frame, text="Número / Nombre de Aula:")
        self.num_label.pack(pady=(20, 5))
        self.num_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Ej: Aula 101", width=250)
        self.num_entry.pack(pady=5)

        # Campo: Capacidad
        self.cap_label = ctk.CTkLabel(self.form_frame, text="Capacidad máxima:")
        self.cap_label.pack(pady=(20, 5))
        self.cap_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Ej: 30", width=250)
        self.cap_entry.pack(pady=5)

        # Botón Guardar
        self.btn_guardar = ctk.CTkButton(
            self,
            text="Guardar Aula",
            command=self.ejecutar_registro,
            fg_color="#2c3e50",
            hover_color="#34495e"
        )
        self.btn_guardar.pack(pady=40)




    def ejecutar_registro(self):

        # Obtener datos de la vista
        numero = self.num_entry.get()
        capacidad = self.cap_entry.get()

        # Validar que no estén vacíos
        if not numero or not capacidad:
            messagebox.showwarning("Campos vacíos", "Por favor, rellena todos los campos.")
            return

        # Llamar al controlador
        resultado = self.controller.crear_aula(numero, capacidad)

        # Mostrar feedback al usuario
        if "Éxito" in resultado:
            messagebox.showinfo("Proceso completado", resultado)
            self.num_entry.delete(0, 'end')
            self.cap_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", resultado)
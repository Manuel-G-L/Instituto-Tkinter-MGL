import customtkinter as ctk
from tkinter import messagebox
from src.controllers.aula_controller import AulaController

class AulaView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # --- CONFIGURACIÓN DE LA VENTANA ---
        self.title("Gestión de Aulas")
        self.geometry("400x500")

        # El metodo grab_set() convierte la ventana en "modal":
        # Bloquea la interacción con la ventana principal hasta que se cierre esta.
        self.grab_set()

        # Instanciamos el controlador para comunicar la UI con la base de datos
        self.controller = AulaController()

        # --- DISEÑO DE LA INTERFAZ (UI) ---
        self.label = ctk.CTkLabel(self, text="REGISTRO DE AULAS", font=("Roboto", 20, "bold"))
        self.label.pack(pady=30)

        # Usamos un Frame para agrupar los campos de entrada y mejorar la estética
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Campo para el Nombre o Número del aula (ej: "Laboratorio 1")
        self.num_label = ctk.CTkLabel(self.form_frame, text="Número / Nombre de Aula:")
        self.num_label.pack(pady=(20, 5))
        self.num_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Ej: Aula 101", width=250)
        self.num_entry.pack(pady=5)

        # Campo para la capacidad de alumnos
        self.cap_label = ctk.CTkLabel(self.form_frame, text="Capacidad máxima:")
        self.cap_label.pack(pady=(20, 5))
        self.cap_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Ej: 30", width=250)
        self.cap_entry.pack(pady=5)

        # Botón de acción con colores personalizados (Midnight Blue)
        self.btn_guardar = ctk.CTkButton(
            self,
            text="Guardar Aula",
            command=self.ejecutar_registro,  # Al pulsar, llama al metodo de abajo
            fg_color="#2c3e50",
            hover_color="#34495e"
        )
        self.btn_guardar.pack(pady=40)

    # --- LÓGICA DE PROCESAMIENTO ---

    def ejecutar_registro(self):

        # Recuperamos lo que el usuario escribió en los campos de texto
        numero = self.num_entry.get()
        capacidad = self.cap_entry.get()

        # Validación visual: Evita enviar datos vacíos al controlador
        if not numero or not capacidad:
            messagebox.showwarning("Campos vacíos", "Por favor, rellena todos los campos.")
            return

        # Llamamos al controlador para que intente crear el aula en la BD
        resultado = self.controller.crear_aula(numero, capacidad)

        # Feedback visual según el resultado de la operación
        if "Éxito" in resultado:
            messagebox.showinfo("Proceso completado", resultado)

            # Limpiamos los campos para una nueva entrada
            self.num_entry.delete(0, 'end')
            self.cap_entry.delete(0, 'end')

        else:
            # En caso de error
            messagebox.showerror("Error", resultado)
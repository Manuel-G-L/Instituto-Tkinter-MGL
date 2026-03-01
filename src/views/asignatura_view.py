import customtkinter as ctk
from tkinter import messagebox
from src.controllers.asignatura_controller import AsignaturaController

class AsignaturaView(ctk.CTkToplevel):
    def __init__(self):

        # Inicializamos la clase padre
        super().__init__()

        # Configuración básica de la ventana de gestión
        self.title("Gestión de Asignaturas")
        self.geometry("450x500")

        # Instanciamos el controlador para comunicar la vista con el modelo
        self.controller = AsignaturaController()

        # --- CREACIÓN DE ELEMENTOS DE LA INTERFAZ (UI) ---

        # Título llamativo en la parte superior
        ctk.CTkLabel(self, text="NUEVA ASIGNATURA", font=("Roboto", 20, "bold")).pack(pady=20)

        # Campo de texto para el nombre de la asignatura
        self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Nombre de la Asignatura", width=300)
        self.nombre_entry.pack(pady=10)

        # Campo de texto para el departamento
        self.depto_entry = ctk.CTkEntry(self, placeholder_text="Departamento (ej. Ciencias, Lengua)", width=300)
        self.depto_entry.pack(pady=10)

        # Botón para ejecutar la acción de guardado
        # Al hacer clic, llama a la función self.guardar
        self.btn_guardar = ctk.CTkButton(self, text="Añadir Asignatura", command=self.guardar)
        self.btn_guardar.pack(pady=30)

    # --- LÓGICA DE LA VISTA ---

    def guardar(self):

        # Obtenemos el texto introducido por el usuario
        nombre = self.nombre_entry.get()
        depto = self.depto_entry.get()

        # Enviamos los datos al controlador y recibimos una respuesta (String)
        resultado = self.controller.registrar_asignatura(nombre, depto)

        # Gestión de la respuesta para informar al usuario
        if "Éxito" in resultado:
            messagebox.showinfo("Confirmación", resultado)

            # Limpiamos los campos para poder introducir otra asignatura
            self.nombre_entry.delete(0, 'end')
            self.depto_entry.delete(0, 'end')

        else:
            # Si el controlador devuelve un error (campos vacíos, etc.), mostramos alerta roja
            messagebox.showerror("Error", resultado)
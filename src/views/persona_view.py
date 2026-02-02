import customtkinter as ctk
from src.controllers.persona_controller import PersonaController

# Usamos Toplevel para que sea una ventana hija
class PersonaView(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Gestión de Personas")
        self.geometry("500x600")
        self.controller = PersonaController()

        # --- FORMULARIO ---
        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.entry_nombre.pack(pady=10)

        self.entry_apellidos = ctk.CTkEntry(self, placeholder_text="Apellidos")
        self.entry_apellidos.pack(pady=10)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=10)

        self.combobox_rol = ctk.CTkComboBox(self, values=["Alumno", "Profesor", "Direccion"])
        self.combobox_rol.pack(pady=10)

        self.entry_extra = ctk.CTkEntry(self, placeholder_text="Matrícula / Dept / Cargo")
        self.entry_extra.pack(pady=10)

        # Botón Guardar
        self.btn_guardar = ctk.CTkButton(self, text="Registrar Persona", command=self.guardar)
        self.btn_guardar.pack(pady=20)



    # Función para guardar la persona
    def guardar(self):
        datos = {
            "nombre": self.entry_nombre.get(),
            "apellidos": self.entry_apellidos.get(),
            "email": self.entry_email.get(),
            "rol": self.combobox_rol.get().lower(),
            "extra_info": self.entry_extra.get()
        }
        mensaje = self.controller.crear_persona(datos)
        print(mensaje)
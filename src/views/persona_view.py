import customtkinter as ctk
from src.controllers.persona_controller import PersonaController


class PersonaView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # --- CONFIGURACIÓN DE LA VENTANA ---
        self.title("Gestión de Personas")
        self.geometry("500x600")

        # Instanciamos el controlador para procesar los registros
        self.controller = PersonaController()

        # --- FORMULARIO DE INSCRIPCIÓN (Requisito 6.b) ---

        # Campo para el nombre
        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre", width=300)
        self.entry_nombre.pack(pady=10)

        # Campo para los apellidos
        self.entry_apellidos = ctk.CTkEntry(self, placeholder_text="Apellidos", width=300)
        self.entry_apellidos.pack(pady=10)

        # Campo para el correo electrónico (será validado por el controlador)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email", width=300)
        self.entry_email.pack(pady=10)

        # Selector de Rol: Permite elegir la categoría de la persona
        self.combobox_rol = ctk.CTkComboBox(self, values=["Alumno", "Profesor", "Direccion"], width=300)
        self.combobox_rol.pack(pady=10)

        # Campo polivalente: sirve para Matrícula (alumnos), Departamento (profes) o Cargo (dirección)
        self.entry_extra = ctk.CTkEntry(self, placeholder_text="Matrícula / Dept / Cargo", width=300)
        self.entry_extra.pack(pady=10)

        # Botón para ejecutar la acción de registro
        self.btn_guardar = ctk.CTkButton(self, text="Registrar Persona", command=self.guardar)
        self.btn_guardar.pack(pady=20)

    # --- LÓGICA DE LA VISTA ---

    def guardar(self):

        # Creamos el diccionario de datos recogiendo los valores de los Entry
        datos = {
            "nombre": self.entry_nombre.get(),
            "apellidos": self.entry_apellidos.get(),
            "email": self.entry_email.get(),
            "rol": self.combobox_rol.get().lower(),  # Convertimos a minúsculas para consistencia en BD
            "extra_info": self.entry_extra.get()  # Aquí va el dato específico según el rol
        }

        # El controlador se encarga de instanciar la clase correcta (Alumno, Profesor...) y devolver un mensaje con el resultado de la operación.
        mensaje = self.controller.crear_persona(datos)

        # Mostramos el resultado por consola
        print(mensaje)
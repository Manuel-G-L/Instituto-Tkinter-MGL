import customtkinter as ctk
# Asegúrate de que estas rutas sean correctas según tu estructura de carpetas
from src.views.asignatura_view import AsignaturaView
from src.views.clase_view import ClaseView
from src.views.material_view import MaterialView
from src.views.persona_view import PersonaView
from src.views.aula_view import AulaView # Suponiendo que ya la creaste

class MainMenuView(ctk.CTk):
    def __init__(self, usuario_nombre):
        super().__init__()

        self.title(f"Sistema Escolar - Bienvenida/o {usuario_nombre}")
        self.geometry("600x500")

        # Título
        self.label = ctk.CTkLabel(self, text="PANEL DE CONTROL", font=("Roboto", 24, "bold"))
        self.label.pack(pady=30)

        # Contenedor de botones
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Botones de Gestión - AHORA ASIGNADOS CORRECTAMENTE
        ctk.CTkButton(self.frame, text="Gestión de Personas",
                      command=self.abrir_personas).grid(row=0, column=0, padx=20, pady=20)

        ctk.CTkButton(self.frame, text="Gestión de Aulas",
                      command=self.abrir_aulas).grid(row=0, column=1, padx=20, pady=20)

        ctk.CTkButton(self.frame, text="Gestión de Materiales",
                      command=self.abrir_materiales).grid(row=1, column=0, padx=20, pady=20)

        ctk.CTkButton(self.frame, text="Gestión de Asignaturas",
                      command=self.abrir_asignaturas).grid(row=1, column=1, padx=20, pady=20)

        ctk.CTkButton(self.frame, text="Gestión de Clases",
                      command=self.abrir_clases,
                      fg_color="darkgreen").grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=20)

    # Funciones corregidas (sin mainloop interno)
    def abrir_personas(self):
        PersonaView() # Se abre sola al instanciarse

    def abrir_aulas(self):
        AulaView()

    def abrir_asignaturas(self):
        AsignaturaView()

    def abrir_materiales(self):
        MaterialView()

    def abrir_clases(self):
        ClaseView()
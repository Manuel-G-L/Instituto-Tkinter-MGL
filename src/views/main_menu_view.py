import customtkinter as ctk
from src.views.asignatura_view import AsignaturaView
from src.views.clase_view import ClaseView
from src.views.material_view import MaterialView
from src.views.persona_view import PersonaView
from src.views.aula_view import AulaView
from src.views.calificaciones_view import CalificacionesView


class MainMenuView(ctk.CTk):
    def __init__(self, usuario_nombre):
        super().__init__()

        # Configuración de la ventana principal
        self.title(f"Sistema Escolar - Bienvenida/o {usuario_nombre}")
        self.geometry("700x550")

        # Configuración de la cuadrícula (Grid) de la ventana principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- CABECERA ---
        self.label = ctk.CTkLabel(self, text="PANEL DE CONTROL ADMINISTRATIVO",
                                  font=("Roboto", 24, "bold"))
        self.label.grid(row=0, column=0, pady=30)

        # --- CONTENEDOR DE BOTONES ---
        # Creamos un frame para agrupar los botones de gestión
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=40, pady=(0, 40), sticky="nsew")

        # Configuramos el grid interno del frame: 2 columnas y 3 filas
        self.frame.grid_columnconfigure((0, 1), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Definimos un diccionario con parámetros comunes para mantener la estética uniforme
        btn_params = {"width": 220, "height": 50, "font": ("Roboto", 14)}

        # --- FILA 0: Gestión de Personal y Espacios ---
        ctk.CTkButton(self.frame, text="👥 Gestión de Personas",
                      command=self.abrir_personas, **btn_params).grid(row=0, column=0, padx=20, pady=20)

        ctk.CTkButton(self.frame, text="🏫 Gestión de Aulas",
                      command=self.abrir_aulas, **btn_params).grid(row=0, column=1, padx=20, pady=20)

        # --- FILA 1: Gestión de Inventario y Materias ---
        ctk.CTkButton(self.frame, text="📦 Gestión de Materiales",
                      command=self.abrir_materiales, **btn_params).grid(row=1, column=0, padx=20, pady=20)

        ctk.CTkButton(self.frame, text="📚 Gestión de Asignaturas",
                      command=self.abrir_asignaturas, **btn_params).grid(row=1, column=1, padx=20, pady=20)

        # --- FILA 2: Operaciones Académicas ---
        # Botón para programar clases
        ctk.CTkButton(self.frame, text="🗓️ Programar Clases",
                      command=self.abrir_clases, fg_color="#27ae60", hover_color="#2ecc71",
                      **btn_params).grid(row=2, column=0, padx=20, pady=20)

        # Botón para ver notas
        ctk.CTkButton(self.frame, text="📝 Ver Calificaciones",
                      command=self.abrir_calificaciones, fg_color="#8e44ad", hover_color="#9b59b6",
                      **btn_params).grid(row=2, column=1, padx=20, pady=20)

    # --- MÉTODOS PARA INSTANCIAR LAS VISTAS SECUNDARIAS ---
    # Cada metodo crea una nueva ventana del tipo correspondiente al pulsar el botón

    def abrir_personas(self): PersonaView()

    def abrir_aulas(self): AulaView()

    def abrir_materiales(self): MaterialView()

    def abrir_asignaturas(self): AsignaturaView()

    def abrir_clases(self): ClaseView()

    def abrir_calificaciones(self): CalificacionesView()
from database.database_manager import DatabaseManager
from src.models.persona import Persona

class Profesor(Persona):
    def __init__(self, id_persona=None, nombre="", apellidos="", email="", departamento=""):

        # Llamamos al constructor de la clase padre (Persona) para inicializar datos comunes
        super().__init__(id_persona, nombre, apellidos, email)

        self.__departamento = departamento
        self.__rol = "profesor"
        self.db = DatabaseManager()

    # --- GETTERS Y SETTERS PARA DEPARTAMENTO ---

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, valor):
        if valor and len(valor.strip()) > 0:
            self.__departamento = valor
        else:
            print("Error: El departamento no puede estar vacío.")

    # --- MÉTODOS DE PERSISTENCIA ---

    def registrar(self):
        self._Persona__rol = "profesor"  # Acceso al atributo privado de la clase padre si fuera necesario
        return super().registrar(info_adicional=self.__departamento)

    def modificar(self):
        return super().modificar(info_adicional=self.__departamento)
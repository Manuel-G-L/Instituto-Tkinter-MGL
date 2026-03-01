from database.database_manager import DatabaseManager
from src.models.profesor import Profesor

class Direccion(Profesor):
    def __init__(self, id_persona=None, nombre="", apellidos="", email="", departamento="", cargo=""):

        # Llamamos al constructor de Profesor, que a su vez llama al de Persona
        super().__init__(id_persona, nombre, apellidos, email, departamento)

        self.__cargo = cargo
        self.db = DatabaseManager()

    # --- GETTER Y SETTER PARA CARGO ---

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, valor):
        if valor and len(valor.strip()) > 0:
            self.__cargo = valor
        else:
            print("Error: El cargo de dirección es obligatorio.")

    # --- MÉTODOS DE PERSISTENCIA ---

    def registrar(self):
        self.rol = "direccion"
        return super().registrar(info_adicional=self.__cargo)

    def modificar(self):
        return super().modificar(info_adicional=self.__cargo)
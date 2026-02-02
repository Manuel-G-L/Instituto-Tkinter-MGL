from database.database_manager import DatabaseManager
from src.models.profesor import Profesor

class Direccion(Profesor):
    def __init__(self, id_persona=None, nombre="", apellidos="", email="", departamento="", cargo=""):

        # Cargo puede ser: Director, Secretario o Jefe de Estudios
        super().__init__(id_persona, nombre, apellidos, email, departamento)
        self.__cargo = cargo
        self.db = DatabaseManager()

    @property
    def cargo(self):
        return self.__cargo
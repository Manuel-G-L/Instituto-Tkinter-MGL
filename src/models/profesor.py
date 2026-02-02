from database.database_manager import DatabaseManager
from src.models.persona import Persona

class Profesor(Persona):

    def __init__(self, id_persona=None, nombre="", apellidos="", email="", departamento=""):
        super().__init__(id_persona, nombre, apellidos, email)
        self.__departamento = departamento
        self.db = DatabaseManager()

    @property
    def departamento(self):
        return self.__departamento
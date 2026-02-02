from database.database_manager import DatabaseManager
from src.models.persona import Persona

class Alumno(Persona):

    def __init__(self, id_persona=None, nombre="", apellidos="", email="", matricula="", rol=""):
        super().__init__(id_persona, nombre, apellidos, email)
        self.__matricula = matricula
        self.__rol = rol
        self.db = DatabaseManager()

    @property
    def matricula(self):
        return self.__matricula
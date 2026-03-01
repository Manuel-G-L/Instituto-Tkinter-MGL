from database.database_manager import DatabaseManager
from src.models.persona import Persona

class Alumno(Persona):

    def __init__(self, id_persona=None, nombre="", apellidos="", email="", matricula="", rol="alumno"):

        # Llamamos al constructor de la clase padre (Persona)
        super().__init__(id_persona, nombre, apellidos, email)

        # Atributos privados (Encapsulamiento mediante __)
        self.__matricula = matricula
        self.__rol = rol
        self.db = DatabaseManager()

    # --- GETTERS Y SETTERS PARA MATRÍCULA ---

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        if valor and len(valor) > 0:
            self.__matricula = valor
        else:
            print("Error: La matrícula no puede estar vacía.")

    # --- GETTERS Y SETTERS PARA ROL ---

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, valor):
        self.__rol = valor

    # --- MÉTODOS DE PERSISTENCIA ---

    def registrar(self):
        return super().registrar(info_adicional=self.__matricula)

    def modificar(self):
        return super().modificar(info_adicional=self.__matricula)
from database.database_manager import DatabaseManager


class Persona:
    def __init__(self, id_persona=None, nombre="", apellidos="", email="", rol=""):

        # Usamos __ para que sean PRIVADOS
        self.__id = id_persona
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__rol = rol
        self.db = DatabaseManager()


    # Propiedades
    @property
    def id(self): return self.__id

    @property
    def nombre(self): return self.__nombre

    @nombre.setter
    def nombre(self, valor): self.__nombre = valor

    @property
    def email(self): return self.__email



    # Métodos de Gestión a usar
    def registrar(self, info_adicional=""):
        sql = "INSERT INTO personas (nombre, apellidos, email, rol, extra_info) VALUES (?, ?, ?, ?, ?)"
        params = (self.__nombre, self.__apellidos, self.__email, self.__rol, info_adicional)
        self.__id = self.db.execute_query(sql, params)
        return self.__id

    def modificar(self, info_adicional=""):
        sql = "UPDATE personas SET nombre=?, apellidos=?, email=?, extra_info=? WHERE id=?"
        params = (self.__nombre, self.__apellidos, self.__email, info_adicional, self.__id)
        return self.db.execute_query(sql, params)

    def eliminar(self):
        sql = "DELETE FROM personas WHERE id=?"
        return self.db.execute_query(sql, (self.__id,))
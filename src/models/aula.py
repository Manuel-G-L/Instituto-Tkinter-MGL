from database.database_manager import DatabaseManager

class Aula:

    def __init__(self, id_aula=None, numero="", capacidad=0):

        # Campos privados
        self.__id = id_aula
        self.__numero = numero
        self.__capacidad = capacidad
        self.db = DatabaseManager()


    # Propiedades
    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if valor:
            self.__numero = valor

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if int(valor) > 0: # Validación: capacidad positiva
            self.__capacidad = int(valor)
        else:
            print("Error: La capacidad debe ser mayor que 0")



    # Métodos
    def registrar(self):
        sql = "INSERT INTO aulas (numero, capacidad) VALUES (?, ?)"
        self.__id = self.db.execute_query(sql, (self.__numero, self.__capacidad))
        return self.__id

    def modificar(self):
        sql = "UPDATE aulas SET numero=?, capacidad=? WHERE id=?"
        return self.db.execute_query(sql, (self.__numero, self.__capacidad, self.__id))

    def eliminar(self):
        sql = "DELETE FROM aulas WHERE id=?"
        return self.db.execute_query(sql, (self.__id,))
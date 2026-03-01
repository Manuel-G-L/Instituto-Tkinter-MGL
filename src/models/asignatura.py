from database.database_manager import DatabaseManager

class Asignatura:

    def __init__(self, id_asig=None, nombre="", departamento=""):

        # Atributos privados
        self.__id = id_asig
        self.__nombre = nombre
        self.__departamento = departamento
        self.db = DatabaseManager()


    # Propiedades
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 0:
            self.__nombre = valor
        else:
            print("Error: El nombre de la asignatura no puede estar vacío")

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, valor):
        # El departamento es obligatorio según el PDF
        self.__departamento = valor



    # Métodos a usar
    def registrar(self):
        sql = "INSERT INTO asignaturas (nombre, departamento) VALUES (?, ?)"
        self.__id = self.db.execute_query(sql, (self.__nombre, self.__departamento))
        return self.__id

    def modificar(self):
        sql = "UPDATE asignaturas SET nombre=?, departamento=? WHERE id=?"
        return self.db.execute_query(sql, (self.__nombre, self.__departamento, self.__id))

    def eliminar(self):
        sql = "DELETE FROM asignaturas WHERE id=?"
        return self.db.execute_query(sql, (self.__id,))
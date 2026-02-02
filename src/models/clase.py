from database.database_manager import DatabaseManager


class Clase:

    def __init__(self, id_clase=None, id_profesor=None, id_aula=None, id_asignatura=None, anio_academico=""):

        # Campos privados
        self.__id = id_clase
        self.__id_profesor = id_profesor
        self.__id_aula = id_aula
        self.__id_asignatura = id_asignatura
        self.__anio_academico = anio_academico
        self.db = DatabaseManager()


    # Propiedades
    @property
    def id(self): return self.__id

    @property
    def anio_academico(self): return self.__anio_academico

    # Necesitamos estas propiedades para que el Controlador pueda verificar
    # si el profesor o el aula están disponibles.
    @property
    def id_profesor(self): return self.__id_profesor

    @property
    def id_aula(self): return self.__id_aula



    # Métodos
    def registrar(self):
        sql = "INSERT INTO clases (id_profesor, id_aula, id_asignatura, anio_academico) VALUES (?, ?, ?, ?)"
        params = (self.__id_profesor, self.__id_aula, self.__id_asignatura, self.__anio_academico)
        self.__id = self.db.execute_query(sql, params)
        return self.__id

    def modificar(self):
        sql = "UPDATE clases SET id_profesor=?, id_aula=?, id_asignatura=?, anio_academico=? WHERE id=?"
        params = (self.__id_profesor, self.__id_aula, self.__id_asignatura, self.__anio_academico, self.__id)
        return self.db.execute_query(sql, params)

    def eliminar(self):
        sql = "DELETE FROM clases WHERE id=?"
        return self.db.execute_query(sql, (self.__id,))
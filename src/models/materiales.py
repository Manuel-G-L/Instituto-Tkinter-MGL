from database.database_manager import DatabaseManager


class Material:
    def __init__(self, id_material=None, nombre="", estado="Nuevo", aula_id=None):

        # Campos privados
        self.__id = id_material
        self.__nombre = nombre
        self.__estado = estado
        self.__aula_id = aula_id
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
        if len(valor) > 2:
            self.__nombre = valor

    @property
    def aula_id(self):
        return self.__aula_id

    @aula_id.setter
    def aula_id(self, valor):
        self.__aula_id = valor



    # Métodos
    def registrar(self):
        sql = "INSERT INTO materiales (nombre, id_aula) VALUES (?, ?)"
        self.__id = self.db.execute_query(sql, (self.__nombre, self.__aula_id))
        return self.__id

    def modificar(self):
        sql = "UPDATE materiales SET nombre=?, id_aula=? WHERE id=?"
        return self.db.execute_query(sql, (self.__nombre, self.__aula_id, self.__id))

    def eliminar(self):
        sql = "DELETE FROM materiales WHERE id=?"
        return self.db.execute_query(sql, (self.__id,))


    # Metodo para importar los materiales desde un archivo
    @staticmethod
    def importar_desde_archivo(ruta_archivo, aula_id):

        # Lee un archivo y registra los materiales en un aula específica
        try:
            with open(ruta_archivo, 'r') as f:
                for linea in f:
                    nombre_material = linea.strip()
                    nuevo = Material(nombre=nombre_material, aula_id=aula_id)
                    nuevo.registrar()
            return True
        except Exception as e:
            print(f"Error al importar: {e}")
            return False
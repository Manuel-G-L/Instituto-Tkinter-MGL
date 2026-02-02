import sqlite3
from sqlite3 import Error

class DatabaseManager:

    def __init__(self, db_file="instituto.db"):
        self.db_file = db_file

        # Creamos las tablas automáticamente al instanciar el manager
        self.setup_tables()



    # Crear Conexión
    def create_connection(self):

        # Crea una conexión a la base de datos SQLite.
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        return conn



    # Crear Tablas
    def setup_tables(self):

        # Crear la estructura de la BD en 3ª Forma Normal
        # Incluye Personas, Aulas, Materiales, Asignaturas y Clases
        script_tablas = """
        
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT UNIQUE,
            rol TEXT NOT NULL, -- 'alumno', 'profesor', 'direccion'
            extra_info TEXT    -- Para matrícula, departamento o cargo
        );

        CREATE TABLE IF NOT EXISTS aulas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL,
            capacidad INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS materiales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            id_aula INTEGER,
            FOREIGN KEY (id_aula) REFERENCES aulas (id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS asignaturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            departamento TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS clases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_profesor INTEGER,
            id_aula INTEGER,
            id_asignatura INTEGER,
            anio_academico TEXT NOT NULL,
            FOREIGN KEY (id_profesor) REFERENCES personas (id),
            FOREIGN KEY (id_aula) REFERENCES aulas (id),
            FOREIGN KEY (id_asignatura) REFERENCES asignaturas (id)
        );
        """

        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.executescript(script_tablas)
                conn.commit()
            except Error as e:
                print(f"Error al crear las tablas: {e}")
            finally:
                conn.close()

        # DATOS INICIALES (PARA EL LOGIN)
        def populate_initial_data(self):

            # Comprobamos si ya hay datos
            check = self.fetch_all("SELECT id FROM personas LIMIT 1")
            if not check:
                print("Insertando datos de prueba iniciales...")

                # Personas (ID 1 será admin, ID 2 profe, ID 3 alumno)
                usuarios = []

                for u in usuarios:
                    self.execute_query(
                        "INSERT INTO personas (nombre, apellidos, email, rol, extra_info) VALUES (?,?,?,?,?)", u)

                # Aulas
                self.execute_query("INSERT INTO aulas (numero, capacidad) VALUES (?,?)", ("101", 30))
                self.execute_query("INSERT INTO aulas (numero, capacidad) VALUES (?,?)", ("Laboratorio", 20))

                # Asignaturas
                self.execute_query("INSERT INTO asignaturas (nombre, departamento) VALUES (?,?)",
                                   ("Python", "Informática"))

                print("Datos insertados. Puedes usar: admin@instituto.com con ID: 1")



    # Ejecutar Consultas
    def execute_query(self, query, params=()):

        # Ejecuta una consulta (INSERT, UPDATE, DELETE)
        conn = self.create_connection()

        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error ejecutando consulta: {e}")
                return None
            finally:
                conn.close()
        return None

    def fetch_all(self, query, params=()):

        # Recupera todos los resultados de una consulta (SELECT)
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, params)
                return cursor.fetchall()
            except Error as e:
                print(f"Error al recuperar datos: {e}")
                return []
            finally:
                conn.close()
        return []
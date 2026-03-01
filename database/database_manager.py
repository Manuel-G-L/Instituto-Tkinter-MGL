import sqlite3
from sqlite3 import Error


class DatabaseManager:
    def __init__(self, db_file="instituto.db"):
        self.db_file = db_file

        # Creamos las tablas
        self.setup_tables()

        # Insertamos los datos iniciales
        self.populate_initial_data()

    def create_connection(self):
        conn = None
        try:

            # Conectamos a la BD
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:

            # Gestion de errores
            print(f"Error al conectar a la base de datos: {e}")
        return conn

    # Creamos las tablas
    def setup_tables(self):
        script_tablas = """
                        CREATE TABLE IF NOT EXISTS personas \
                        ( \
                            id \
                            INTEGER \
                            PRIMARY \
                            KEY \
                            AUTOINCREMENT, \
                            nombre \
                            TEXT \
                            NOT \
                            NULL, \
                            apellidos \
                            TEXT \
                            NOT \
                            NULL, \
                            email \
                            TEXT \
                            UNIQUE, \
                            rol \
                            TEXT \
                            NOT \
                            NULL, \
                            extra_info \
                            TEXT
                        );

                        CREATE TABLE IF NOT EXISTS aulas \
                        ( \
                            id \
                            INTEGER \
                            PRIMARY \
                            KEY \
                            AUTOINCREMENT, \
                            numero \
                            TEXT \
                            NOT \
                            NULL, \
                            capacidad \
                            INTEGER \
                            NOT \
                            NULL
                        );

                        CREATE TABLE IF NOT EXISTS materiales \
                        ( \
                            id \
                            INTEGER \
                            PRIMARY \
                            KEY \
                            AUTOINCREMENT, \
                            nombre \
                            TEXT \
                            NOT \
                            NULL, \
                            id_aula \
                            INTEGER, \
                            FOREIGN \
                            KEY \
                        ( \
                            id_aula \
                        ) REFERENCES aulas \
                        ( \
                            id \
                        ) ON DELETE CASCADE
                            );

                        CREATE TABLE IF NOT EXISTS asignaturas \
                        ( \
                            id \
                            INTEGER \
                            PRIMARY \
                            KEY \
                            AUTOINCREMENT, \
                            nombre \
                            TEXT \
                            NOT \
                            NULL, \
                            departamento \
                            TEXT \
                            NOT \
                            NULL
                        );

                        CREATE TABLE IF NOT EXISTS clases \
                        ( \
                            id \
                            INTEGER \
                            PRIMARY \
                            KEY \
                            AUTOINCREMENT, \
                            id_profesor \
                            INTEGER, \
                            id_aula \
                            INTEGER, \
                            id_asignatura \
                            INTEGER, \
                            anio_academico \
                            TEXT \
                            NOT \
                            NULL, \
                            FOREIGN \
                            KEY \
                        ( \
                            id_profesor \
                        ) REFERENCES personas \
                        ( \
                            id \
                        ),
                            FOREIGN KEY \
                        ( \
                            id_aula \
                        ) REFERENCES aulas \
                        ( \
                            id \
                        ),
                            FOREIGN KEY \
                        ( \
                            id_asignatura \
                        ) REFERENCES asignaturas \
                        ( \
                            id \
                        )
                            );

                        CREATE TABLE IF NOT EXISTS calificaciones \
                        ( \
                            id \
                            INTEGER \
                            PRIMARY \
                            KEY \
                            AUTOINCREMENT, \
                            id_alumno \
                            INTEGER, \
                            id_asignatura \
                            INTEGER, \
                            nota \
                            REAL \
                            CHECK \
                        ( \
                            nota \
                            >= \
                            0 \
                            AND \
                            nota \
                            <= \
                            10 \
                        ),
                            convocatoria TEXT,
                            anio TEXT,
                            FOREIGN KEY \
                        ( \
                            id_alumno \
                        ) REFERENCES personas \
                        ( \
                            id \
                        ),
                            FOREIGN KEY \
                        ( \
                            id_asignatura \
                        ) REFERENCES asignaturas \
                        ( \
                            id \
                        )
                            ); \
                        """

        # Creamos la conexion
        conn = self.create_connection()
        if conn:
            try:

                # Creamos el cursor y ejecutamos las tablas
                cursor = conn.cursor()
                cursor.executescript(script_tablas)
                conn.commit()

            except Error as e:

                # Gestion de errores
                print(f"Error al crear las tablas: {e}")
            finally:
                conn.close()

    # Datos iniciales
    def populate_initial_data(self):

        # Comprobamos si ya existe el admin para no duplicarlo cada vez que abras la app
        check = self.fetch_all("SELECT id FROM personas WHERE email = 'admin@instituto.com'")

        if not check:
            print("Base de datos vacía. Insertando administrador por defecto...")

            # Insertamos al Administrador (ID 1)
            self.execute_query(
                "INSERT INTO personas (nombre, apellidos, email, rol, extra_info) VALUES (?,?,?,?,?)",
                ("Admin", "Instituto", "admin@instituto.com", "direccion", "Director General")
            )

            # Insertamos un Alumno de prueba (ID 2) para que la pantalla de notas no esté vacía
            self.execute_query(
                "INSERT INTO personas (nombre, apellidos, email, rol, extra_info) VALUES (?,?,?,?,?)",
                ("Juan", "García", "juan@alumno.com", "alumno", "MAT-2024-001")
            )

            # Una asignatura de prueba
            self.execute_query(
                "INSERT INTO asignaturas (nombre, departamento) VALUES (?,?)",
                ("Python Avanzado", "Informática")
            )

            # Una nota de prueba para Juan
            self.execute_query(
                "INSERT INTO calificaciones (id_alumno, id_asignatura, nota, convocatoria, anio) VALUES (?,?,?,?,?)",
                (2, 1, 9.5, "Ordinaria", "2023-24")
            )

            print("¡Hecho! Login: admin@instituto.com | Contraseña: 1")

    # Ejecutamos una consulta
    def execute_query(self, query, params=()):

        # Creamos una conexión a la BD
        conn = self.create_connection()
        if conn:
            try:

                # Hacemos al consulta
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid

            except Error as e:

                # Gestion de errores
                print(f"Error ejecutando consulta: {e}")
                return None
            finally:

                # Cerramos la conexión
                conn.close()
        return None

    # Ejecuta una consulta de selección (SELECT) en la base de datos y devuelve todos los registros encontrados.
    def fetch_all(self, query, params=()):

        # Intentamos establecer conexión con el archivo .db
        conn = self.create_connection()

        if conn:
            try:

                # Creamos un cursor
                cursor = conn.cursor()

                # Ejecutamos la sentencia SQL recibida.
                # Se pasan 'params' de forma segura para evitar Inyección SQL.
                cursor.execute(query, params)

                # Retornamos una lista con todas las filas obtenidas
                return cursor.fetchall()

            except Error as e:

                # Gestion de errores
                print(f"Error al recuperar datos: {e}")
                return []

            finally:

                # Cerramos la conexión
                conn.close()

        # Si la conexión no se pudo establecer, devolvemos una lista vacía
        return []
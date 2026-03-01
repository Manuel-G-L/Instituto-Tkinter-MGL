import csv
from database.database_manager import DatabaseManager

class CalificacionesController:
    def __init__(self):

        # Inicializamos la conexión a la base de datos
        self.db = DatabaseManager()

    def obtener_alumnos(self):

        # Definimos la consulta para traer solo a los usuarios registrados como alumnos
        query = "SELECT id, nombre, apellidos FROM personas WHERE rol = 'alumno'"

        # Ejecutamos la consulta y devolvemos la lista de alumnos
        return self.db.fetch_all(query)


    def obtener_notas_alumno(self, id_alumno):

        # Consulta SQL con JOIN para obtener el nombre de la asignatura desde otra tabla
        query = """
            SELECT a.nombre, c.nota, c.convocatoria, c.anio 
            FROM calificaciones c
            JOIN asignaturas a ON c.id_asignatura = a.id
            WHERE c.id_alumno = ?
        """

        # Ejecutamos la consulta pasando el ID del alumno como parámetro seguro
        return self.db.fetch_all(query, (id_alumno,))


    def exportar_csv(self, nombre_alumno, notas):

        # Generamos un nombre de archivo dinámico basado en el nombre del alumno
        filename = f"notas_{nombre_alumno.replace(' ', '_')}.csv"

        try:

            # Abrimos el archivo en modo escritura con codificación UTF-8
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Escribimos la fila de encabezados del CSV
                writer.writerow(['Asignatura', 'Nota', 'Convocatoria', 'Año'])

                # Escribimos todas las filas de notas obtenidas de la consulta
                writer.writerows(notas)

            # Retornamos mensaje de éxito si el archivo se creó correctamente
            return f"Éxito: Exportado como {filename}"

        except Exception as e:

            # Capturamos cualquier error
            return f"Error al exportar: {e}"
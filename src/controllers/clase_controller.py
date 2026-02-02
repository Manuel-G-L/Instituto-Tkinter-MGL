from ..models.clase import Clase

class ClaseController:

    # Función para crear una clase
    def programar_clase(self, id_profesor, id_aula, id_asignatura, anio):

        # Une todas las entidades para crear una clase
        try:

            # Validaciones básicas
            if not all([id_profesor, id_aula, id_asignatura, anio]):
                return "Error: Faltan datos para crear la clase."

            # Creamos la instancia de la clase
            nueva_clase = Clase(
                id_profesor=id_profesor,
                id_aula=id_aula,
                id_asignatura=id_asignatura,
                anio_academico=anio
            )

            nueva_clase.registrar()
            return "La clase ha sido programada en el sistema."

        except Exception as e:
            return f"No se pudo crear la clase: {e}"
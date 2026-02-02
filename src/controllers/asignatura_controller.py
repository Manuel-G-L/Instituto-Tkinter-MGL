from ..models.asignatura import Asignatura


class AsignaturaController:

    # Función para registrar una asignatura
    def registrar_asignatura(self, nombre, departamento):

        # Valida y registra una nueva asignatura
        try:

            # Validación de errores
            if not nombre.strip() or not departamento.strip():
                return "Error: Todos los campos son obligatorios."

            # Creamos el objeto del modelo
            nueva_asig = Asignatura(nombre=nombre, departamento=departamento)

            # Llamamos al metodo del modelo para guardar
            nueva_asig.registrar()
            return f"Éxito: La asignatura '{nombre}' ha sido registrada."

        except Exception as e:
            return f"Error en el controlador: {str(e)}"

    # Función para actualizar una asignatura
    def actualizar_asignatura(self, id_asig, nombre, departamento):

        # Modifica una asignatura existente
        if not id_asig:
            return "Error: No se ha seleccionado ninguna asignatura."

        asig = Asignatura(id_asig=id_asig, nombre=nombre, departamento=departamento)
        asig.modificar()
        return "Asignatura modificada correctamente."
from ..models.materiales import Material

class MaterialController:

    # Función para añadir materiales
    def añadir_material_manual(self, nombre, id_aula):

        # Añade un material suelto a un aula
        if not nombre or not id_aula:
            return "Error: Indica el nombre del material y el aula."

        nuevo_mat = Material(nombre=nombre, aula_id=id_aula)
        nuevo_mat.registrar()
        return "Material registrado con éxito."

    # Función para cargar materiales desde un fichero
    def cargar_materiales_desde_fichero(self, ruta_archivo, id_aula):

        # Importación de materiales desde un archivo
        # Se asocia cada material del archivo al ID del aula seleccionada

        try:

            # Usamos el metodo estático que definimos en el modelo
            resultado = Material.importar_desde_archivo(ruta_archivo, id_aula)

            if resultado:
                return "Importación completada correctamente."
            else:
                return "Error al leer el archivo de materiales."

        except Exception as e:
            return f"Error crítico en la carga: {e}"
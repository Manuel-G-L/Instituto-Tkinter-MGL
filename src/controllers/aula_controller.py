from src.models.aula import Aula

class AulaController:
    def crear_aula(self, numero, capacidad):
        try:

            # Validar que capacidad sea un número
            cap_int = int(capacidad)

            # Crear el objeto modelo
            nueva_aula = Aula(numero=numero, capacidad=cap_int)

            # Llamar al metodo registrar del modelo (que usa DatabaseManager)
            id_generado = nueva_aula.registrar()

            if id_generado:
                return f"Éxito: Aula guardada con el ID {id_generado}"
            else:
                return "Error: No se pudo insertar en la base de datos."

        except ValueError:
            return "Error: La capacidad debe ser un número entero."
        except Exception as e:
            return f"Error inesperado: {str(e)}"
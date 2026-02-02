from ..models.alumno import Alumno
from ..models.profesor import Profesor
from ..models.direccion import Direccion
from ..models.persona import Persona

class PersonaController:

    def __init__(self):
        pass

    # Función crear persona
    def crear_persona(self, datos):

        # 'datos' es un diccionario que viene de la interfaz (Vista).
        try:

            # Validaciones básicas
            if not datos.get('nombre') or not datos.get('apellidos'):
                return "Error: Nombre y apellidos son obligatorios."

            if "@" not in datos.get('email', ''):
                return "Error: El formato del email es incorrecto."



            # Lógica de creación según el Rol
            rol = datos.get('rol').lower()

            if rol == 'alumno':
                nueva_persona = Alumno(
                    nombre=datos['nombre'],
                    apellidos=datos['apellidos'],
                    email=datos['email'],
                    matricula=datos.get('matricula', 'PENDIENTE')
                )

            elif rol == 'profesor':
                nueva_persona = Profesor(
                    nombre=datos['nombre'],
                    apellidos=datos['apellidos'],
                    email=datos['email'],
                    departamento=datos.get('departamento', 'General')
                )

            elif rol == 'direccion':
                nueva_persona = Direccion(
                    nombre=datos['nombre'],
                    apellidos=datos['apellidos'],
                    email=datos['email'],
                    departamento=datos.get('departamento', 'Gerencia'),
                    cargo=datos.get('cargo', 'Vocal')
                )

            else:
                return "Error: Rol no reconocido."



            # Guardar en el modelo
            nueva_persona.registrar()
            return f"Rol {rol.capitalize()} registrado correctamente."

        except Exception as e:

            # Gestión de errores
            return f"Error crítico al procesar la persona: {str(e)}"



    # Función eliminar Persona
    def eliminar_persona(self, id_persona):

        # Llamada simple para eliminar mediante el ID
        # Comprobación de error
        if not id_persona:
            return "Error: No se ha seleccionado a nadie para eliminar."

        # Usamos la clase base para eliminar ya que solo necesitamos el ID
        p = Persona(id_persona=id_persona)
        p.eliminar()
        return "Registro eliminado correctamente."
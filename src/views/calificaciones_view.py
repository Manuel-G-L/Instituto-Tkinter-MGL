import customtkinter as ctk
from tkinter import messagebox
from src.controllers.calificaciones_controller import CalificacionesController

class CalificacionesView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana (Título y tamaño)
        self.title("Panel de Calificaciones")
        self.geometry("600x500")

        # Instanciamos el controlador para acceder a los datos
        self.controller = CalificacionesController()

        # Cargamos la lista de alumnos y establecemos el índice inicial para la navegación
        self.alumnos = self.controller.obtener_alumnos()
        self.indice_actual = 0

        # --- ELEMENTOS DE LA INTERFAZ (UI) ---

        # Etiqueta de título principal
        self.label_titulo = ctk.CTkLabel(self, text="CALIFICACIONES", font=("Roboto", 20, "bold"))
        self.label_titulo.pack(pady=10)

        # Etiqueta dinámica que mostrará el nombre del alumno seleccionado
        self.label_alumno = ctk.CTkLabel(self, text="", font=("Roboto", 16, "italic"))
        self.label_alumno.pack(pady=5)

        # Contenedor de texto para simular la tabla de notas (con scroll)
        self.txt_notas = ctk.CTkTextbox(self, width=500, height=200)
        self.txt_notas.pack(pady=10)

        # Contenedor (Frame) para agrupar los botones de navegación
        self.nav_frame = ctk.CTkFrame(self)
        self.nav_frame.pack(pady=20)

        # Botón para ir al alumno anterior en la lista
        self.btn_ant = ctk.CTkButton(self.nav_frame, text="<< Anterior", command=self.anterior_alumno)
        self.btn_ant.grid(row=0, column=0, padx=10)

        # Botón para ir al alumno siguiente en la lista
        self.btn_sig = ctk.CTkButton(self.nav_frame, text="Siguiente >>", command=self.siguiente_alumno)
        self.btn_sig.grid(row=0, column=1, padx=10)

        # Botón para exportar los datos actuales a un archivo CSV
        self.btn_exportar = ctk.CTkButton(self, text="Exportar a CSV", fg_color="darkblue", command=self.exportar)
        self.btn_exportar.pack(pady=10)

        # Lógica inicial: si hay alumnos, mostramos el primero; si no, avisamos al usuario
        if self.alumnos:
            self.mostrar_alumno()
        else:
            self.txt_notas.insert("0.0", "No hay alumnos registrados.")

    def mostrar_alumno(self):

        # Obtenemos los datos del alumno según el índice de navegación
        alumno = self.alumnos[self.indice_actual]
        id_al, nombre, apellidos = alumno

        # Actualizamos la etiqueta con el nombre completo
        self.label_alumno.configure(text=f"Alumno: {nombre} {apellidos} (ID: {id_al})")

        # Solicitamos las notas al controlador
        notas = self.controller.obtener_notas_alumno(id_al)

        # Limpiamos el cuadro de texto y escribimos la cabecera formateada
        self.txt_notas.delete("0.0", "end")
        header = f"{'ASIGNATURA':<20} | {'NOTA':<5} | {'CONVOCATORIA':<12} | {'AÑO':<10}\n"
        self.txt_notas.insert("end", header + "-" * 60 + "\n")

        # Iteramos sobre las notas para insertarlas línea a línea en el cuadro de texto
        for n in notas:
            linea = f"{n[0]:<20} | {n[1]:<5} | {n[2]:<12} | {n[3]:<10}\n"
            self.txt_notas.insert("end", linea)

    def siguiente_alumno(self):
        if self.indice_actual < len(self.alumnos) - 1:
            self.indice_actual += 1
            self.mostrar_alumno()

    def anterior_alumno(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_alumno()

    def exportar(self):
        alumno = self.alumnos[self.indice_actual]
        notas = self.controller.obtener_notas_alumno(alumno[0])

        # Llamada al controlador para manejar la creación del archivo físico
        res = self.controller.exportar_csv(f"{alumno[1]}_{alumno[2]}", notas)

        # Mostramos el resultado de la operación (éxito o error)
        messagebox.showinfo("Exportar", res)
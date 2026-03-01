import customtkinter as ctk
from tkinter import messagebox
from database.database_manager import DatabaseManager
from src.views.main_menu_view import MainMenuView


class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- CONFIGURACIÓN DE LA VENTANA ---
        self.title("Sistema de Gestión Escolar - Login")
        self.geometry("400x500")

        # Inicializamos el gestor de base de datos
        self.db = DatabaseManager()

        # Configuración de pesos para que los elementos se centren horizontalmente
        self.grid_columnconfigure(0, weight=1)

        # --- ELEMENTOS DE LA INTERFAZ (UI) ---

        # Título del encabezado
        self.label = ctk.CTkLabel(self, text="INICIO DE SESIÓN", font=("Roboto", 24, "bold"))
        self.label.grid(row=0, column=0, padx=20, pady=40)

        # Campo de entrada para el Email
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Correo electrónico", width=250)
        self.username_entry.grid(row=1, column=0, padx=20, pady=10)

        # Campo de entrada para la Contraseña (en este proyecto usamos el ID de la persona)
        # El parámetro show="*" oculta los caracteres escritos
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Contraseña (ID)", show="*", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=10)

        # Botón para activar la función de login
        self.login_button = ctk.CTkButton(self, text="Entrar", command=self.ejecutar_login)
        self.login_button.grid(row=3, column=0, padx=20, pady=30)

    # --- LÓGICA DE NEGOCIO ---

    def ejecutar_login(self):

        # Obtenemos los valores de los campos de texto
        email = self.username_entry.get()
        password = self.password_entry.get()

        # Validación simple: evitar campos vacíos
        if not email or not password:
            messagebox.showwarning("Atención", "Por favor, rellena todos los campos")
            return

        # Consulta SQL: Buscamos un registro que coincida con el email y el ID (contraseña)
        query = "SELECT nombre FROM personas WHERE email = ? AND id = ?"

        # Usamos fetch_all del DatabaseManager pasando los parámetros de forma segura
        resultado = self.db.fetch_all(query, (email, password))

        # Evaluación del resultado
        if resultado:

            # Si hay coincidencia, recuperamos el nombre para el saludo
            nombre_usuario = resultado[0][0]
            messagebox.showinfo("Login correcto", f"Bienvenido/a {nombre_usuario}")

            # Transición al Menú Principal
            self.destroy()  # Cerramos la ventana de Login

            # Lanzamos la instancia del Menú Principal pasando el nombre del usuario
            app_menu = MainMenuView(usuario_nombre=nombre_usuario)
            app_menu.mainloop()

        else:
            # Si no hay coincidencia, informamos al usuario
            messagebox.showerror("Error", "Correo o ID incorrectos.\n(Prueba con admin@instituto.com e ID 1)")


if __name__ == "__main__":

    # Este bloque permite ejecutar el login de forma independiente para pruebas
    app = LoginView()
    app.mainloop()
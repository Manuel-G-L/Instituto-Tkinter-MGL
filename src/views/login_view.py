import customtkinter as ctk
from tkinter import messagebox
from database.database_manager import DatabaseManager
from src.views.main_menu_view import MainMenuView


class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión Escolar - Login")
        self.geometry("400x500")  # Corregido el (x) por x

        # Inicializamos la conexión a DB
        self.db = DatabaseManager()

        # Configuración de la interfaz
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="INICIO DE SESIÓN", font=("Roboto", 24, "bold"))
        self.label.grid(row=0, column=0, padx=20, pady=40)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Correo electrónico", width=250)
        self.username_entry.grid(row=1, column=0, padx=20, pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Contraseña (ID)", show="*", width=250)
        self.password_entry.grid(row=2, column=0, padx=20, pady=10)

        # El botón ahora llama a la función corregida
        self.login_button = ctk.CTkButton(self, text="Entrar", command=self.ejecutar_login)
        self.login_button.grid(row=3, column=0, padx=20, pady=30)

    def ejecutar_login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        # Validación simple de campos vacíos
        if not email or not password:
            messagebox.showwarning("Atención", "Por favor, rellena todos los campos")
            return

        # Consulta a la base de datos
        # Buscamos por email e ID (que actúa como contraseña en este ejercicio)
        query = "SELECT nombre FROM personas WHERE email = ? AND id = ?"
        resultado = self.db.fetch_all(query, (email, password))

        if resultado:
            nombre_usuario = resultado[0][0]
            messagebox.showinfo("Login correcto", f"Bienvenido/a {nombre_usuario}")

            # SALTO AL MENÚ PRINCIPAL
            self.destroy()  # Cerramos el login
            app_menu = MainMenuView(usuario_nombre=nombre_usuario)
            app_menu.mainloop()
        else:
            messagebox.showerror("Error", "Correo o ID incorrectos.\n(Prueba con admin@instituto.com e ID 1)")


if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
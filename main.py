import customtkinter as ctk
from src.views.login_view import LoginView # Importación directa
from database.database_manager import DatabaseManager
from database.database_manager import DatabaseManager

def inicializar_programa():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Inicializamos la DB para asegurar que las tablas existen
    db = DatabaseManager()

    # Lanzamos el Login
    app = LoginView()
    app.mainloop()

if __name__ == "__main__":
    inicializar_programa()
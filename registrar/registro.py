import sqlite3
import os

# --- Ruta de la base de datos ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # sube un nivel desde /registrar
DB_PATH = os.path.join(BASE_DIR, "database", "mi_base_de_datos.db")

# --- Función para registrar un usuario ---
def registrar_usuario_bd(nombre, correo, telefono):
    """Inserta un usuario en la base de datos"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nombre, correo, telefono)
        VALUES (?, ?, ?)
    """, (nombre, correo, telefono))

    conexion.commit()
    conexion.close()
    print("✅ Usuario registrado con éxito")


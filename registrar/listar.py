# registrar/listar.py
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # validar-usuario/
DB_PATH = os.path.join(BASE_DIR, "database", "mi_base_de_datos.db")

def obtener_usuarios():
    """Devuelve una lista de tuplas (id, nombre, correo, telefono)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, correo, telefono FROM usuarios ORDER BY id DESC")
    usuarios = cur.fetchall()
    conn.close()
    return usuarios

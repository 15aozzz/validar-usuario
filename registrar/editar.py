# registrar/editar.py
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "mi_base_de_datos.db")

def obtener_usuario_por_id(user_id):
    """Devuelve la tupla (id, nombre, correo, telefono) o None si no existe."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, correo, telefono FROM usuarios WHERE id = ?", (user_id,))
    usuario = cur.fetchone()
    conn.close()
    return usuario

def actualizar_usuario(user_id, nombre, correo, telefono):
    """
    Actualiza un usuario.
    Retorna True si fue exitoso, False si hubo IntegrityError (ej. correo duplicado).
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE usuarios SET nombre = ?, correo = ?, telefono = ? WHERE id = ?",
            (nombre, correo, telefono, user_id)
        )
        conn.commit()
        ok = True
    except sqlite3.IntegrityError:
        conn.rollback()
        ok = False
    finally:
        conn.close()
    return ok

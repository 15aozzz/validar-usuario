import sqlite3

# Solo el nombre del archivo, sin "database/"
conexion = sqlite3.connect("mi_base_de_datos.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    telefono TEXT
)
""")

conexion.commit()
conexion.close()

print("Base de datos y tabla creada dentro de database/ correctamente")
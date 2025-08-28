import os
from flask import Flask, render_template, request, redirect
import sqlite3
from usuarios.validacion import validar_nombre, validar_correo, validar_telefono

# Ruta absoluta de la carpeta templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

# Ruta principal: formulario
@app.route('/')
def index():
    return render_template("index.html", errores=None, datos={})

# Ruta para registrar usuario
@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']

    errores = []

    # Validaciones
    if validar_nombre(nombre):
        errores.append(validar_nombre(nombre))
    if validar_correo(correo):
        errores.append(validar_correo(correo))
    if validar_telefono(telefono):
        errores.append(validar_telefono(telefono))

    datos = {'nombre': nombre, 'correo': correo, 'telefono': telefono}

    if errores:
        return render_template("index.html", errores=errores, datos=datos)

    # Conectar a la base de datos dentro de database/
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'mi_base_de_datos.db'))
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    # Crear la tabla si no existe (por seguridad)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            telefono TEXT
        )
    """)
    conexion.commit()

    try:
        # Insertar usuario
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, telefono) VALUES (?, ?, ?)",
            (nombre, correo, telefono)
        )
        conexion.commit()
        conexion.close()
        return redirect('/')
    except sqlite3.IntegrityError:
        conexion.close()
        errores.append("El correo ya está registrado.")
        return render_template("index.html", errores=errores, datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
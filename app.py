from flask import Flask, render_template, redirect, url_for, request

# Importamos las funciones desde registrar/
from registrar.registro import registrar_usuario_bd
from registrar.listar import obtener_usuarios
from registrar.editar import obtener_usuario_por_id, actualizar_usuario
from registrar.eliminar import eliminar_usuario_bd

app = Flask(__name__)

# -------------------- RUTAS --------------------

# Página principal → formulario de registro
@app.route("/")
def index():
    return render_template("index.html")

# Registrar usuario (CREATE)
@app.route("/registrar", methods=["POST"])
def registrar_usuario():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]

    registrar_usuario_bd(nombre, correo, telefono)  # 👉 Inserta en DB
    return redirect(url_for("listar_usuarios"))

# Listar usuarios (READ)
@app.route("/usuarios")
def listar_usuarios():
    usuarios = obtener_usuarios()  # 👉 SELECT * FROM usuarios
    return render_template("listar.html", usuarios=usuarios)

# Editar usuario (UPDATE)
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):
    if request.method == "GET":
        usuario = obtener_usuario_por_id(id)  # 👉 SELECT con WHERE id
        return render_template("editar.html", usuario=usuario)

    # Si es POST → actualizar
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]

    actualizar_usuario(id, nombre, correo, telefono)  # 👉 UPDATE
    return redirect(url_for("listar_usuarios"))

# Eliminar usuario (DELETE)
@app.route("/eliminar/<int:id>")
def eliminar_usuario(id):
    eliminar_usuario_bd(id)  # 👉 DELETE
    return redirect(url_for("listar_usuarios"))

# -------------------- MAIN --------------------
if __name__ == "__main__":
    app.run(debug=True)

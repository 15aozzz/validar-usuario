import re

def validar_nombre(nombre):
    if not nombre:
        return "El nombre no puede estar vacío."
    return None

def validar_correo(correo):
    # Validación del correo (debe tener formato correcto)
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(patron, correo):
        return "El correo debe tener un formato válido."
    return None

def validar_telefono(telefono):
    # Validación del teléfono (debe tener prefijo internacional y números)
    patron = r'^\+\d{1,3}\s\d{9,15}$'  # Ejemplo: +34 123456789
    if not re.match(patron, telefono):
        return "El teléfono debe tener un formato válido con prefijo internacional."
    return None

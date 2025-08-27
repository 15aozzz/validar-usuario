import sys
import os

# Añadir la ruta de la carpeta raíz (validar-usuario) al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from usuarios.validacion import validar_nombre, validar_correo, validar_telefono

class TestValidaciones(unittest.TestCase):

    def test_validar_nombre(self):
        # Test del nombre vacío y correcto
        self.assertIsNone(validar_nombre("Juan"))
        self.assertEqual(validar_nombre(""), "El nombre no puede estar vacío.")

    def test_validar_correo(self):
        # Test de correos válidos e inválidos
        self.assertIsNone(validar_correo("correo@dominio.com"))
        self.assertEqual(validar_correo("correo@dominio"), "El correo debe tener un formato válido.")
        self.assertEqual(validar_correo("correo@.com"), "El correo debe tener un formato válido.")
        self.assertEqual(validar_correo("correo@dominiocom"), "El correo debe tener un formato válido.")

    def test_validar_telefono(self):
        # Test de teléfonos válidos e inválidos
        self.assertIsNone(validar_telefono("+34 123456789"))
        self.assertEqual(validar_telefono("123456789"), "El teléfono debe tener un formato válido con prefijo internacional.")
        self.assertEqual(validar_telefono("+34123456789"), "El teléfono debe tener un formato válido con prefijo internacional.")
        self.assertEqual(validar_telefono("+34 123"), "El teléfono debe tener un formato válido con prefijo internacional.")

if __name__ == "__main__":
    unittest.main()

"""
===========================================================
ASIGNATURA:        PRUEBAS DE SOFTWARE
TÍTULO:            Pruebas Unitarias con Pytest 
N° PRÁCTICA:       03
AÑO LECTIVO:       2026
SEMESTRE:          VII
FECHA ENTREGA:     05/05/2026

INTEGRANTES:
- Quispe Flores Marco Ramiro
- Quispe Madariaga Jeferson Jofre
- Ramirez Ccahuana Max Edu
- Valdiviezo Tovar Alexander

DESCRIPCIÓN:
Este código realiza pruebas unitarias para validar el funcionamiento de la 
función `validar_contrasena`. Las pruebas verifican que una contraseña cumpla 
con criterios de seguridad, como longitud mínima, uso de mayúsculas, 
minúsculas, dígitos y caracteres especiales. Además, se evalúan casos inválidos 
y contraseñas débiles para asegurar el correcto comportamiento del sistema.
===========================================================
"""

import pytest
from validador import validar_contrasena

def test_contrasena_valida():
    resultado = validar_contrasena("Segura#1")
    assert resultado["valida"] is True
    assert resultado["errores"] == []

def test_contrasena_muy_corta():
    resultado = validar_contrasena("Ab1!")
    assert resultado["valida"] is False
    assert "longitud" in resultado["errores"]

def test_sin_mayuscula():
    resultado = validar_contrasena("segura#1")
    assert resultado["valida"] is False
    assert "mayuscula" in resultado["errores"]

def test_sin_minuscula():
    resultado = validar_contrasena("SEGURA#1")
    assert resultado["valida"] is False
    assert "minuscula" in resultado["errores"]


def test_sin_digito():
    resultado = validar_contrasena("Segura##")
    assert resultado["valida"] is False
    assert "digito" in resultado["errores"]

def test_sin_caracter_especial():
    resultado = validar_contrasena("Segura12")
    assert resultado["valida"] is False
    assert "especial" in resultado["errores"]

def test_contrasena_vacia():
    resultado = validar_contrasena("")
    assert resultado["valida"] is False
    assert len(resultado["errores"]) >= 4

@pytest.mark.parametrize("contrasena", [
    "abc",
    "password",
    "ABCDEFGH",
    "12345678",
])

def test_contrasenas_debiles(contrasena):
    resultado = validar_contrasena(contrasena)
    assert resultado["valida"] is False

def test_contrasena_8_caracteres_valida():
    resultado = validar_contrasena("aB1!cDe2")
    assert resultado["valida"] is True
    assert resultado["errores"] == []

"""
===========================================================
ASIGNATURA:        PRUEBAS DE SOFTWARE
TÍTULO:            Desarrollo Orientado a Pruebas (TDD) y Comportamiento (BDD)
N° PRÁCTICA:       02
AÑO LECTIVO:       2026
SEMESTRE:          VII
FECHA ENTREGA:     29/04/2026

INTEGRANTES:
- Quispe Flores Marco Ramiro
- Quispe Madariaga Jeferson Jofre
- Ramirez Ccahuana Max Edu
- Valdiviezo Tovar Alexander

DESCRIPCIÓN:
Este código contiene pruebas automatizadas usando pytest para validar la función 
evaluar_rendimiento, verificando la correcta clasificación de notas, valores límite, 
entradas fuera de rango y tipos inválidos para asegurar la robustez del sistema.
===========================================================
"""

import pytest
from calificaciones import evaluar_rendimiento

def test_insuficiente():
    assert evaluar_rendimiento(8) == "Insuficiente"

def test_regular():
    assert evaluar_rendimiento(13) == "Regular"

def test_excelente():
    assert evaluar_rendimiento(18) == "Excelente"

def test_valores_limite():
    assert evaluar_rendimiento(0) == "Insuficiente"
    assert evaluar_rendimiento(10) == "Insuficiente"
    assert evaluar_rendimiento(11) == "Regular"
    assert evaluar_rendimiento(15) == "Regular"
    assert evaluar_rendimiento(16) == "Excelente"
    assert evaluar_rendimiento(20) == "Excelente"

def test_fuera_de_rango():
    with pytest.raises(ValueError):
        evaluar_rendimiento(-1)

    with pytest.raises(ValueError):
        evaluar_rendimiento(21)

def test_tipo_invalido():

    with pytest.raises(TypeError):
        evaluar_rendimiento("15")

    with pytest.raises(TypeError):
        evaluar_rendimiento(None)

    with pytest.raises(TypeError):
        evaluar_rendimiento(15.5)
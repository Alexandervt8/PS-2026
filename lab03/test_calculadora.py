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
Este código realiza pruebas unitarias para verificar el correcto funcionamiento 
de una calculadora básica. Las pruebas evalúan operaciones matemáticas como 
suma, resta, multiplicación y división, incluyendo casos normales, valores 
negativos y números decimales. Además, se validan errores como divisiones 
entre cero y argumentos inválidos, asegurando la confiabilidad del sistema.
===========================================================
"""

import pytest
from calculadora import suma, resta, multiplicacion, division

"""Pruebas unitarias para calculadora con patron Arrange-Act-Assert"""

@pytest.mark.parametrize("a, b, esperado", [
    (5, 3, 8),
    (-4, 4, 0),
    (0, 0, 0),
    (-1, -1, -2),
    (2.5, 3.5, 6.0),
])
# Test de suma
def test_suma(a, b, esperado):
    # Arrange, datos en parametrize
    # Act
    resultado = suma(a, b)
    # Assert
    assert resultado == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (10, 3, 7),
    (3, 10, -7),
    (7, -3, 10),
    (0, 0, 0),
    (-1, -1, 0),
])
# Test de resta
def test_resta(a, b, esperado):
    # Arrange, datos en parametrize
    # Act
    resultado = resta(a, b)
    # Assert
    assert resultado == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 6),
    (7, -3, -21),
    (5, 0, 0),
    (-1, -1, 1),
    (2.5, 4, 10.0),
])
# Test de multiplicación
def test_multiplicacion(a, b, esperado):
    # Arrange, datos en parametrize
    # Act
    resultado = multiplicacion(a, b)
    # Assert
    assert resultado == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5.0),
    (10, -2, -5.0),
    (0, 1, 0.0),
    (-4, -2, 2.0),
    (7, 2, 3.5),
])
# Test de división
def test_division(a, b, esperado):
    # Arrange, datos en parametrize
    # Act
    resultado = division(a, b)
    # Assert
    assert resultado == esperado

# Test de división por cero
def test_division_por_cero():
    with pytest.raises(ValueError):
        division(5, 0)

@pytest.mark.parametrize("operacion, a, b", [
    (suma, "a", 3),
    (resta, 5, "cinco"),
    (multiplicacion, "?", 4),
    (division, None, 2),
])
# Test de argumentos inválidos
def test_argumentos_invalidos(operacion, a, b):
    # Arrange, datos en parametrize
    # Act y Assert
    with pytest.raises(TypeError):
        operacion(a, b)
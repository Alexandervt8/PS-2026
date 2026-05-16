"""
===========================================================
ASIGNATURA:        PRUEBAS DE SOFTWARE
TÍTULO:            Depuración y Pruebas de Software
N° PRÁCTICA:       01
AÑO LECTIVO:       2026
SEMESTRE:          VII
FECHA ENTREGA:     22/04/2026

INTEGRANTES:
- Quispe Flores Marco Ramiro
- Quispe Madariaga Jeferson Jofre
- Ramirez Ccahuana Max Edu
- Valdiviezo Tovar Alexander

DESCRIPCIÓN:
El presente código fue desarrollado por los integrantes del grupo
como parte de la práctica académica, aplicando conceptos de pruebas
de software y aseguramiento de calidad.

Se implementan funciones de prueba para verificar la correcta clasificación
de números como pares o impares, así como la validación de la cantidad
y tipo de datos ingresados por el usuario, evaluando tanto casos
válidos como inválidos para garantizar el correcto funcionamiento
del sistema.
"""

from numbers import par_impar, verifCantidad, verifNumero

def test_par_impar():
    """
    Test para la clasificación correcta de números como pares o impares.
    """

    print("\nTest clasificación de par impar en los números (1, -2 y 3)")

    esperado = [(1, "impar"), (-2, "par"), (3, "impar")]
    print("Resultado esperado: ", esperado)

    resultado = par_impar([1, -2, 3])
    print("Resultado obtenido:", resultado)

    assert resultado == esperado
    print("Test de clasificación par o impar correcto")


def test_verifCantidad():
    """
    Test para la verificación de la cantidad de números ingresados.
    Casos válidos e inválidos
    """

    print("\nTest cantidad válida (5):")
    print("Resultado:", verifCantidad("5"))
    assert verifCantidad("5") == 5

    print("\nTest cantidad inválida (0):")
    print("Resultado:", verifCantidad("0"))
    assert "Cantidad inválida" in verifCantidad("0")

    print("\nTest cantidad inválida (-3):")
    print("Resultado:", verifCantidad("-3"))
    assert "Cantidad inválida" in verifCantidad("-3")

    print("\nTest cantidad inválida (texto 'abc'):")
    print("Resultado:", verifCantidad("abc"))
    assert "Cantidad inválida" in verifCantidad("abc")

    print("Test de validación de cantidad correcto")


def test_verifNumero():
    """
    Test para la verificación de números que son ingresados.
    Casos válidos e inválidos.
    """

    print("\nTest número válido (10):")
    print("Resultado:", verifNumero("10"))
    assert verifNumero("10") == 10

    print("\nTest número válido (-7):")
    print("Resultado:", verifNumero("-7"))
    assert verifNumero("-7") == -7

    print("\nTest número inválido (decimal 2.5):")
    print("Resultado:", verifNumero("2.5"))
    assert "Número inválido" in verifNumero("2.5")

    print("\nTest número inválido (texto 'abc'):")
    print("Resultado:", verifNumero("abc"))
    assert "Número inválido" in verifNumero("abc")

    print("Test de validación de números correcto")


if __name__ == "__main__":
    test_par_impar()
    test_verifCantidad()
    test_verifNumero()

    print("\nTodas las pruebas pasaron correctamente")
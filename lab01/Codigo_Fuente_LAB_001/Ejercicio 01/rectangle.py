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

Esta función permite calcular el área de un rectángulo a partir de
los valores de base y altura ingresados por el usuario, evaluando el
correcto funcionamiento del algoritmo mediante la utilización de datos
de entrada y la verificación de resultados esperados.
===========================================================
"""

def calcularArea(base, altura):
    """
    Esta función calcula el área de un rectángulo.
    Args:
    base: La longitud de la base del rectángulo.
    altura: La longitud de la altura del rectángulo.
    Returns:
    El área del rectángulo.
    """
    return base * altura

# Solicitar al usuario la longitud de los lados
base = int(input("Ingrese la longitud de la base: "))
altura = int(input("Ingrese la longitud de la altura: "))

# Calcular el área del rectángulo
area = calcularArea(base, altura)
print(f"El área del rectángulo es: {area}") 
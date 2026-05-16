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
Este código implementa una función que evalúa el rendimiento de un estudiante 
a partir de una nota entre 0 y 20. Se validan errores como tipos de datos inválidos 
y valores fuera del rango permitido, y luego se clasifica el resultado en 
"Insuficiente", "Regular" o "Excelente". Esto asegura el correcto funcionamiento 
y la robustez del sistema ante diferentes tipos de entrada.
===========================================================
"""

def evaluar_rendimiento(nota):

    # Validación de tipo
    if not isinstance(nota, int):
        raise TypeError("La nota debe ser un número entero")

    # Validación de rango
    if not 0 <= nota <= 20:
        raise ValueError("La nota debe estar entre 0 y 20")

    # Clasificación del rendimiento
    if nota <= 10:
        return "Insuficiente"

    if nota <= 15:
        return "Regular"

    return "Excelente"
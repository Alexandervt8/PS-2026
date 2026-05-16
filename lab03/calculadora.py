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
Este código implementa operaciones matemáticas básicas como suma, resta, 
multiplicación y división, validando que los argumentos ingresados sean números. 
Además, incluye manejo de excepciones para evitar errores, como divisiones entre 
cero o el uso de datos inválidos, garantizando el correcto funcionamiento de las
operaciones.
===========================================================
"""

def suma(a, b):
    validar_argumentos(a, b)
    return a + b

def resta(a, b):
    validar_argumentos(a, b)
    return a - b

def multiplicacion(a, b):
    validar_argumentos(a, b)
    return a * b

def division(a, b):
    validar_argumentos(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def validar_argumentos(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Argumentos inválidos, solo ingresar números")
    
if __name__ == "__main__":
    try:
        print(suma(2, 3))
        print(resta(5, 2))
        print(multiplicacion(2.5, 4))
        print(division(7, 2))
        print(division(10, None))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
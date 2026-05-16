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

Este programa lee dos números (enteros o decimales) que representan 
la base y la altura de un rectángulo y calcula su área, validando que 
los valores sean positivos.
"""

def calcularArea(base, altura):
    """
    Calcula el área de un rectángulo.
    Args:
    base: Longitud de la base (número positivo).
    altura: Longitud de la altura (número positivo).
    Returns:
    El área del rectángulo.
    """
    return base * altura


def validar_rectangulo(base, altura):
    """
    Valida que la base y la altura sean positivas.
    Args:
    base: Longitud de la base.
    altura: Longitud de la altura.
    Returns:
    Una cadena de texto indicando si es válido o el error.
    """
    # Verificar que la base y altura sean positivas
    if base <= 0 or altura <= 0:
        return "Rectángulo inválido: Las longitudes de los lados deben ser positivas."
    return "Válido"


# --- Programa Principal ---
if __name__ == "__main__":
    print("Ingrese las longitudes de la base y la altura del rectángulo:")
    try:
        # Leer las entradas del usuario y convertirlas a float (permite enteros y decimales)
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        
        # Validar que los valores sean positivos
        validacion = validar_rectangulo(base, altura)
        if validacion != "Válido":
            print(validacion)
        else:
            # Llamar a la función para calcular el área
            area = calcularArea(base, altura)
            # Mostrar el resultado (si es entero, mostrarlo sin decimales)
            if area.is_integer():
                print(f"El área del rectángulo es: {int(area)}")
            else:
                print(f"El área del rectángulo es: {area}")
                
    except ValueError:
        # Manejar el caso en que la entrada no sea un número válido
        print("Error: Por favor, ingrese solo valores numéricos válidos.")
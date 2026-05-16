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
Este código implementa la función `validar_contrasena`, encargada de verificar 
si una contraseña cumple con criterios básicos de seguridad, como longitud mínima, 
uso de letras mayúsculas, minúsculas, dígitos y caracteres especiales. 
Además, devuelve un listado de errores cuando alguna condición no se cumple, 
permitiendo validar la fortaleza de las contraseñas de manera sencilla.
===========================================================
"""

def validar_contrasena(contrasena: str) -> dict:

    errores = []

    if len(contrasena) < 8:
        errores.append("longitud")

    if not any(c.isupper() for c in contrasena):
        errores.append("mayuscula")

    if not any(c.islower() for c in contrasena):
        errores.append("minuscula")

    if not any(c.isdigit() for c in contrasena):
        errores.append("digito")

    especiales = "!@#$%^&*"
    if not any(c in especiales for c in contrasena):
        errores.append("especial")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }
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
Este archivo implementa la lógica para validar identificadores, asegurando que sean 
cadenas de entre 1 y 6 caracteres, que comiencen con una letra y que el resto de 
caracteres sean alfanuméricos.
===========================================================
"""

def es_identificador_valido(nombre):
    if not isinstance(nombre, str): # Sea cadena de caracteres
        return False

    if len(nombre) < 1 or len(nombre) > 6: # caracteres [1,6]
        return False

    if not nombre[0].isalpha(): #primero como letra
        return False

    for c in nombre: #caracteres letras o numeros
        if not c.isalnum():
            return False

    return True


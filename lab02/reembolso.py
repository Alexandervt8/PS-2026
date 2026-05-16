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
Este código define la función calcular_reembolso, que determina el monto 
a devolver según el tiempo de cancelación y si el cliente es VIP, incluyendo 
validaciones básicas para evitar entradas inválidas.
===========================================================
"""

def calcular_reembolso(monto, horas, es_vip):
    if monto < 0:
        raise ValueError("Monto no válido")
        
    if horas > 72:
        return monto
    elif horas <= 72 and horas >= 24:
        return monto * 0.5
    else:
        if es_vip:
            return monto * 0.5
        else:
            return 0
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
Este código utiliza pytest para validar el comportamiento de la función calcular_reembolso, 
evaluando distintos escenarios para clientes VIP y no VIP, incluyendo valores límite de 
tiempo y manejo de errores como montos negativos.
===========================================================
"""

import pytest
from reembolso import calcular_reembolso

def test_reembolso_noVip():
    '''Pruebas para clientes no VIP'''
    #Reembolso completo
    assert calcular_reembolso(200, 73, False) == 200
    #Reembolso parcial
    assert calcular_reembolso(120, 72, False) == 60
    assert calcular_reembolso(120, 24, False) == 60
    #Reembolso cero
    assert calcular_reembolso(300, 23, False) == 0
    assert calcular_reembolso(300, 0, False) == 0

def test_reembolso_vip():
    '''Pruebas para clientes VIP'''
    #Reembolso completo
    assert calcular_reembolso(400, 73, True) == 400
    #Reembolso parcial
    assert calcular_reembolso(250, 72, True) == 125
    assert calcular_reembolso(250, 24, True) == 125
    #Reembolso parcial para VIP
    assert calcular_reembolso(500, 23, True)  == 250
    assert calcular_reembolso(500, 0, True)  == 250

def test_reembolso_monto_negativo():
    with pytest.raises(ValueError):
        calcular_reembolso(-100, 50, False)
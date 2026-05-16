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
Este código implementa la clase Atm, que permite consultar saldo, 
depositar y retirar dinero. Además, valida operaciones inválidas, 
como montos negativos o retiros mayores al saldo disponible, 
utilizando excepciones personalizadas para garantizar el correcto 
funcionamiento del sistema y servir como base para pruebas unitarias con Pytest.
===========================================================
"""

# atm.py

class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más del saldo disponible."""
    pass


class MontoInvalidoError(Exception):
    """Se lanza cuando el monto es cero o negativo."""
    pass


class Atm:
    def __init__(self, saldo_inicial=1000.0):
        if saldo_inicial < 0:
            raise MontoInvalidoError("Saldo inicial no puede ser negativo")
        self._saldo = saldo_inicial



    def consultar_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto <= 0:
            raise MontoInvalidoError("El monto debe ser mayor a cero")
        self._saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise MontoInvalidoError("El monto debe ser mayor a cero")

        if monto > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente")
 
        self._saldo -= monto
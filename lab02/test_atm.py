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
Este código simula el retiro de dinero en un cajero automático y valida su 
comportamiento mediante pruebas unitarias. La función retirar controla errores 
como montos o saldos negativos y verifica si hay fondos suficientes antes de realizar 
la operación. Las pruebas evalúan casos normales, límites y errores para asegurar el 
correcto funcionamiento del sistema.
===========================================================
"""

import unittest

def retirar(saldo, monto):
    # Se valida que el monto ingresado no sea negativo,
    # ya que no tiene sentido retirar una cantidad menor a cero
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")

    # Se verifica que el saldo inicial tampoco sea negativo,
    # porque representaría un estado inválido del sistema
    if saldo < 0:
        raise ValueError("El saldo no puede ser negativo")

    # Si el monto solicitado supera el saldo disponible,
    # la operación debe ser rechazada mostrando un mensaje
    if monto > saldo:
        return "Fondos Insuficientes"

    # Si todo es correcto, se realiza el retiro y se devuelve el nuevo saldo
    return saldo - monto


class TestATM(unittest.TestCase):

    # Caso principal basado en BDD:
    # Se comprueba que el sistema bloquee retiros cuando no hay suficiente saldo
    def test_retiro_fondos_insuficientes(self):
        saldo = 100
        monto = 150
        resultado = retirar(saldo, monto)

        self.assertEqual(resultado, "Fondos Insuficientes",
                         "Debe bloquear retiros mayores al saldo")

    # Caso normal:
    # Se verifica que un retiro valido reduzca correctamente el saldo
    def test_retiro_exitoso(self):
        saldo = 200
        monto = 50
        resultado = retirar(saldo, monto)

        self.assertEqual(resultado, 150,
                         "Debe permitir retiro si hay saldo suficiente")

    # Caso límite:
    # Se evalúa el comportamiento cuando el usuario retira todo su saldo
    def test_retiro_saldo_exacto(self):
        saldo = 100
        monto = 100
        resultado = retirar(saldo, monto)

        self.assertEqual(resultado, 0,
                         "Debe permitir retirar todo el saldo")

    # Caso especial:
    # Se comprueba que retirar 0 no altere el saldo
    def test_retiro_monto_cero(self):
        saldo = 100
        monto = 0
        resultado = retirar(saldo, monto)

        self.assertEqual(resultado, 100,
                         "Retirar 0 no debe cambiar el saldo")

    # Caso de robustez:
    # Se valida que el sistema lance un error si el monto es negativo
    def test_monto_negativo(self):
        with self.assertRaises(ValueError):
            retirar(100, -10)

    # Caso de robustez:
    # Se verifica que no se permita trabajar con un saldo inválido (negativo)
    def test_saldo_negativo(self):
        with self.assertRaises(ValueError):
            retirar(-100, 50)


if __name__ == "__main__":
    unittest.main()
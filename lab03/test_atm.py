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
Este código implementa y prueba el funcionamiento de un cajero automático 
(ATM) mediante pruebas unitarias utilizando Pytest. La clase `Atm` permite 
realizar operaciones como consultar saldo, depositar y retirar dinero, 
validando diferentes condiciones y manejando excepciones cuando ocurren 
errores.
===========================================================
"""

import pytest
from atm import Atm, SaldoInsuficienteError, MontoInvalidoError

@pytest.fixture
def atm():
    """Fixture: retorna un Atm con S/.1000 de saldo inicial."""
    return Atm(1000.0)


#-------- Pruebas: saldo, depósito y retiro válidos --------
def test_saldo_inicial(atm):
    assert atm.consultar_saldo() == 1000.0


def test_deposito_valido(atm):
    atm.depositar(500)
    assert atm.consultar_saldo() == 1500.0


def test_retiro_valido(atm):
    atm.retirar(300)
    assert atm.consultar_saldo() == 700.0


def test_retiro_total(atm):
    atm.retirar(1000)
    assert atm.consultar_saldo() == 0.0


#-------- Pruebas: excepciones --------
def test_retiro_excede(atm):
    with pytest.raises(SaldoInsuficienteError):
        atm.retirar(2000)


def test_deposito_negativo(atm):
    with pytest.raises(MontoInvalidoError):
        atm.depositar(-100)


def test_deposito_cero(atm):
    with pytest.raises(MontoInvalidoError):
        atm.depositar(0)


def test_retiro_negativo(atm):
    with pytest.raises(MontoInvalidoError):
        atm.retirar(-50)


def test_saldo_inicial_negativo():
    with pytest.raises(MontoInvalidoError):
        Atm(-500)


#-------- Pruebas: parametrizadas --------
@pytest.mark.parametrize("depositos, saldo", [
    ([100, 200, 300], 1600.0)
])
def test_depositos_multiples(atm, depositos, saldo):
    for d in depositos:
        atm.depositar(d)
    assert atm.consultar_saldo() == saldo


@pytest.mark.parametrize("retiros, saldo", [
    ([100, 200, 300], 400.0)
])
def test_retiros_multiples(atm, retiros, saldo):
    for r in retiros:
        atm.retirar(r)
    assert atm.consultar_saldo() == saldo


def test_consultar_no_modifica(atm):
    atm.consultar_saldo()
    atm.consultar_saldo()
    assert atm.consultar_saldo() == 1000.0


# python -m pytest test_atm.py
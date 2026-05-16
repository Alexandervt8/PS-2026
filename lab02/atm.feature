Feature: Retiro de dinero en ATM

  Scenario: Intento de retiro con fondos insuficientes
    Given que mi saldo es 100
    When intento retirar 150
    Then debo ver un mensaje de "Fondos Insuficientes"

  Scenario: Retiro exitoso
    Given que mi saldo es 200
    When intento retirar 50
    Then el saldo final debe ser 150

  Scenario: Retiro de saldo exacto
    Given que mi saldo es 100
    When intento retirar 100
    Then el saldo final debe ser 0

  Scenario: Retiro de monto cero
    Given que mi saldo es 100
    When intento retirar 0
    Then el saldo final debe ser 100
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
Este archivo implementa pruebas unitarias con unittest para verificar si la función 
es_identificador_valido cumple con las reglas establecidas, evaluando casos válidos, 
límites de longitud, formato del primer carácter y presencia de caracteres inválidos.
===========================================================
"""

import unittest
from identificador import es_identificador_valido

class TestIdentificador(unittest.TestCase):

        #tener entre 1 y 6 caracteres
        #el primer caracter debe ser una letra
        #los demas caracteres pueden ser letras o numeros

    def test_escenario_valido(self):
         
        self.assertTrue(es_identificador_valido("abc123"))
        self.assertTrue(es_identificador_valido("a1"))

    def test_escenario_longitud(self):  #valores entre limites [1, 6]
        self.assertFalse(es_identificador_valido(""))        # 0
        self.assertTrue(es_identificador_valido("a"))        # 1 minimo
        self.assertTrue(es_identificador_valido("abcdef"))   # 6 maximo
        self.assertFalse(es_identificador_valido("abcdefg")) # 7

    def test_escenario_primer_caracter_como_letra(self): #primer caracter como letra
        self.assertFalse(es_identificador_valido("1abc"))    # 1

    def test_escenario_caracteres_invalidos(self): #caracteres restantes pueden ser letras o numeros
        self.assertFalse(es_identificador_valido("ab$12"))   # $
        self.assertTrue(es_identificador_valido("abc12"))    # caracteres validos

unittest.main()
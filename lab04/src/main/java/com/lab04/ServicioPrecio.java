/*
===========================================================
ASIGNATURA:        PRUEBAS DE SOFTWARE
TÍTULO:            Pruebas Unitarias con JUnit 5 y Mockito
N° PRÁCTICA:       04
AÑO LECTIVO:       2026
SEMESTRE:          VII
FECHA ENTREGA:     15/05/2026

INTEGRANTES:
- Quispe Flores Marco Ramiro
- Quispe Madariaga Jeferson Jofre
- Ramirez Ccahuana Max Edu
- Valdiviezo Tovar Alexander

DESCRIPCIÓN:
Este archivo define la interfaz ServicioPrecio, utilizada 
para abstraer las operaciones de cálculo de descuentos e 
impuestos aplicados al carrito de compras. Su propósito es 
permitir la inyección de dependencias y facilitar el uso de 
Mockito durante las pruebas unitarias, simulando servicios 
externos de cálculo de precios sin depender de implementaciones 
reales.
===========================================================
*/

package com.lab04;

public interface ServicioPrecio {
    double calcularDescuento(double subtotal);
    double calcularImpuesto(double montoConDescuento);
}

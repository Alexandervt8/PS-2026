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
Este archivo define el enumerador TipoMovimiento, utilizado 
para representar los tipos de operaciones posibles dentro 
del sistema de inventario. Los valores ENTRADA y SALIDA 
permiten identificar si un movimiento corresponde al ingreso 
de productos al stock o a la extracción de productos del 
inventario, facilitando el registro y control de operaciones.
===========================================================
*/

package pe.com.lab04;

public enum TipoMovimiento {
    ENTRADA,
    SALIDA
}

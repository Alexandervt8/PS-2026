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
Este archivo implementa la clase Movimiento, encargada de 
representar cada operación realizada sobre el inventario. 
La clase registra el tipo de movimiento (entrada o salida), 
la cantidad afectada y la fecha y hora en que se realizó la 
operación mediante LocalDateTime. Además, incluye validaciones 
para garantizar que el tipo de movimiento no sea nulo y que 
la cantidad registrada sea mayor a cero.
===========================================================
*/

package pe.com.lab04;

import java.time.LocalDateTime;

public class Movimiento {
    private TipoMovimiento tipo;
    private int cantidad;
    private LocalDateTime fecha;

    public Movimiento(TipoMovimiento tipo, int cantidad) {
        
        if (tipo == null) {
            throw new IllegalArgumentException("El tipo de movimiento no puede ser nulo");
        }
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad debe ser mayor a cero");
        }

        this.tipo = tipo;
        this.cantidad = cantidad;
        this.fecha = LocalDateTime.now();
    }

    public TipoMovimiento getTipo() {
        return tipo;
    }

    public int getCantidad() {
        return cantidad;
    }

    public LocalDateTime getFecha() {
        return fecha;
    }
}

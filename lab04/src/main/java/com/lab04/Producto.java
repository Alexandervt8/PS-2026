"""
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
Este archivo implementa la clase Producto, utilizada para 
representar los productos disponibles en la tienda en línea. 
La clase almacena información como id, nombre, precio y estado 
de disponibilidad del producto. Además, incorpora validaciones 
para evitar datos inválidos, como identificadores vacíos o 
precios negativos. También redefine los métodos equals() y 
hashCode() para facilitar la comparación de productos dentro 
del carrito de compras.
===========================================================
"""

package com.lab04;

import java.util.Objects;

public class Producto {
    private final String id;
    private final String nombre;
    private final double precio;
    private final boolean disponible;

    public Producto(String id, String nombre, double precio, boolean disponible) {
        if (id == null || id.isBlank()) {
            throw new IllegalArgumentException("El id del producto no puede ser vacío");
        }
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("El nombre del producto no puede ser vacío");
        }
        if (precio < 0) {
            throw new IllegalArgumentException("El precio no puede ser negativo");
        }
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.disponible = disponible;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public double getPrecio() { return precio; }
    public boolean isDisponible() { return disponible; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Producto producto)) return false;
        return Objects.equals(id, producto.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}

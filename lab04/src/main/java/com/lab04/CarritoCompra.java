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
Este archivo implementa la clase principal CarritoCompra, 
encargada de gestionar todas las operaciones relacionadas 
con el carrito de compras de la tienda en línea. La clase 
permite agregar, remover y actualizar productos, calcular 
subtotales, descuentos, impuestos y el total final de la 
compra. También valida productos indisponibles, cantidades 
inválidas y detecta productos duplicados dentro del carrito. 
Adicionalmente, mantiene un historial de operaciones y genera 
un resumen detallado de la compra realizada.
===========================================================
"""

package com.lab04;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

public class CarritoCompra {
    private final List<ItemCarrito> items;
    private final List<String> historialOperaciones;
    private final ServicioPrecio servicioPrecio;

    public CarritoCompra(ServicioPrecio servicioPrecio) {
        if (servicioPrecio == null) {
            throw new IllegalArgumentException("El servicio de precio es obligatorio");
        }
        this.servicioPrecio = servicioPrecio;
        this.items = new ArrayList<>();
        this.historialOperaciones = new ArrayList<>();
    }

    public void agregarProducto(Producto producto, int cantidad) {
        validarProductoYCantidad(producto, cantidad);
        Optional<ItemCarrito> existente = buscarItem(producto.getId());
        if (existente.isPresent()) {
            existente.get().actualizarCantidad(existente.get().getCantidad() + cantidad);
            registrar("Producto duplicado actualizado: " + producto.getNombre());
        } else {
            items.add(new ItemCarrito(producto, cantidad));
            registrar("Producto agregado: " + producto.getNombre());
        }
    }

    public void actualizarCantidad(String idProducto, int nuevaCantidad) {
        if (nuevaCantidad <= 0) {
            throw new IllegalArgumentException("La cantidad debe ser positiva");
        }
        ItemCarrito item = buscarItem(idProducto)
                .orElseThrow(() -> new IllegalArgumentException("Producto no encontrado en el carrito"));
        item.actualizarCantidad(nuevaCantidad);
        registrar("Cantidad actualizada para producto: " + idProducto);
    }

    public void removerProducto(String idProducto) {
        boolean removido = items.removeIf(item -> item.getProducto().getId().equals(idProducto));
        if (!removido) {
            throw new IllegalArgumentException("Producto no encontrado en el carrito");
        }
        registrar("Producto removido: " + idProducto);
    }

    public void vaciar() {
        items.clear();
        registrar("Carrito vaciado");
    }

    public double calcularSubtotal() {
        return items.stream().mapToDouble(ItemCarrito::obtenerSubtotal).sum();
    }

    public double calcularTotal() {
        double subtotal = calcularSubtotal();
        if (subtotal == 0) {
            return 0;
        }
        double descuento = servicioPrecio.calcularDescuento(subtotal);
        double montoConDescuento = subtotal - descuento;
        double impuesto = servicioPrecio.calcularImpuesto(montoConDescuento);
        return montoConDescuento + impuesto;
    }

    public String obtenerResumenCompra() {
        if (items.isEmpty()) {
            return "Carrito vacío";
        }
        StringBuilder resumen = new StringBuilder("Resumen de compra:\n");
        for (ItemCarrito item : items) {
            resumen.append(item.getProducto().getNombre())
                    .append(" x ").append(item.getCantidad())
                    .append(" = ").append(item.obtenerSubtotal())
                    .append("\n");
        }
        resumen.append("Subtotal: ").append(calcularSubtotal())
               .append("\nTotal: ").append(calcularTotal());
        return resumen.toString();
    }

    public boolean contieneProducto(String idProducto) {
        return buscarItem(idProducto).isPresent();
    }

    public int obtenerCantidadItems() {
        return items.size();
    }

    public int obtenerCantidadProducto(String idProducto) {
        return buscarItem(idProducto).map(ItemCarrito::getCantidad).orElse(0);
    }

    public List<ItemCarrito> getItems() {
        return Collections.unmodifiableList(items);
    }

    public List<String> getHistorialOperaciones() {
        return Collections.unmodifiableList(historialOperaciones);
    }

    private Optional<ItemCarrito> buscarItem(String idProducto) {
        return items.stream()
                .filter(item -> item.getProducto().getId().equals(idProducto))
                .findFirst();
    }

    private void validarProductoYCantidad(Producto producto, int cantidad) {
        if (producto == null) {
            throw new IllegalArgumentException("El producto no puede ser nulo");
        }
        if (!producto.isDisponible()) {
            throw new IllegalArgumentException("No se puede agregar un producto indisponible");
        }
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad debe ser positiva");
        }
    }

    private void registrar(String operacion) {
        historialOperaciones.add(LocalDateTime.now() + " - " + operacion);
    }
}

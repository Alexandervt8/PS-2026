package com.lab04;

public interface ServicioPrecio {
    double calcularDescuento(double subtotal);
    double calcularImpuesto(double montoConDescuento);
}

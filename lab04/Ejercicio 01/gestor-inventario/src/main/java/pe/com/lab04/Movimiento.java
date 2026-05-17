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
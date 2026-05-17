package pe.com.lab04;

import java.util.ArrayList;
import java.util.List;

public class Producto {
    private String codigo;
    private String nombre;
    private double precio;
    private int cantidad;
    private List<Movimiento> movimientos;

    public Producto(String codigo, String nombre, double precio, int cantidad) {
        
        if (codigo == null || codigo.isBlank()) {
            throw new IllegalArgumentException("El codigo no puede estar vacio");
        }
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("El nombre no puede estar vacio");
        }
        if (precio <= 0) {
            throw new IllegalArgumentException("El precio debe ser positivo");
        }
        if (cantidad < 0) {
            throw new IllegalArgumentException("La cantidad no puede ser negativa");
        }

        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
        this.movimientos = new ArrayList<>();
    }

    public void agregarStock(int cantidad) {
        
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad a agregar debe ser mayor a cero");
        }

        this.cantidad += cantidad;

        movimientos.add(
            new Movimiento(
                TipoMovimiento.ENTRADA,
                cantidad
            )
        );
    }

    public void extraerStock(int cantidad) {

        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad a extraer debe ser mayor a cero");
        }

        if (cantidad > this.cantidad) {
            throw new IllegalArgumentException("Stock insuficiente");
        }

        this.cantidad -= cantidad;

        movimientos.add(
            new Movimiento(
                TipoMovimiento.SALIDA,
                cantidad
            )
        );
    }

    public int consultarStock() {
        return cantidad;
    }

    public double obtenerValorTotal() {
        return precio * cantidad;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public List<Movimiento> getMovimientos() {
        return movimientos;
    }
}
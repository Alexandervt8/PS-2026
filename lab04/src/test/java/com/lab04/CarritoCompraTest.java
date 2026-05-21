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
Este archivo contiene las pruebas unitarias desarrolladas 
para verificar el correcto funcionamiento del sistema de 
carrito de compras utilizando JUnit 5 y Mockito. Las pruebas 
cubren operaciones básicas del carrito, validaciones de 
productos y cantidades, cálculo de impuestos y descuentos, 
casos límite y manejo de excepciones. Además, se emplean 
pruebas parametrizadas, clases anidadas (@Nested) y mocks 
de Mockito para simular el comportamiento de servicios 
externos y garantizar independencia entre pruebas.
===========================================================
*/

package com.lab04;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.junit.jupiter.api.extension.ExtendWith;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("Pruebas del carrito de compras")
class CarritoCompraTest {

    @Mock
    private ServicioPrecio servicioPrecio;

    private CarritoCompra carrito;
    private Producto laptop;
    private Producto mouse;
    private Producto audifonosNoDisponibles;

    @BeforeEach
    void setUp() {
        carrito = new CarritoCompra(servicioPrecio);
        laptop = new Producto("P001", "Laptop", 2500.0, true);
        mouse = new Producto("P002", "Mouse", 80.0, true);
        audifonosNoDisponibles = new Producto("P003", "Audífonos", 150.0, false);
    }

    @Nested
    @DisplayName("Operaciones básicas sin mocks")
    class OperacionesBasicas {

        @Test
        @DisplayName("Agregar un producto disponible al carrito")
        void agregarProductoDisponible() {
            carrito.agregarProducto(laptop, 1);

            assertAll(
                    () -> assertEquals(1, carrito.obtenerCantidadItems()),
                    () -> assertTrue(carrito.contieneProducto("P001")),
                    () -> assertEquals(1, carrito.obtenerCantidadProducto("P001"))
            );
        }

        @Test
        @DisplayName("No debe agregar producto indisponible")
        void noAgregarProductoIndisponible() {
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class,
                    () -> carrito.agregarProducto(audifonosNoDisponibles, 1));

            assertEquals("No se puede agregar un producto indisponible", ex.getMessage());
        }

        @Test
        @DisplayName("No debe agregar cantidad negativa")
        void noAgregarCantidadNegativa() {
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class,
                    () -> carrito.agregarProducto(laptop, -2));

            assertEquals("La cantidad debe ser positiva", ex.getMessage());
        }

        @Test
        @DisplayName("No debe agregar cantidad cero")
        void noAgregarCantidadCero() {
            assertThrows(IllegalArgumentException.class, () -> carrito.agregarProducto(laptop, 0));
        }

        @Test
        @DisplayName("Remover producto existente")
        void removerProductoExistente() {
            carrito.agregarProducto(laptop, 1);

            carrito.removerProducto("P001");

            assertAll(
                    () -> assertEquals(0, carrito.obtenerCantidadItems()),
                    () -> assertFalse(carrito.contieneProducto("P001"))
            );
        }

        @Test
        @DisplayName("Vaciar carrito con productos")
        void vaciarCarrito() {
            carrito.agregarProducto(laptop, 1);
            carrito.agregarProducto(mouse, 2);

            carrito.vaciar();

            assertEquals(0, carrito.obtenerCantidadItems());
        }

        @Test
        @DisplayName("Actualizar cantidad de producto existente")
        void actualizarCantidadProductoExistente() {
            carrito.agregarProducto(mouse, 2);

            carrito.actualizarCantidad("P002", 5);

            assertEquals(5, carrito.obtenerCantidadProducto("P002"));
        }

        @Test
        @DisplayName("Detectar producto duplicado y sumar cantidad")
        void productoDuplicadoSumaCantidad() {
            carrito.agregarProducto(mouse, 2);
            carrito.agregarProducto(mouse, 3);

            assertAll(
                    () -> assertEquals(1, carrito.obtenerCantidadItems()),
                    () -> assertEquals(5, carrito.obtenerCantidadProducto("P002"))
            );
        }

        @Test
        @DisplayName("Registrar historial de operaciones")
        void registrarHistorialOperaciones() {
            carrito.agregarProducto(laptop, 1);
            carrito.actualizarCantidad("P001", 2);
            carrito.removerProducto("P001");

            assertAll(
                    () -> assertEquals(3, carrito.getHistorialOperaciones().size()),
                    () -> assertTrue(carrito.getHistorialOperaciones().get(0).contains("Producto agregado")),
                    () -> assertTrue(carrito.getHistorialOperaciones().get(1).contains("Cantidad actualizada")),
                    () -> assertTrue(carrito.getHistorialOperaciones().get(2).contains("Producto removido"))
            );
        }

        @Test
        @DisplayName("Obtener resumen de carrito vacío")
        void resumenCarritoVacio() {
            assertEquals("Carrito vacío", carrito.obtenerResumenCompra());
        }
    }

    @Nested
    @DisplayName("Cálculos con Mockito")
    class CalculosConMockito {

        @Test
        @DisplayName("Carrito vacío tiene total cero y no llama al servicio")
        void carritoVacioTotalCero() {
            double total = carrito.calcularTotal();

            assertEquals(0.0, total);
            verifyNoInteractions(servicioPrecio);
        }

        @Test
        @DisplayName("Calcular total con descuento e impuesto")
        void calcularTotalConDescuentoEImpuesto() {
            carrito.agregarProducto(laptop, 1);
            when(servicioPrecio.calcularDescuento(2500.0)).thenReturn(250.0);
            when(servicioPrecio.calcularImpuesto(2250.0)).thenReturn(405.0);

            double total = carrito.calcularTotal();

            assertEquals(2655.0, total);
        }

        @Test
        @DisplayName("Validar cálculo correcto solo con impuesto")
        void calcularTotalSoloConImpuesto() {
            carrito.agregarProducto(mouse, 2);
            when(servicioPrecio.calcularDescuento(160.0)).thenReturn(0.0);
            when(servicioPrecio.calcularImpuesto(160.0)).thenReturn(28.8);

            assertEquals(188.8, carrito.calcularTotal());
        }

        @Test
        @DisplayName("Validar cálculo correcto con descuento sin impuesto")
        void calcularTotalSoloConDescuento() {
            carrito.agregarProducto(mouse, 10);
            when(servicioPrecio.calcularDescuento(800.0)).thenReturn(80.0);
            when(servicioPrecio.calcularImpuesto(720.0)).thenReturn(0.0);

            assertEquals(720.0, carrito.calcularTotal());
        }

        @Test
        @DisplayName("Verificar llamadas a ServicioPrecio")
        void verificarLlamadasServicioPrecio() {
            carrito.agregarProducto(laptop, 1);
            when(servicioPrecio.calcularDescuento(2500.0)).thenReturn(100.0);
            when(servicioPrecio.calcularImpuesto(2400.0)).thenReturn(432.0);

            carrito.calcularTotal();

            verify(servicioPrecio, times(1)).calcularDescuento(2500.0);
            verify(servicioPrecio, times(1)).calcularImpuesto(2400.0);
        }

        @ParameterizedTest(name = "subtotal={0}, descuento={1}, impuesto={2}, total={3}")
        @CsvSource({
                "100.0, 0.0, 18.0, 118.0",
                "500.0, 50.0, 81.0, 531.0",
                "1000.0, 100.0, 162.0, 1062.0",
                "2000.0, 300.0, 306.0, 2006.0"
        })
        @DisplayName("Pruebas parametrizadas para diferentes montos")
        void calcularTotalesParametrizados(double subtotal, double descuento, double impuesto, double esperado) {
            Producto producto = new Producto("PX" + subtotal, "Producto", subtotal, true);
            carrito.agregarProducto(producto, 1);
            when(servicioPrecio.calcularDescuento(subtotal)).thenReturn(descuento);
            when(servicioPrecio.calcularImpuesto(subtotal - descuento)).thenReturn(impuesto);

            assertEquals(esperado, carrito.calcularTotal());
        }
    }

    @Nested
    @DisplayName("Casos límite")
    class CasosLimite {

        @Test
        @DisplayName("Carrito con un solo producto")
        void carritoConUnProducto() {
            carrito.agregarProducto(mouse, 1);
            when(servicioPrecio.calcularDescuento(80.0)).thenReturn(0.0);
            when(servicioPrecio.calcularImpuesto(80.0)).thenReturn(14.4);

            assertAll(
                    () -> assertEquals(1, carrito.obtenerCantidadItems()),
                    () -> assertEquals(94.4, carrito.calcularTotal())
            );
        }

        @Test
        @DisplayName("Carrito con 100 productos distintos")
        void carritoConCienProductos() {
            for (int i = 1; i <= 100; i++) {
                carrito.agregarProducto(new Producto("P" + i, "Producto " + i, 10.0, true), 1);
            }
            when(servicioPrecio.calcularDescuento(1000.0)).thenReturn(100.0);
            when(servicioPrecio.calcularImpuesto(900.0)).thenReturn(162.0);

            assertAll(
                    () -> assertEquals(100, carrito.obtenerCantidadItems()),
                    () -> assertEquals(1062.0, carrito.calcularTotal())
            );
        }

        @Test
        @DisplayName("No debe remover un producto inexistente")
        void noRemoverProductoInexistente() {
            assertThrows(IllegalArgumentException.class, () -> carrito.removerProducto("NO_EXISTE"));
        }

        @Test
        @DisplayName("No debe actualizar producto inexistente")
        void noActualizarProductoInexistente() {
            assertThrows(IllegalArgumentException.class, () -> carrito.actualizarCantidad("NO_EXISTE", 2));
        }

        @Test
        @DisplayName("El resumen debe incluir productos y total")
        void resumenIncluyeProductosYTotal() {
            carrito.agregarProducto(mouse, 2);
            when(servicioPrecio.calcularDescuento(160.0)).thenReturn(0.0);
            when(servicioPrecio.calcularImpuesto(160.0)).thenReturn(28.8);

            String resumen = carrito.obtenerResumenCompra();

            assertAll(
                    () -> assertTrue(resumen.contains("Resumen de compra")),
                    () -> assertTrue(resumen.contains("Mouse x 2")),
                    () -> assertTrue(resumen.contains("Subtotal: 160.0")),
                    () -> assertTrue(resumen.contains("Total: 188.8"))
            );
        }
    }
}

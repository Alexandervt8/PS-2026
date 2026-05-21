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
Este archivo implementa la clase M_Producto, utilizada para 
gestionar productos dentro del sistema de inventario. La clase 
almacena información como código, nombre, precio y cantidad 
disponible en stock. Además, incorpora validaciones para evitar 
códigos vacíos, precios no positivos y cantidades negativas. 
También permite agregar y extraer stock, calcular el valor total 
del inventario y registrar automáticamente cada movimiento de 
entrada o salida realizado sobre el producto.
===========================================================
*/

package pe.com.lab04;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

public class M_ProductoTest {

    private M_Producto producto;

    @BeforeEach
    void setUp() {
        producto = new M_Producto(
                "P001",
                "Laptop",
                2500.0,
                10
        );
    }

    @Nested
    @DisplayName("Pruebas de creación de producto")
    class CreacionProductoTest {

        @Test
        @DisplayName("Crear producto correctamente")
        void crearProductoCorrectamente() {
            assertAll(
                    () -> assertEquals("P001", producto.getCodigo()),
                    () -> assertEquals("Laptop", producto.getNombre()),
                    () -> assertEquals(2500.0, producto.getPrecio()),
                    () -> assertEquals(10, producto.consultarStock())
            );
        }

        @Test
        @DisplayName("Lanzar excepción si código está vacío")
        void lanzarExcepcionCodigoVacio() {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> new M_Producto("", "Mouse", 100, 5)
            );

            assertEquals(
                    "El codigo no puede estar vacio",
                    exception.getMessage()
            );
        }

        @Test
        @DisplayName("Lanzar excepción si nombre está vacío")
        void lanzarExcepcionNombreVacio() {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> new M_Producto("P002", "", 100, 5)
            );

            assertEquals(
                    "El nombre no puede estar vacio",
                    exception.getMessage()
            );
        }

        @Test
        @DisplayName("Lanzar excepción si precio es negativo")
        void lanzarExcepcionPrecioNegativo() {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> new M_Producto("P003", "Teclado", -10, 5)
            );

            assertEquals(
                    "El precio debe ser positivo",
                    exception.getMessage()
            );
        }

        @Test
        @DisplayName("Lanzar excepción si cantidad es negativa")
        void lanzarExcepcionCantidadNegativa() {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> new M_Producto("P004", "Monitor", 500, -1)
            );

            assertEquals(
                    "La cantidad no puede ser negativa",
                    exception.getMessage()
            );
        }
    }

    @Nested
    @DisplayName("Pruebas de agregar stock")
    class AgregarStockTest {

        @Test
        @DisplayName("Agregar stock correctamente")
        void agregarStockCorrectamente() {

            producto.agregarStock(5);

            assertEquals(15, producto.consultarStock());
        }

        @ParameterizedTest
        @ValueSource(ints = {-1, 0})
        @DisplayName("Lanzar excepción para cantidades inválidas")
        void lanzarExcepcionCantidadInvalidaAgregar(int cantidad) {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> producto.agregarStock(cantidad)
            );

            assertEquals(
                    "La cantidad a agregar debe ser mayor a cero",
                    exception.getMessage()
            );
        }
    }

    @Nested
    @DisplayName("Pruebas de extracción de stock")
    class ExtraerStockTest {

        @Test
        @DisplayName("Extraer stock correctamente")
        void extraerStockCorrectamente() {

            producto.extraerStock(3);

            assertEquals(7, producto.consultarStock());
        }

        @ParameterizedTest
        @ValueSource(ints = {-5, 0})
        @DisplayName("Lanzar excepción para extracción inválida")
        void lanzarExcepcionCantidadInvalidaExtraer(int cantidad) {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> producto.extraerStock(cantidad)
            );

            assertEquals(
                    "La cantidad a extraer debe ser mayor a cero",
                    exception.getMessage()
            );
        }

        @Test
        @DisplayName("Lanzar excepción por stock insuficiente")
        void lanzarExcepcionStockInsuficiente() {

            IllegalArgumentException exception = assertThrows(
                    IllegalArgumentException.class,
                    () -> producto.extraerStock(20)
            );

            assertEquals(
                    "Stock insuficiente",
                    exception.getMessage()
            );
        }
    }

    @Nested
    @DisplayName("Pruebas de cálculos")
    class CalculosTest {

        @Test
        @DisplayName("Calcular valor total correctamente")
        void calcularValorTotalCorrectamente() {

            double total = producto.obtenerValorTotal();

            assertEquals(25000.0, total);
        }
    }

    @Nested
    @DisplayName("Pruebas de movimientos")
    class MovimientoTest {

        @Test
        @DisplayName("Registrar movimiento de entrada")
        void registrarMovimientoEntrada() {

            producto.agregarStock(5);

            assertEquals(1, producto.getMovimientos().size());
            assertEquals(
                    TipoMovimiento.ENTRADA,
                    producto.getMovimientos().get(0).getTipo()
            );
        }

        @Test
        @DisplayName("Registrar movimiento de salida")
        void registrarMovimientoSalida() {

            producto.extraerStock(2);

            assertEquals(1, producto.getMovimientos().size());
            assertEquals(
                    TipoMovimiento.SALIDA,
                    producto.getMovimientos().get(0).getTipo()
            );
        }
    }
}
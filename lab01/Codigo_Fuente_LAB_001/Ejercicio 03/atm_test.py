"""
===========================================================
ASIGNATURA:        PRUEBAS DE SOFTWARE
TÍTULO:            Depuración y Pruebas de Software
N° PRÁCTICA:       01
AÑO LECTIVO:       2026
SEMESTRE:          VII
FECHA ENTREGA:     22/04/2026

INTEGRANTES:
- Quispe Flores Marco Ramiro
- Quispe Madariaga Jeferson Jofre
- Ramirez Ccahuana Max Edu
- Valdiviezo Tovar Alexander

DESCRIPCIÓN:
El presente código fue desarrollado por los integrantes del grupo
como parte de la práctica académica, aplicando conceptos de pruebas
de software y aseguramiento de calidad.

Este programa simula las operaciones básicas de un cajero automático.
Inicia con un saldo fijo de S/.1000 y permite consultar saldo, depositar,
retirar dinero o salir. Valida que los montos sean números positivos, 
maneja decimales y verifica saldo suficiente antes de retirar.
"""

def consultar_saldo(saldo):
    """
    Muestra el saldo actual.
    Args:
    saldo: El saldo actual de la cuenta.
    Returns:
    El saldo actual (sin cambios).
    """
    return saldo


def depositar(saldo, monto):
    """
    Actualiza el saldo sumando el monto depositado.
    Args:
    saldo: El saldo actual de la cuenta.
    monto: La cantidad a depositar (debe ser positivo).
    Returns:
    El nuevo saldo actualizado.
    """
    return saldo + monto


def retirar(saldo, monto):
    """
    Actualiza el saldo restando el monto retirado.
    Args:
    saldo: El saldo actual de la cuenta.
    monto: La cantidad a retirar (debe ser positivo y menor o igual al saldo).
    Returns:
    El nuevo saldo actualizado.
    """
    return saldo - monto


def obtener_monto_positivo(mensaje):
    """
    Solicita un monto positivo al usuario, validando entradas.
    Maneja valores no numéricos, decimales, vacíos, negativos y cero.
    Args:
    mensaje: El mensaje a mostrar al usuario.
    Returns:
    El monto válido (float).
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            
            # Validar entrada vacía
            if not entrada:
                print("Error: Por favor, ingrese un monto válido.")
                continue
            
            # Intentar convertir a float (permite enteros y decimales)
            monto = float(entrada)
            
            # Validar que sea mayor que cero
            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
                continue
            
            return monto
            
        except ValueError:
            print("Error: Por favor, ingrese un monto válido.")


def obtener_opcion_valida():
    """
    Solicita una opción válida del menú al usuario.
    Maneja entradas no numéricas, vacías y fuera de rango.
    Returns:
    La opción válida (entero del 1 al 4).
    """
    while True:
        try:
            entrada = input("Seleccione una opción: ").strip()
            
            # Validar entrada vacía
            if not entrada:
                print("Error: Por favor, seleccione una opción válida (1-4).")
                continue
            
            # Intentar convertir a entero
            opcion = int(entrada)
            
            # Validar que esté en el rango 1-4
            if opcion < 1 or opcion > 4:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
                continue
            
            return opcion
            
        except ValueError:
            print("Error: Por favor, seleccione una opción válida (1-4).")


def formatear_saldo(saldo):
    """
    Formatea el saldo para mostrarlo correctamente.
    Si es entero, muestra sin decimales; si tiene decimales, muestra con 2 decimales.
    Args:
    saldo: El saldo a formatear.
    Returns:
    El saldo formateado como string.
    """
    if saldo.is_integer():
        return f"S/.{int(saldo)}"
    else:
        return f"S/.{saldo:.2f}"


# --- Programa Principal ---
if __name__ == "__main__":
    saldo = 1000.0  # Saldo inicial fijo
    
    print("Bienvenido al cajero automático.")
    
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")
        
        opcion = obtener_opcion_valida()
        
        if opcion == 1:
            # Consultar saldo
            saldo_actual = consultar_saldo(saldo)
            print(f"Su saldo actual es: {formatear_saldo(saldo_actual)}")
        
        elif opcion == 2:
            # Depositar dinero
            monto = obtener_monto_positivo("Ingrese la cantidad a depositar: S/.")
            saldo = depositar(saldo, monto)
            print(f"Depósito exitoso. Su nuevo saldo es: {formatear_saldo(saldo)}")
        
        elif opcion == 3:
            # Retirar dinero
            monto = obtener_monto_positivo("Ingrese la cantidad a retirar: S/.")
            
            # Validar saldo suficiente
            if monto > saldo:
                print(f"Error: Saldo insuficiente. Su saldo actual es: {formatear_saldo(saldo)}")
            else:
                saldo = retirar(saldo, monto)
                print(f"Retiro exitoso. Su nuevo saldo es: {formatear_saldo(saldo)}")
        
        elif opcion == 4:
            # Salir
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
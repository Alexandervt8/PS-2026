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
retirar dinero o salir.
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
    monto: La cantidad a depositar.
    Returns:
    El nuevo saldo actualizado.
    """
    return saldo + monto


def retirar(saldo, monto):
    """
    Actualiza el saldo restando el monto retirado.
    Args:
    saldo: El saldo actual de la cuenta.
    monto: La cantidad a retirar.
    Returns:
    El nuevo saldo actualizado.
    """
    return saldo - monto


# --- Programa Principal ---
if __name__ == "__main__":
    saldo = 1000  # Saldo inicial fijo
    
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            # Consultar saldo
            saldo_actual = consultar_saldo(saldo)
            print(f"Su saldo actual es: S/.{saldo_actual}")
        
        elif opcion == 2:
            # Depositar dinero
            monto = int(input("Ingrese la cantidad a depositar: S/."))
            saldo = depositar(saldo, monto)
            print(f"Depósito exitoso. Su nuevo saldo es: S/.{saldo}")
        
        elif opcion == 3:
            # Retirar dinero
            monto = int(input("Ingrese la cantidad a retirar: S/."))
            if monto <= saldo:
                saldo = retirar(saldo, monto)
                print(f"Retiro exitoso. Su nuevo saldo es: S/.{saldo}")
            else:
                print("Error: Saldo insuficiente.")
        
        elif opcion == 4:
            # Salir
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
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

Se implementan funciones que permiten clasificar números como pares o 
impares, así como validar la cantidad de datos ingresados y verificar 
que los valores sean numéricos enteros. Además, se integran mecanismos 
de control que gestionan errores en la entrada de datos, garantizando 
un procesamiento correcto y consistente de la información proporcionada 
por el usuario.
"""

def par_impar(nums):
    """
    En esta función se clasifica en par o impar cada número n
    de la lista nums, se devuelve la lista resultado con tuplas (int,String)
    """
    resultado = []
    for n in nums:
        if n % 2 == 0:
            resultado.append((n, "par"))
        else:
            resultado.append((n, "impar"))
    return resultado


def verifCantidad(entrada):
    """
    En esta función se verifica que la cantidad de números a clasificar
    corresponda a un entero.
    """
    try:
        cantidad = int(entrada)
        if cantidad <= 0:
            return "Cantidad inválida, debe ingresar un número entero mayor que cero"
        return cantidad
    except ValueError:
        return "Cantidad inválida, debe ingresar un número entero"


def verifNumero(entrada):
    """
    En esta función se verifica que los números ingresados son enteros.
    """
    try:
        return int(entrada)
    except ValueError:
        return "Número inválido, solo se permiten números enteros"


"""
Desarrollo del programa
Se hacen uso de los verificadores y se hace uso de isinstance para saber si
lo recibido corresponde a un error e imprimirlo
"""
if __name__ == "__main__":

    nums = []

    entrada = input("Ingrese la cantidad de números a clasificar: ")
    cantidad = verifCantidad(entrada)

    if isinstance(cantidad, str):
        print(cantidad)
        exit()

    for i in range(cantidad):
        entrada = input("Ingrese número: ")
        numero = verifNumero(entrada)

        if isinstance(numero, str):
            print(numero)
            exit()

        nums.append(numero)

    procesados = par_impar(nums)

    for numero, tipo in procesados:
        print(numero, " es ", tipo)
"""
===========================================================
ASIGNATURA:        PRUEBAS DE SOFTWARE
TÍTULO:            Pruebas de Rendimiento y Seguridad en API REST
N° PRÁCTICA:       09
AÑO LECTIVO:       2026
SEMESTRE:          VII
FECHA ENTREGA:     16/07/2026

INTEGRANTES:
- Quispe Flores Marco Ramiro
- Quispe Madariaga Jeferson Jofre
- Ramirez Ccahuana Max Edu
- Valdiviezo Tovar Alexander

DESCRIPCIÓN:
Este archivo implementa pruebas básicas de seguridad sobre la API de reservas
utilizando la biblioteca Requests. Evalúa el acceso a recursos inexistentes,
el envío de campos obligatorios vacíos, los tipos de datos incorrectos y el uso
de métodos HTTP no permitidos, verificando los códigos de respuesta esperados.
===========================================================
Pruebas básicas de seguridad para la API Flask de reservas.

Uso:
    pip install requests
    python pruebas_seguridad_api.py

La API debe estar ejecutándose en http://localhost:5000.
"""

import json
import sys

import requests


BASE_URL = "http://localhost:5000"
TIMEOUT = 5


def mostrar_resultado(caso, respuesta, codigo_esperado):
    correcto = respuesta.status_code == codigo_esperado
    estado = "APROBADO" if correcto else "FALLIDO"
    try:
        cuerpo = respuesta.json()
    except ValueError:
        cuerpo = respuesta.text

    print(f"\n{caso}: {estado}")
    print(f"Código obtenido: {respuesta.status_code}")
    print(f"Código esperado: {codigo_esperado}")
    print("Respuesta:", json.dumps(cuerpo, ensure_ascii=False, indent=2))
    return correcto


def reserva_valida():
    return {
        "cliente": "Cliente de Seguridad",
        "hotel": "Hotel de Prueba",
        "tipo_habitacion": "Doble",
        "fecha_ingreso": "2026-09-10",
        "fecha_salida": "2026-09-15",
        "numero_huespedes": 2,
        "estado": "Confirmada",
    }


def caso_1_recurso_inexistente():
    respuesta = requests.get(
        f"{BASE_URL}/reservas/999999", timeout=TIMEOUT
    )
    return mostrar_resultado(
        "Caso 1 - Recurso inexistente", respuesta, 404
    )


def caso_2_datos_incompletos():
    datos = reserva_valida()
    datos["cliente"] = ""
    respuesta = requests.post(
        f"{BASE_URL}/reservas", json=datos, timeout=TIMEOUT
    )
    codigo_correcto = mostrar_resultado(
        "Caso 2 - Campo obligatorio vacío", respuesta, 400
    )
    mensaje_descriptivo = bool(respuesta.json().get("error"))
    print(
        "Mensaje descriptivo:",
        "SÍ" if mensaje_descriptivo else "NO",
    )
    return codigo_correcto and mensaje_descriptivo


def caso_3_tipo_incorrecto():
    datos = reserva_valida()
    datos["numero_huespedes"] = "ABC"
    respuesta = requests.post(
        f"{BASE_URL}/reservas", json=datos, timeout=TIMEOUT
    )
    return mostrar_resultado(
        "Caso 3 - Tipo de dato incorrecto", respuesta, 400
    )


def caso_4_metodo_no_permitido():
    respuesta = requests.patch(
        f"{BASE_URL}/reservas", json={}, timeout=TIMEOUT
    )
    return mostrar_resultado(
        "Caso 4 - Método PATCH no permitido", respuesta, 405
    )


def main():
    print("PRUEBAS BÁSICAS DE SEGURIDAD - API DE RESERVAS")
    print(f"Servidor evaluado: {BASE_URL}")
    try:
        resultados = [
            caso_1_recurso_inexistente(),
            caso_2_datos_incompletos(),
            caso_3_tipo_incorrecto(),
            caso_4_metodo_no_permitido(),
        ]
    except requests.RequestException as error:
        print(f"\nNo fue posible conectar con la API: {error}")
        print("Verifique que app.py esté en ejecución.")
        return 2

    print("\nCaso 5 - Fuerza bruta: NO APLICA")
    print("La API actual no implementa autenticación ni endpoint de inicio de sesión.")
    aprobados = sum(resultados)
    print(f"\nResultado final: {aprobados}/{len(resultados)} casos aprobados")
    return 0 if all(resultados) else 1


if __name__ == "__main__":
    sys.exit(main())


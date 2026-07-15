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

DESCRIPCION:
Programa libre para Ejercicio 1 - Pruebas de caja blanca.
Sistema simple de biblioteca con reglas de prestamo, multa y clasificacion.
===========================================================
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Usuario:
    edad: int
    es_estudiante: bool
    sancionado: bool
    prestamos_activos: int


@dataclass
class Libro:
    categoria: str
    disponible: bool
    es_referencia: bool
    copias: int


def puede_prestar(usuario: Usuario, libro: Libro, dias: int) -> str:
    """
    Evalua si un usuario puede prestar un libro.

    Decision principal para combinacion de condiciones:
    (C1 and C2) and (C3 or C4)
    C1: libro.disponible and libro.copias > 0
    C2: not usuario.sancionado
    C3: usuario.es_estudiante
    C4: dias <= 7
    """
    if dias <= 0:
        return "Dias invalidos"

    if libro.es_referencia and dias > 1:
        return "Referencia solo sala"

    if usuario.prestamos_activos >= 5:
        return "Limite de prestamos"

    c1 = libro.disponible and libro.copias > 0
    c2 = not usuario.sancionado
    c3 = usuario.es_estudiante
    c4 = dias <= 7

    if (c1 and c2) and (c3 or c4):
        if usuario.edad < 12 and libro.categoria == "adultos":
            return "Restriccion por edad"
        return "Prestamo aprobado"
    else:
        return "Prestamo rechazado"


def calcular_multa(dias_retraso: int, es_estudiante: bool, libro_perdido: bool) -> float:
    """Calcula multa por retraso o perdida."""
    if dias_retraso < 0:
        raise ValueError("dias_retraso no puede ser negativo")

    if libro_perdido:
        multa = 80.0
    elif dias_retraso == 0:
        multa = 0.0
    elif dias_retraso <= 7:
        multa = dias_retraso * 1.5
    else:
        multa = 10.5 + ((dias_retraso - 7) * 3.0)

    if es_estudiante and not libro_perdido:
        multa = multa * 0.5

    return round(multa, 2)


def clasificar_usuario(edad: int, prestamos_activos: int, sancionado: bool) -> str:
    """Clasifica al usuario para reportes internos."""
    if edad < 0:
        return "Edad invalida"

    if sancionado:
        return "Suspendido"

    if edad < 12:
        grupo = "Infantil"
    elif edad < 18:
        grupo = "Juvenil"
    elif edad < 60:
        grupo = "Adulto"
    else:
        grupo = "Senior"

    if prestamos_activos == 0:
        actividad = "sin prestamos"
    elif prestamos_activos <= 3:
        actividad = "activo"
    else:
        actividad = "intensivo"

    return f"{grupo} - {actividad}"


def generar_recomendaciones(usuario: Usuario, historial: List[str]) -> List[str]:
    """Genera recomendaciones segun edad, historial y sancion."""
    recomendaciones = []

    if usuario.sancionado:
        recomendaciones.append("Regularizar sancion")
        return recomendaciones

    if usuario.edad < 12:
        recomendaciones.append("Cuentos infantiles")
    elif usuario.edad < 18:
        recomendaciones.append("Novela juvenil")
    else:
        recomendaciones.append("Literatura general")

    if "ciencia" in historial:
        recomendaciones.append("Divulgacion cientifica")

    if usuario.es_estudiante:
        recomendaciones.append("Material academico")

    if not historial:
        recomendaciones.append("Guia de bienvenida")

    return recomendaciones

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
===========================================================
"""

# =========================================================
# 1 y 2. STATEMENT TESTING y BRANCH TESTING
# =========================================================
# Estos casos recorren todas las sentencias y ramas del programa.


def test_puede_prestar_dias_invalidos():
    usuario = Usuario(20, True, False, 0)
    libro = Libro("general", True, False, 1)
    assert puede_prestar(usuario, libro, 0) == "Dias invalidos"


def test_puede_prestar_referencia_solo_sala():
    usuario = Usuario(20, True, False, 0)
    libro = Libro("general", True, True, 1)
    assert puede_prestar(usuario, libro, 2) == "Referencia solo sala"


def test_puede_prestar_limite_prestamos():
    usuario = Usuario(20, True, False, 5)
    libro = Libro("general", True, False, 1)
    assert puede_prestar(usuario, libro, 3) == "Limite de prestamos"


def test_puede_prestar_restriccion_por_edad():
    usuario = Usuario(10, True, False, 0)
    libro = Libro("adultos", True, False, 2)
    assert puede_prestar(usuario, libro, 3) == "Restriccion por edad"


def test_puede_prestar_aprobado():
    usuario = Usuario(22, True, False, 0)
    libro = Libro("general", True, False, 2)
    assert puede_prestar(usuario, libro, 10) == "Prestamo aprobado"


def test_puede_prestar_rechazado():
    usuario = Usuario(22, False, True, 0)
    libro = Libro("general", True, False, 2)
    assert puede_prestar(usuario, libro, 3) == "Prestamo rechazado"


def test_calcular_multa_negativa():
    with pytest.raises(ValueError):
        calcular_multa(-1, False, False)


@pytest.mark.parametrize(
    "dias, estudiante, perdido, esperado",
    [
        (5, False, True, 80.0),
        (0, False, False, 0.0),
        (4, False, False, 6.0),
        (10, False, False, 19.5),
        (4, True, False, 3.0),
    ],
)
def test_calcular_multa_ramas(dias, estudiante, perdido, esperado):
    assert calcular_multa(dias, estudiante, perdido) == esperado


@pytest.mark.parametrize(
    "edad, prestamos, sancionado, esperado",
    [
        (-1, 0, False, "Edad invalida"),
        (20, 0, True, "Suspendido"),
        (8, 0, False, "Infantil - sin prestamos"),
        (15, 2, False, "Juvenil - activo"),
        (30, 4, False, "Adulto - intensivo"),
        (70, 1, False, "Senior - activo"),
    ],
)
def test_clasificar_usuario_ramas(edad, prestamos, sancionado, esperado):
    assert clasificar_usuario(edad, prestamos, sancionado) == esperado


def test_generar_recomendaciones_sancionado():
    usuario = Usuario(20, True, True, 0)
    assert generar_recomendaciones(usuario, ["ciencia"]) == ["Regularizar sancion"]


@pytest.mark.parametrize(
    "usuario, historial, esperado",
    [
        (Usuario(10, False, False, 0), [], ["Cuentos infantiles", "Guia de bienvenida"]),
        (Usuario(15, True, False, 0), ["ciencia"], ["Novela juvenil", "Divulgacion cientifica", "Material academico"]),
        (Usuario(25, False, False, 0), ["historia"], ["Literatura general"]),
    ],
)
def test_generar_recomendaciones_ramas(usuario, historial, esperado):
    assert generar_recomendaciones(usuario, historial) == esperado


# =========================================================
# 3. BRANCH CONDITION COMBINATION TESTING
# =========================================================
# Decision: (C1 AND C2) AND (C3 OR C4)
# C1: libro.disponible and libro.copias > 0
# C2: not usuario.sancionado
# C3: usuario.es_estudiante
# C4: dias <= 7
# Requisito academico: probar 16 combinaciones de V y F.


@pytest.mark.parametrize(
    "c1, c2, c3, c4, esperado, tabla",
    [
        (True, True, True, True, "Prestamo aprobado", "V-V-V-V"),
        (True, True, True, False, "Prestamo aprobado", "V-V-V-F"),
        (True, True, False, True, "Prestamo aprobado", "V-V-F-V"),
        (True, True, False, False, "Prestamo rechazado", "V-V-F-F"),
        (True, False, True, True, "Prestamo rechazado", "V-F-V-V"),
        (True, False, True, False, "Prestamo rechazado", "V-F-V-F"),
        (True, False, False, True, "Prestamo rechazado", "V-F-F-V"),
        (True, False, False, False, "Prestamo rechazado", "V-F-F-F"),
        (False, True, True, True, "Prestamo rechazado", "F-V-V-V"),
        (False, True, True, False, "Prestamo rechazado", "F-V-V-F"),
        (False, True, False, True, "Prestamo rechazado", "F-V-F-V"),
        (False, True, False, False, "Prestamo rechazado", "F-V-F-F"),
        (False, False, True, True, "Prestamo rechazado", "F-F-V-V"),
        (False, False, True, False, "Prestamo rechazado", "F-F-V-F"),
        (False, False, False, True, "Prestamo rechazado", "F-F-F-V"),
        (False, False, False, False, "Prestamo rechazado", "F-F-F-F"),
    ],
)
def test_combinacion_condiciones_puede_prestar(c1, c2, c3, c4, esperado, tabla):
    disponible = c1
    copias = 1 if c1 else 0
    sancionado = not c2
    estudiante = c3
    dias = 7 if c4 else 10

    usuario = Usuario(20, estudiante, sancionado, 0)
    libro = Libro("general", disponible, False, copias)

    assert puede_prestar(usuario, libro, dias) == esperado

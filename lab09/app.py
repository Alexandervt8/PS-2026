##################################################
# CONFIGURACIÓN
##################################################

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

##################################################
# DATOS EN MEMORIA
##################################################

reservas = [
    {
        "id": 1,
        "cliente": "Juan Velarde",
        "hotel": "Hotel Superior",
        "tipo_habitacion": "Suite",
        "fecha_ingreso": "2026-07-20",
        "fecha_salida": "2026-07-24",
        "numero_huespedes": 2,
        "estado": "Confirmada"
    },
    {
        "id": 2,
        "cliente": "Julia Torres",
        "hotel": "Hotel Cusco",
        "tipo_habitacion": "Doble",
        "fecha_ingreso": "2026-08-01",
        "fecha_salida": "2026-08-05",
        "numero_huespedes": 3,
        "estado": "Pendiente"
    },
    {
        "id": 3,
        "cliente": "Lucas Fernández",
        "hotel": "Hotel Lozano",
        "tipo_habitacion": "Simple",
        "fecha_ingreso": "2026-08-10",
        "fecha_salida": "2026-08-12",
        "numero_huespedes": 1,
        "estado": "Confirmada"
    }
]

##################################################
# FUNCIONES AUXILIARES
##################################################

# Se busca una reserva por su ID
def buscar_reserva(reserva_id):
    for reserva in reservas:
        if reserva["id"] == reserva_id:
            return reserva
    return None

# Se valida la información de la reserva
def validar_reserva(datos):
    campos_obligatorios = [
        "cliente",
        "hotel",
        "tipo_habitacion",
        "fecha_ingreso",
        "fecha_salida",
        "numero_huespedes",
        "estado"
    ]

    # Validación de campos obligatorios
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] in ("", None):
            return False, f"El campo '{campo}' es obligatorio."

    # Número de huéspedes
    if not isinstance(datos["numero_huespedes"], int):
        return False, "El número de huéspedes debe ser un número entero."

    # Validación del número de huéspedes
    if datos["numero_huespedes"] <= 0:
        return False, "El número de huéspedes debe ser mayor que cero."

    # Estados válidos
    estados_validos = [
        "Confirmada",
        "Pendiente",
        "Cancelada"
    ]

    # Validación del estado
    if datos["estado"] not in estados_validos:
        return False, (
            "Estado no válido. "
            "Debe ser Confirmada, Pendiente o Cancelada."
        )

    # Validación de fechas
    try:
        fecha_ingreso = datetime.strptime(
            datos["fecha_ingreso"],
            "%Y-%m-%d"
        )

        fecha_salida = datetime.strptime(
            datos["fecha_salida"],
            "%Y-%m-%d"
        )
    except ValueError:
        return False, (
            "Las fechas deben tener el formato YYYY-MM-DD."
        )

    # Validación de que la fecha de salida sea posterior a la fecha de ingreso
    if fecha_salida <= fecha_ingreso:
        return False, (
            "La fecha de salida debe ser posterior "
            "a la fecha de ingreso."
        )

    return True, None

##################################################
# ENDPOINTS DE LA API
##################################################

# Rutas de la API
@app.route("/reservas", methods=["GET"])
def obtener_reservas():
    return jsonify(reservas), 200

# Ruta para obtener una reserva específica por su ID
@app.route("/reservas/<int:reserva_id>", methods=["GET"])
def obtener_reserva(reserva_id):
    reserva = buscar_reserva(reserva_id)

    if reserva is None:
        return jsonify({
            "error": "Reserva no encontrada."
        }), 404

    return jsonify(reserva), 200

# Ruta para crear una nueva reserva
@app.route("/reservas", methods=["POST"])
def crear_reserva():

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "Debe enviar datos en formato JSON."
        }), 400

    valido, mensaje = validar_reserva(datos)

    if not valido:
        return jsonify({
            "error": mensaje
        }), 400

    if reservas:
        nuevo_id = max(reserva["id"] for reserva in reservas) + 1
    else:
        nuevo_id = 1

    nueva_reserva = {
        "id": nuevo_id,
        "cliente": datos["cliente"],
        "hotel": datos["hotel"],
        "tipo_habitacion": datos["tipo_habitacion"],
        "fecha_ingreso": datos["fecha_ingreso"],
        "fecha_salida": datos["fecha_salida"],
        "numero_huespedes": datos["numero_huespedes"],
        "estado": datos["estado"]
    }

    reservas.append(nueva_reserva)

    return jsonify({
        "mensaje": "Reserva creada correctamente.",
        "reserva": nueva_reserva
    }), 201

# Ruta para actualizar una reserva existente
@app.route("/reservas/<int:reserva_id>", methods=["PUT"])
def actualizar_reserva(reserva_id):

    reserva = buscar_reserva(reserva_id)

    if reserva is None:
        return jsonify({
            "error": "Reserva no encontrada."
        }), 404

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "Debe enviar datos en formato JSON."
        }), 400

    valido, mensaje = validar_reserva(datos)

    if not valido:
        return jsonify({
            "error": mensaje
        }), 400

    reserva["cliente"] = datos["cliente"]
    reserva["hotel"] = datos["hotel"]
    reserva["tipo_habitacion"] = datos["tipo_habitacion"]
    reserva["fecha_ingreso"] = datos["fecha_ingreso"]
    reserva["fecha_salida"] = datos["fecha_salida"]
    reserva["numero_huespedes"] = datos["numero_huespedes"]
    reserva["estado"] = datos["estado"]

    return jsonify({
        "mensaje": "Reserva actualizada correctamente.",
        "reserva": reserva
    }), 200

# Ruta para eliminar una reserva existente
@app.route("/reservas/<int:reserva_id>", methods=["DELETE"])
def eliminar_reserva(reserva_id):

    reserva = buscar_reserva(reserva_id)

    if reserva is None:
        return jsonify({
            "error": "Reserva no encontrada."
        }), 404

    reservas.remove(reserva)

    return jsonify({
        "mensaje": "Reserva eliminada correctamente."
    }), 200

##################################################
# EJECUCIÓN DE LA APLICACIÓN
##################################################

if __name__ == "__main__":
    app.run(debug=True)
# Laboratorio 09 - API REST para Gestión de Reservas de Hotel

## Descripción

Este proyecto implementa una API REST desarrollada con Flask para la gestión de reservas de hotel.
La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para reservas almacenadas temporalmente en memoria.

---

## Tecnologías utilizadas

- Python 3
- Flask
- Thunder Client / Postman para pruebas

---

## Instalación

1. Crear un entorno virtual:

```bash
python -m venv venv
```

2. Activar el entorno virtual.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar la aplicación con:

```bash
python app.py
```

La API estará disponible en:

```
http://127.0.0.1:5000
```

---

## Endpoints disponibles

| Método | Endpoint | Descripción |
|---------|----------|-------------|
| GET | /reservas | Obtener todas las reservas |
| GET | /reservas/{id} | Obtener una reserva por ID |
| POST | /reservas | Crear una reserva |
| PUT | /reservas/{id} | Actualizar una reserva |
| DELETE | /reservas/{id} | Eliminar una reserva |

---

## Validaciones implementadas

- Campos obligatorios.
- Número de huéspedes entero y mayor que cero.
- Estado válido (`Confirmada`, `Pendiente`, `Cancelada`).
- Fechas con formato `YYYY-MM-DD`.
- La fecha de salida debe ser posterior a la fecha de ingreso.

---

## Códigos HTTP utilizados

| Código | Significado |
|---------|-------------|
| 200 | Operación exitosa |
| 201 | Recurso creado correctamente |
| 400 | Error en los datos enviados |
| 404 | Recurso no encontrado |
| 415 | Tipo de contenido no soportado (gestionado por Flask) |
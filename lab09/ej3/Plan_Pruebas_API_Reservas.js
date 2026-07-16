/*
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
Este archivo implementa un plan de pruebas de rendimiento en k6 para evaluar
una API de gestión de reservas. Configura tres escenarios con diferentes
cantidades de usuarios virtuales y ejecuta operaciones CRUD mediante solicitudes
GET, POST, PUT y DELETE, verificando los códigos HTTP obtenidos.
===========================================================
*/

import http from 'k6/http';
import { check, sleep } from 'k6';

// Configuración de los escenarios de prueba
// Los escenarios son análogos a los del ejercicio 2 para una mejor comparativa de resultados en el informe
export const options = {
  scenarios: {
    // Escenario 1: 20 usuarios, 5 iteraciones, ramp-up 10s
    escenario_1: {
      executor: 'per-vu-iterations',
      vus: 20,
      iterations: 5,
      maxDuration: '30s',
      startTime: '0s',
      gracefulStop: '5s',
      tags: { escenario: 'Escenario 1' },
    },
    // Escenario 2: 50 usuarios, 10 iteraciones, ramp-up 20s
    escenario_2: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '20s', target: 50 },
        { duration: '5s', target: 50 },
        { duration: '5s', target: 0 },
      ],
      gracefulRampDown: '5s',
      startTime: '35s',
      tags: { escenario: 'Escenario 2' },
    },
    // Escenario 3: 100 usuarios, 15 iteraciones, ramp-up 30s
    escenario_3: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '30s', target: 100 },
        { duration: '10s', target: 100 },
        { duration: '10s', target: 0 },
      ],
      gracefulRampDown: '5s',
      startTime: '75s',
      tags: { escenario: 'Escenario 3' },
    },
  },
};

// Función para generar fechas aleatorias
function generarFechaAleatoria(mesInicio, mesFin) {
  const dia = String(Math.floor(Math.random() * 28) + 1).padStart(2, '0');
  const mes = String(Math.floor(Math.random() * (mesFin - mesInicio + 1)) + mesInicio).padStart(2, '0');
  return `2026-${mes}-${dia}`;
}

// Función para crear una reserva de prueba
function crearReservaPrueba() {
  const clientes = ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Sánchez', 
                    'Laura Torres', 'Miguel Rodríguez', 'Sofía Fernández', 'David Gómez', 'Elena Ruiz'];
  const hoteles = ['Hotel Superior', 'Hotel Cusco', 'Hotel Lozano', 'Hotel Plaza', 'Hotel Royal',
                   'Hotel Imperial', 'Hotel Dorado', 'Hotel Pacifico', 'Hotel Central', 'Hotel Victoria'];
  const habitaciones = ['Simple', 'Doble', 'Suite', 'Familiar', 'Premium'];
  const estados = ['Confirmada', 'Pendiente', 'Cancelada'];
  
  const fechaIngreso = generarFechaAleatoria(7, 8);
  const fechaSalida = generarFechaAleatoria(8, 9);
  
  return {
    cliente: clientes[Math.floor(Math.random() * clientes.length)],
    hotel: hoteles[Math.floor(Math.random() * hoteles.length)],
    tipo_habitacion: habitaciones[Math.floor(Math.random() * habitaciones.length)],
    fecha_ingreso: fechaIngreso,
    fecha_salida: fechaSalida,
    numero_huespedes: Math.floor(Math.random() * 4) + 1,
    estado: estados[Math.floor(Math.random() * estados.length)],
  };
}

// Función principal de la prueba - Ejecuta un ciclo CRUD completo
export default function () {
  const baseUrl = 'http://127.0.0.1:5000';
  
  // 1. GET /reservas - Obtener todas las reservas
  let response = http.get(`${baseUrl}/reservas`);
  check(response, {
    'GET /reservas - status 200': (r) => r.status === 200,
  });
  sleep(0.1);

  // 2. POST /reservas - Crear una nueva reserva
  const nuevaReserva = crearReservaPrueba();
  response = http.post(`${baseUrl}/reservas`, JSON.stringify(nuevaReserva), {
    headers: { 'Content-Type': 'application/json' },
  });
  
  let reservaId = null;
  check(response, {
    'POST /reservas - status 201': (r) => r.status === 201,
  });
  
  // Extraer el ID de la reserva creada
  if (response.status === 201) {
    try {
      const body = JSON.parse(response.body);
      if (body.reserva && body.reserva.id) {
        reservaId = body.reserva.id;
      }
    } catch (e) {
      console.error('Error al parsear respuesta POST');
    }
  }
  sleep(0.1);

  // 3. GET /reservas/{id} - Obtener la reserva creada
  if (reservaId) {
    response = http.get(`${baseUrl}/reservas/${reservaId}`);
    check(response, {
      'GET /reservas/{id} - status 200': (r) => r.status === 200,
    });
    sleep(0.1);

    // 4. PUT /reservas/{id} - Actualizar la reserva
    const reservaActualizada = {
      cliente: 'Cliente Actualizado',
      hotel: 'Hotel Actualizado',
      tipo_habitacion: 'Suite',
      fecha_ingreso: '2026-08-15',
      fecha_salida: '2026-08-20',
      numero_huespedes: 3,
      estado: 'Confirmada',
    };
    response = http.put(`${baseUrl}/reservas/${reservaId}`, JSON.stringify(reservaActualizada), {
      headers: { 'Content-Type': 'application/json' },
    });
    check(response, {
      'PUT /reservas/{id} - status 200': (r) => r.status === 200,
    });
    sleep(0.1);

    // 5. DELETE /reservas/{id} - Eliminar la reserva
    response = http.del(`${baseUrl}/reservas/${reservaId}`);
    check(response, {
      'DELETE /reservas/{id} - status 200': (r) => r.status === 200,
    });
    sleep(0.1);
  } else {
    // Si no se pudo crear, intentamos con una reserva existente
    response = http.get(`${baseUrl}/reservas`);
    try {
      const reservas = JSON.parse(response.body);
      if (reservas.length > 0) {
        const idExistente = reservas[0].id;
        
        // GET de reserva existente
        response = http.get(`${baseUrl}/reservas/${idExistente}`);
        check(response, {
          'GET /reservas/{id} (existente) - status 200': (r) => r.status === 200,
        });
        sleep(0.1);
        
        // PUT de reserva existente
        const reservaActualizada = {
          cliente: 'Cliente Modificado',
          hotel: 'Hotel Modificado',
          tipo_habitacion: 'Doble',
          fecha_ingreso: '2026-08-10',
          fecha_salida: '2026-08-15',
          numero_huespedes: 2,
          estado: 'Pendiente',
        };
        response = http.put(`${baseUrl}/reservas/${idExistente}`, JSON.stringify(reservaActualizada), {
          headers: { 'Content-Type': 'application/json' },
        });
        check(response, {
          'PUT /reservas/{id} (existente) - status 200': (r) => r.status === 200,
        });
        sleep(0.1);
      }
    } catch (e) {
      console.error('Error al obtener reservas existentes');
    }
  }
  
  // Pequeña pausa entre iteraciones
  sleep(0.2);
}

// Función para resumen personalizado al finalizar
export function handleSummary(data) {
  const totalRequests = data.metrics.http_reqs.values.count;
  const avgDuration = data.metrics.http_req_duration.values.avg;
  const maxDuration = data.metrics.http_req_duration.values.max;
  const minDuration = data.metrics.http_req_duration.values.min;
  const throughput = data.metrics.http_reqs.values.rate;
  const errorRate = data.metrics.http_req_failed.values.rate * 100;
  // const stdDev = data.metrics.http_req_duration.values.p('stddev');
  
  return {
    'stdout': `
╔═══════════════════════════════════════════════════════════════╗
║                  RESULTADOS DE PRUEBAS K6                    ║
╠═══════════════════════════════════════════════════════════════╣
║ Total solicitudes:       ${String(totalRequests).padEnd(10)}                           ║
║ Tiempo promedio:         ${String(avgDuration.toFixed(2)).padEnd(10)} ms                           ║
║ Tiempo mínimo:           ${String(minDuration.toFixed(2)).padEnd(10)} ms                           ║
║ Tiempo máximo:           ${String(maxDuration.toFixed(2)).padEnd(10)} ms                           ║
║ Throughput:              ${String(throughput.toFixed(2)).padEnd(10)} req/s                         ║
║ Tasa de error:           ${String(errorRate.toFixed(2)).padEnd(10)} %                             ║
╚═══════════════════════════════════════════════════════════════╝
`,
    'resultados-k6.json': JSON.stringify({
      timestamp: new Date().toISOString(),
      total_requests: totalRequests,
      avg_response_time_ms: avgDuration,
      min_response_time_ms: minDuration,
      max_response_time_ms: maxDuration,
      throughput_req_s: throughput,
      error_rate_percent: errorRate,
      // std_dev_ms: stdDev,
    }, null, 2),
  };
}
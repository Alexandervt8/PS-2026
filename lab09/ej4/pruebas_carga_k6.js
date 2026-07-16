import http from 'k6/http';
import { check, sleep } from 'k6';
import exec from 'k6/execution';

const escenario = __ENV.ESCENARIO || '1';
const configuraciones = {
  '1': { vus: 20, iteraciones: 5, rampUpSegundos: 10 },
  '2': { vus: 50, iteraciones: 10, rampUpSegundos: 20 },
  '3': { vus: 100, iteraciones: 15, rampUpSegundos: 30 },
};

const config = configuraciones[escenario];
if (!config) {
  throw new Error('ESCENARIO debe ser 1, 2 o 3');
}

export const options = {
  scenarios: {
    carga_api_reservas: {
      executor: 'per-vu-iterations',
      vus: config.vus,
      iterations: config.iteraciones,
      maxDuration: '2m',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost:5000';
let inicioEscalonado = false;

export default function () {
  if (!inicioEscalonado) {
    const posicion = exec.vu.idInTest - 1;
    const divisor = Math.max(config.vus - 1, 1);
    sleep((posicion * config.rampUpSegundos) / divisor);
    inicioEscalonado = true;
  }

  const respuesta = http.get(`${BASE_URL}/reservas`, {
    tags: { endpoint: 'GET /reservas', escenario },
  });

  check(respuesta, {
    'estado HTTP 200': (r) => r.status === 200,
    'respuesta en formato JSON': (r) =>
      (r.headers['Content-Type'] || '').includes('application/json'),
  });
}

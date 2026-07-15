const request = require('supertest');
const app = require('./app');

describe('Laboratorio 08 - Integracion API Biblioteca Musical', () => {
  beforeEach(async () => {
    await request(app).post('/api/testing/reset');
  });

  test('Flujo de persistencia cruzada: POST /api/canciones y GET /api/canciones/:id', async () => {
    const cancionBase = {
      titulo: 'Luz de medianoche',
      artista: 'Aurora Andina',
      album: 'Rutas Sonoras',
      genero: 'Indie Rock',
      duracionSegundos: 245,
      reproducciones: 12,
      calificacion: 4.8,
      favorita: true,
    };

    const respuestaPost = await request(app)
      .post('/api/canciones')
      .send(cancionBase)
      .expect(201);

    expect(respuestaPost.body).toHaveProperty('id');
    expect(respuestaPost.body.titulo).toBe(cancionBase.titulo);
    expect(respuestaPost.body.reproducciones).toBe(12);

    const idGenerado = respuestaPost.body.id;

    const respuestaGet = await request(app)
      .get(`/api/canciones/${idGenerado}`)
      .expect(200);

    expect(respuestaGet.body.id).toBe(idGenerado);
    expect(respuestaGet.body.artista).toBe('Aurora Andina');
    expect(respuestaGet.body.album).toBe('Rutas Sonoras');
    expect(respuestaGet.body.genero).toBe('Indie Rock');
  });

  test('Simulacion de modificacion de estado: actualizar reproducciones y confirmar con GET', async () => {
    const respuestaPost = await request(app)
      .post('/api/canciones')
      .send({
        titulo: 'Acero y compas',
        artista: 'Taller Sonoro',
        album: 'Metal Urbano',
        genero: 'Fusion',
        duracionSegundos: 198,
        reproducciones: 5,
        calificacion: 4.2,
      })
      .expect(201);

    const id = respuestaPost.body.id;

    const respuestaPatch = await request(app)
      .patch(`/api/canciones/${id}/reproducir`)
      .send({ incremento: 7 })
      .expect(200);

    expect(respuestaPatch.body.mensaje).toBe('Reproducciones actualizadas');
    expect(respuestaPatch.body.cancion.reproducciones).toBe(12);

    const respuestaGet = await request(app)
      .get(`/api/canciones/${id}`)
      .expect(200);

    expect(respuestaGet.body.reproducciones).toBe(12);
  });

  test('Edge case 1: rechaza campo numerico enviado como texto con HTTP 400', async () => {
    const respuesta = await request(app)
      .post('/api/canciones')
      .send({
        titulo: 'Cancion invalida',
        artista: 'QA Band',
        album: 'Errores comunes',
        genero: 'Rock',
        duracionSegundos: 'tres minutos',
        reproducciones: 0,
      })
      .expect(400);

    expect(respuesta.body.error).toBe('Solicitud invalida');
    expect(respuesta.body.detalles).toContain('El campo duracionSegundos debe ser numerico y mayor que 0.');
  });

  test('Edge case 2: rechaza campos obligatorios vacios con HTTP 400', async () => {
    const respuesta = await request(app)
      .post('/api/canciones')
      .send({
        titulo: '',
        artista: '',
        album: 'Sin datos',
        genero: 'Pop',
        duracionSegundos: 210,
        reproducciones: 1,
      })
      .expect(400);

    expect(respuesta.body.error).toBe('Solicitud invalida');
    expect(respuesta.body.detalles).toContain('El campo titulo es obligatorio y debe ser texto.');
    expect(respuesta.body.detalles).toContain('El campo artista es obligatorio y debe ser texto.');
  });

  test('Edge case 3: rechaza incremento invalido al modificar reproducciones', async () => {
    const creada = await request(app)
      .post('/api/canciones')
      .send({
        titulo: 'Prueba de incremento',
        artista: 'QA Band',
        album: 'Testing Sessions',
        genero: 'Electronica',
        duracionSegundos: 180,
        reproducciones: 3,
      })
      .expect(201);

    const respuesta = await request(app)
      .patch(`/api/canciones/${creada.body.id}/reproducir`)
      .send({ incremento: -2 })
      .expect(400);

    expect(respuesta.body.error).toBe('El campo incremento debe ser un entero positivo.');
  });
});

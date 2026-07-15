const express = require('express');

const app = express();
app.use(express.json());

let canciones = [];
let siguienteId = 1;

function esTextoValido(valor) {
  return typeof valor === 'string' && valor.trim().length > 0;
}

function esNumeroPositivo(valor) {
  return typeof valor === 'number' && Number.isFinite(valor) && valor > 0;
}

function esEnteroNoNegativo(valor) {
  return Number.isInteger(valor) && valor >= 0;
}

function validarCancion(body) {
  const errores = [];
  if (!esTextoValido(body.titulo)) errores.push('El campo titulo es obligatorio y debe ser texto.');
  if (!esTextoValido(body.artista)) errores.push('El campo artista es obligatorio y debe ser texto.');
  if (!esTextoValido(body.album)) errores.push('El campo album es obligatorio y debe ser texto.');
  if (!esTextoValido(body.genero)) errores.push('El campo genero es obligatorio y debe ser texto.');
  if (!esNumeroPositivo(body.duracionSegundos)) errores.push('El campo duracionSegundos debe ser numerico y mayor que 0.');
  if (!esEnteroNoNegativo(body.reproducciones)) errores.push('El campo reproducciones debe ser entero y no negativo.');
  if (body.calificacion !== undefined && (typeof body.calificacion !== 'number' || body.calificacion < 0 || body.calificacion > 5)) {
    errores.push('El campo calificacion debe ser un numero entre 0 y 5.');
  }
  return errores;
}

function buscarCancion(id) {
  return canciones.find((cancion) => cancion.id === Number(id));
}

app.get('/api/estado', (req, res) => {
  res.status(200).json({ servicio: 'Biblioteca musical', totalCanciones: canciones.length });
});

app.post('/api/canciones', (req, res) => {
  const errores = validarCancion(req.body);
  if (errores.length > 0) {
    return res.status(400).json({ error: 'Solicitud invalida', detalles: errores });
  }

  const nuevaCancion = {
    id: siguienteId++,
    titulo: req.body.titulo.trim(),
    artista: req.body.artista.trim(),
    album: req.body.album.trim(),
    genero: req.body.genero.trim(),
    duracionSegundos: req.body.duracionSegundos,
    reproducciones: req.body.reproducciones,
    calificacion: req.body.calificacion ?? 0,
    favorita: Boolean(req.body.favorita),
    creadaEn: new Date().toISOString(),
  };

  canciones.push(nuevaCancion);
  res.status(201).json(nuevaCancion);
});

app.get('/api/canciones', (req, res) => {
  res.status(200).json({ total: canciones.length, items: canciones });
});

app.get('/api/canciones/:id', (req, res) => {
  const cancion = buscarCancion(req.params.id);
  if (!cancion) {
    return res.status(404).json({ error: 'Cancion no encontrada' });
  }
  res.status(200).json(cancion);
});

app.patch('/api/canciones/:id/reproducir', (req, res) => {
  const cancion = buscarCancion(req.params.id);
  if (!cancion) {
    return res.status(404).json({ error: 'Cancion no encontrada' });
  }

  const incremento = req.body.incremento ?? 1;
  if (!Number.isInteger(incremento) || incremento <= 0) {
    return res.status(400).json({ error: 'El campo incremento debe ser un entero positivo.' });
  }

  cancion.reproducciones += incremento;
  res.status(200).json({ mensaje: 'Reproducciones actualizadas', cancion });
});

app.put('/api/canciones/:id', (req, res) => {
  const cancion = buscarCancion(req.params.id);
  if (!cancion) {
    return res.status(404).json({ error: 'Cancion no encontrada' });
  }

  const datosActualizados = { ...cancion, ...req.body };
  const errores = validarCancion(datosActualizados);
  if (errores.length > 0) {
    return res.status(400).json({ error: 'Solicitud invalida', detalles: errores });
  }

  Object.assign(cancion, {
    titulo: datosActualizados.titulo.trim(),
    artista: datosActualizados.artista.trim(),
    album: datosActualizados.album.trim(),
    genero: datosActualizados.genero.trim(),
    duracionSegundos: datosActualizados.duracionSegundos,
    reproducciones: datosActualizados.reproducciones,
    calificacion: datosActualizados.calificacion,
    favorita: Boolean(datosActualizados.favorita),
  });

  res.status(200).json(cancion);
});

app.delete('/api/canciones/:id', (req, res) => {
  const posicion = canciones.findIndex((cancion) => cancion.id === Number(req.params.id));
  if (posicion === -1) {
    return res.status(404).json({ error: 'Cancion no encontrada' });
  }

  const eliminada = canciones.splice(posicion, 1)[0];
  res.status(200).json({ mensaje: 'Cancion eliminada', cancion: eliminada });
});

app.post('/api/testing/reset', (req, res) => {
  canciones = [];
  siguienteId = 1;
  res.status(200).json({ mensaje: 'Persistencia reiniciada' });
});

if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => console.log(`API Biblioteca Musical activa en puerto ${PORT}`));
}

module.exports = app;

<template>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
        <td>{{calificacion.id_estudiante.rut + "-" + calificacion.id_estudiante.dig_verificador}}</td>
        <td>{{calificacion.id_evaluacion.id_coordinacion.id_asignatura.nombre}}</td>
        <td>{{calificacion.id_evaluacion.nombre}}</td>
        <td>{{calificacion.nota}}</td>
        <td>{{calificacion.fecha_entrega}}</td>

        <div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Nueva Nota" aria-label="Nueva Nota" aria-describedby="button-addon2">
  <input type="text" class="form-control" placeholder="ObsOpcional" aria-label="ObsOpcional" aria-describedby="button-addon2">
  <button class="btn btn-outline-secondary" type="button" id="button-addon2">Calificar</button>
</div>
</template>

<script>
export default {
    props:{ 
        calificacion: Array,
    },
}
</script>
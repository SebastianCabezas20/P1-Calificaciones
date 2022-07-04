<template>
  <td>{{ asignatura.id_coordinacion.id_asignatura.codigo }}</td>
  <td>{{ asignatura.id_coordinacion.id_asignatura.nombre }}</td>
  <td>{{ asignatura.id_coordinacion.bloques_horario }}</td>
  <td>{{ asignatura.id_coordinacion.id_asignatura.componente }}</td>
  <td>{{ asignatura.id_coordinacion.id_asignatura.nivel }}</td>

  <td><button type="button" class="btn btn-light">Más Información</button></td>
</template>

<script>
export default {
  props: {
    asignatura: Array,
  },
};
</script>

<template>
  <td>
    <input
      class="form-check-input"
      type="checkbox"
      value=""
      id="defaultCheck1"
    />
  </td>
  <td>{{ calificacionEstudiante.id_estudiante.id_usuario.first_name }} {{ calificacionEstudiante.id_estudiante.id_usuario.last_name }} </td>
  <td>{{ calificacionEstudiante.id_estudiante.rut }}-{{ calificacionEstudiante.id_estudiante.dig_verificador }}</td>
  <td>{{ calificacionEstudiante.nota }}</td>

  <td>
    <input class="form-control" type="text" placeholder="Calificación" />
  </td>
</template>

<script>
export default {
  props: {
    calificacionEstudiante: Array,
  },
};
</script>

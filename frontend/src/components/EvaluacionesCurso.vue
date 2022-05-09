<template>
  <td>{{ evaluacionCurso.nombre }}</td>
  <td>{{ evaluacionCurso.id_tipoEvaluacion.nombre }}</td>
  <td>{{ evaluacionCurso.fechaEvActual }}</td>
  <td>{{ evaluacionCurso.estado }}</td>
  <td>{{ evaluacionCurso.ponderacion }}</td>
  <td>
      <div class="text-center">
        <i class="fa-solid fa-pencil"></i>
      </div>
  </td>
  <td>
      <div class="text-center">
        <span class="fa-solid fa-trash-can"></span>
      </div>
  </td>
</template>

<script>
export default {
  props: {
    evaluacionCurso: Array,
  },
};
</script>

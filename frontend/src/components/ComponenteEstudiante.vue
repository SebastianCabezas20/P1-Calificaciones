<template>
  <div class="titleSectionV2">
    <h3 class="textTitleV2">Estudiante - {{ componente }}</h3>
  </div>

  <!-- Evaluaciones calificadas. -->
  <div class="titleSectionV2">
    <h3 class="textSubTitleV2">Evaluaciones calificadas</h3>
  </div>

  <table class="tableV2">
    <thead>
      <tr>
        <th>Evaluación</th>
        <th>Calificación</th>
        <th>Pondera</th>
        <th>Fecha de realización</th>
        <th>Fecha de calificación</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="calificacion in calificaciones" :key="calificacion.id">
        <td>{{ calificacion.id_evaluacion.nombre }}</td>
        <td>{{ calificacion.nota }}</td>
        <td>{{ calificacion.id_evaluacion.ponderacion * 100 }}%</td>
        <td>{{ calificacion.id_evaluacion.fechaEvActual }}</td>
        <td>{{ calificacion.fecha_entrega }}</td>
      </tr>
    </tbody>
  </table>

  <!-- Evaluaciones pendientes. -->
  <div class="titleSectionV2">
    <h3 class="textSubTitleV2">Evaluaciones pendientes</h3>
  </div>

  <table class="tableV2">
    <thead>
      <tr>
        <th>Evaluación</th>
        <th>Pondera</th>
        <th>Fecha de evaluación</th>
        <th>Fecha limite de entrega de notas</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="evaluacion in evaluaciones" :key="evaluacion.id">
        <td>{{ evaluacion.nombre }}</td>
        <td>{{ evaluacion.ponderacion * 100 }}%</td>
        <td>{{ evaluacion.fechaEvActual }}</td>
        <td>{{ evaluacion.fechaEntrega }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    componente: String,
    evaluaciones: Array,
    calificaciones: Array,
  },
};
</script>

<style></style>

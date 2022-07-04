<template>
  <table class="tableDashboard">
    <thead>
      <tr>
        <th style="width: 40%">Asignatura</th>
        <th>Evaluación</th>
        <th>Fecha de recepción</th>
        <th>Calificación</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(calificacion, index) in calificaciones.slice(0, 3)"
        :key="index"
        @click="ingresarCurso(index)"
      >
        <td>{{ calificacion.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
        <td>{{ calificacion.id_evaluacion.nombre }}</td>
        <td>{{ calificacion.fecha_entrega }}</td>
        <td>{{ calificacion.nota }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  props: {
    calificaciones: Array,
  },
  emits: ["EventIngresarCurso"],
  methods: {
    ingresarCurso(index) {
        this.$emit("EventIngresarCurso", index);
    },
  },
};
</script>

<style></style>
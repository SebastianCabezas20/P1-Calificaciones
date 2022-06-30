<template>
  <table class="tableDashboard">
    <thead>
      <tr>
        <th style="width: 10%">Código</th>
        <th style="width: 40%">Asignatura</th>
        <th>Evaluación</th>
        <th>Fecha límite para entrega de notas</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(evaluacion, index) in evaluaciones.slice(0, 3)"
        :key="index"
        @click="ingresarEvaluacion(index)"
      >
        <td>
          {{ evaluacion.id_coordinacion.id_asignatura.codigo }}-{{
            evaluacion.id_coordinacion.coordinacion
          }}-{{ evaluacion.id_coordinacion.seccion }}
        </td>
        <td>{{ evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
        <td>{{ evaluacion.nombre }}</td>
        <td>{{ evaluacion.fechaEntrega }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  props: {
    evaluaciones: Array,
  },
  emits: ["EventIngresarEvaluacion"],
  methods: {
    ingresarEvaluacion(index) {
        this.$emit("EventIngresarEvaluacion", index);
    },
  },
};
</script>

<style></style>

<template>
  <table class="tableDashboard">
    <thead>
      <tr>
        <th>Curso</th>
        <th>Evaluación</th>
        <th style="width: 25%">Fecha de respuesta</th>
        <th style="width: 15%">Estado</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="solicitud in solicitudes.slice(0, 3)"
        :key="index"
      >
        <td>
          {{ solicitud.id_evaluacion.id_coordinacion.id_asignatura.nombre }}
        </td>
        <td>{{ solicitud.id_evaluacion.nombre }}</td>
        <td>{{ solicitud.fecha_respuesta }}</td>
        <td v-if="solicitud.estado === 'A'">Aprobada</td>
        <td v-else>Rechazada</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  props: {
    solicitudes: Array,
  },
};
</script>

<style></style>
<template>
  <td>{{ solicitud.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
  <td>{{ solicitud.id_evaluacion.nombre }}</td>
  <td v-if="solicitud.estado == 'P'">Pendiente</td>
  <td v-else-if="solicitud.estado == 'A'">Aceptada</td>
  <td v-else>Rechazada</td>
  <td>{{ solicitud.motivo }}</td>
  <td>{{ solicitud.respuesta }}</td>
</template>

<script>
export default {
  props: {
    solicitud: Object,
  },
};
</script>

<style></style>

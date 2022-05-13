<template>
  <td class="solic">{{ solicitud.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
  <td class="solic">{{ solicitud.id_evaluacion.nombre }}</td>
  <td class="solic" v-if="solicitud.estado == 'P'">Pendiente</td>
  <td class="solic" v-else-if="solicitud.estado == 'A'">Aceptada</td>
  <td class="solic" v-else>Rechazada</td>
  <td class="solic">{{ solicitud.motivo }}</td>
  <td class="solic">{{ solicitud.respuesta }}</td>
</template>

<script>
export default {
  props: {
    solicitud: Object,
  },
};
</script>

<style>
    .solic {
        text-align: center;
    }
</style>

<template>
  <td>{{ solicitud.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
  <td>{{ solicitud.id_evaluacion.nombre }}</td>
  <td v-if="solicitud.estado == 'P'">Pendiente</td>
  <td v-else-if="solicitud.estado == 'A'">Aceptada</td>
  <td v-else-if="solicitud.estado == 'E'">En revisión</td>
  <td v-else>Rechazada</td>
  <td>{{ solicitud.motivo }}</td>
  <td>{{ solicitud.respuesta }}</td>
  <td @click="mostrarSeguimiento(solicitud)">
    <span 
      class="fa-solid fa-info botonTabla" 
      title="Estado de mi solicitud de revisión">
    </span>
  </td>
  <td>
    <button
      class="fa-solid fa-plus botonTabla"
      title="Modificar el motivo de mi solicitud"
      :disabled="solicitud.estado !== 'P'"
      @click="modificarMotivo(solicitud)"
    ></button>
  </td>
</template>

<script>
export default {
  props: {
    solicitud: Object,
  },
  emits: ['EventModificarSolicitud', 'EventMostrarSeguimiento'],
  data() {
    return {
      showTrack: false,
    };
  },
  methods: {
    modificarMotivo(solicitud){
      this.$emit('EventModificarSolicitud', solicitud);
    },
    mostrarSeguimiento(solicitud) {
      this.$emit('EventMostrarSeguimiento', solicitud);
    }
  },
};
</script>

<style></style>
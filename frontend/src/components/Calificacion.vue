<template>
  <td>{{ calificacion.id_evaluacion.nombre }}</td>
  <td>{{ calificacion.id_observacion }}</td>
  <td>{{ calificacion.nota }}</td>
  <td>{{ calificacion.id_evaluacion.ponderacion }}</td>
  <td>{{ calificacion.fecha_entrega }}</td>

  <td>
    <button
      type="button"
      class="btn btn-light"
      @click.prevent="eventoClick(calificacion.id)"
    >
      Apelar Calificación
    </button>
  </td>
</template>

<script>
export default {
  props: {
    calificacion: Object,
  },
  emits: ["EventBoton"],
  methods: {
    eventoClick(id) {
      this.$emit("EventBoton", id);
    },
  },
};
</script>

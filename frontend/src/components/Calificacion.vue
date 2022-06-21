<template>
  <td>{{ calificacion.id_evaluacion.nombre }}</td>
  <td>{{ calificacion.nota }}</td>
  <td>{{ calificacion.id_evaluacion.ponderacion * 100}}%</td>
  <td>{{ calificacion.id_evaluacion.fechaEvActual }}</td>
  <td>{{ calificacion.fecha_entrega }}</td>

  <td>
    <button
      type="button"
      class="botonTabla"
      @click.prevent="informacionCalificacion(calificacion)"
    >
      Más información
    </button>
  </td>

  <td>
    <button
      type="button"
      class="botonTabla"
      @click.prevent="eventoClick(calificacion.id)"
      :disabled="!existeSolicitud(calificacion.id)"
    >
      Apelar
    </button>
  </td>
</template>

<script>
export default {
  props: {
    calificacion: Object,
    CalificacionSolicitudes: Array,
  },
  emits: ["EventBoton", "EventMostrarInformacion"],
  methods: {
    eventoClick(id) {
      this.$emit("EventBoton", id);
    },

    informacionCalificacion(calificacion){
      this.$emit("EventMostrarInformacion", calificacion);
    },

    existeSolicitud(id) {
      if (this.CalificacionSolicitudes.includes(id)) {
        return false;
      } else {
        return true;
      }
    },
  },
};
</script>

<style>
/* No se agregan al main.css, dado que se espera eliminar estos botones en
  el Sprint 3. */
.botonObservacion {
  background: #004883;
  margin: 0px 5px;
  border-radius: 100px;
  box-shadow: #004883 0 10px 20px -10px;
  box-sizing: border-box;
  color: #ffffff;
  font-size: 14px;
  font-weight: 700;
  line-height: 24px;
  outline: 0 solid transparent;
  padding: 8px 18px;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
  width: 120px;
  word-break: break-word;
  border: 0;
}

.botonObservacion:hover {
  transform: scale(1.05);
}
:root {
  --popper-theme-background-color: #333333;
  --popper-theme-background-color-hover: #333333;
  --popper-theme-text-color: #ffffff;
  --popper-theme-border-width: 0px;
  --popper-theme-border-style: solid;
  --popper-theme-border-radius: 6px;
  --popper-theme-padding: 32px;
  --popper-theme-box-shadow: 0 6px 30px -6px rgba(0, 0, 0, 0.25);
}
</style>

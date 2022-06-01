<template>
  
  <td>{{ calificacion.id_evaluacion.nombre }}</td>
  <td>
    <Popper :content="calificacion.obs_privada">
    <button class="btn btn-primary" style="margin-right:20px"> Observación Privada</button>
    </Popper>
    <Popper :content="calificacion.id_evaluacion.obs_general">
    <button class="btn btn-primary"> Observación General</button>
    </Popper>
  </td>
  <td>{{ calificacion.nota }}</td>
  <td>{{ calificacion.id_evaluacion.ponderacion }}</td>
  <td>{{ calificacion.fecha_entrega }}</td>

  <td>
    <button
      type="button"
      class="btn btn-light"
      @click.prevent="eventoClick(calificacion.id)"
      v-show="existeSolicitud(calificacion.id)"
    >
      Apelar Calificación
    </button>
  </td>
</template>


<script>
  import Popper from "vue3-popper";
export default {  
  props:{
    calificacion: Object,
    CalificacionSolicitudes: Array,
  },
  emits: ["EventBoton"],
  methods: {
    eventoClick(id) {
      this.$emit("EventBoton", id);
    },
    existeSolicitud(id){

      if(this.CalificacionSolicitudes.includes(id)){
        return false
      }
      else{
        return true
      }
    }
    
  },
};
</script>

<style>
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
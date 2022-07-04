<template>
  <td>{{ calificacion.id_evaluacion.nombre }}</td>
  <td>{{ calificacion.nota }}</td>
  <td>{{ parseFloat(calificacion.id_evaluacion.ponderacion * 100).toFixed(1) }}%</td>
  <td>{{ calificacion.id_evaluacion.fechaEvActual }}</td>
  <td>{{ calificacion.fecha_entrega }}</td>
  <td>{{ calcularPromedio(this.allCalificaciones, calificacion.id_evaluacion.nombre) }}</td>
  <td>{{ obtenerMaxNota(this.allCalificaciones, calificacion.id_evaluacion.nombre) }}</td>
  <td>{{ obtenerMinNota(this.allCalificaciones, calificacion.id_evaluacion.nombre) }}</td>

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
    <!-- Caso 1: El estudiante ya realizo la apelación de esa calificación,
    o bien, pasaron los 5 días disponibles para solicitar la apelación. -->
    <button
      type="button"
      class="botonTabla"
      @click.prevent="eventoClick(calificacion.id)"
      v-if="existeSolicitud(calificacion.id) || !apelacionValida(calificacion)"
      disabled
    >
      Apelar
    </button>

    <!-- Caso 2: El estudiante aún está a tiempo de apelar. -->
    <button
      type="button"
      class="botonTabla"
      @click.prevent="eventoClick(calificacion.id)"
      v-else
    >
      Apelar
    </button>
  </td>

  <!-- Marca que indica los días faltantes para solicitar la apelación. 
  Y en otros casos indica un ticket si el estudiante realizó la apelación,
  y una cruz en el caso de que hayan pasado los 5 días. -->
  <td>
    <!-- Ticket: Estudiante realizó la apelación. -->
    <span 
      class="fa-solid fa-check"
      v-if="existeSolicitud(calificacion.id)"
      title="Usted ya realizó una solicitud de revisión."
    >
    </span>
    <!-- Cruz: Estudiante está fuera del plazo (Mayor a 5 días). -->
    <span 
      class="fa-solid fa-x"
      v-else-if="!apelacionValida(calificacion)"
      title="El periodo de apelación (5 días posterior a fecha de entrega de notas) ha concluido."
    > 
    </span>
    <span
      v-else
      title="Días restantes para enviar una solicitud de revisión."
    >
    {{apelacionValida(calificacion)}}
    </span>
  </td>
</template>

<script>
import moment from 'moment';

export default {
  props: {
    calificacion: Object,
    CalificacionSolicitudes: Array,
    allCalificaciones: Array,
  },
  emits: ["EventBoton", "EventMostrarInformacion"],
  methods: {
    eventoClick(id) {
      this.$emit("EventBoton", id);
    },

    informacionCalificacion(calificacion){
      this.$emit("EventMostrarInformacion", calificacion);
    },

    /* Se comprueba si el estudiante ya realizo una apelación a una nota. */
    existeSolicitud(id) {
      if (this.CalificacionSolicitudes.includes(id)) {
        return true;
      } 
      return false;
    },

    apelacionValida(calificacion){
      let fechaEntrega = moment(calificacion.fecha_entrega);
      let fechaActual = moment().startOf('day');
      let diferenciaDias = moment.duration(fechaActual.diff(fechaEntrega)).asDays();
      
      // Caso 1: El estudiante se encuentra fuera de la fecha de apelación.
      if(diferenciaDias > 5) {
        return false;
      }
      /*  Caso 2: El estudiante puede enviar la apelación y se indican los días
      faltantes */
      return 5 - diferenciaDias;
    },

    //Función que calcula el promedio de una evaluación que ya fue evaluada.
    calcularPromedio(calificaciones, nombreEvaluacion) {
      var acum = 0;
      var cantNotas = 0;
      for(var i = 0; i < calificaciones.length; i++) {
        //Acá se verifica que la evaluación ya fue evaluada y coincide con la que se está escribiendo en la tabla.
        if(calificaciones[i].id_evaluacion.nombre == nombreEvaluacion && calificaciones[i].id_evaluacion.estado == "E") {
          acum = acum + parseInt(calificaciones[i].nota);
          cantNotas++;
        }
      }
      if(acum != 0) {
        const promedio = acum/cantNotas;
        const promedioDecimal = promedio.toFixed(1);
        return promedioDecimal
      }
      else{
        return "P"
      }
    },

    obtenerMaxNota(calificaciones, nombreEvaluacion) {
      var acum = 0;
      for(var i = 0; i < calificaciones.length; i++) {
        //Acá se verifica que la evaluación ya fue evaluada y coincide con la que se está escribiendo en la tabla.
        if(calificaciones[i].id_evaluacion.nombre == nombreEvaluacion && calificaciones[i].id_evaluacion.estado == "E") {
          if(parseInt(calificaciones[i].nota) > acum) {
            acum = parseInt(calificaciones[i].nota);
          }
        }
      }
      return acum.toFixed(1)
    },

    obtenerMinNota(calificaciones, nombreEvaluacion) {
      var acum = 7;
      for(var i = 0; i < calificaciones.length; i++) {
        //Acá se verifica que la evaluación ya fue evaluada y coincide con la que se está escribiendo en la tabla.
        if(calificaciones[i].id_evaluacion.nombre == nombreEvaluacion && calificaciones[i].id_evaluacion.estado == "E") {
          if(parseInt(calificaciones[i].nota) < acum) {
            acum = parseInt(calificaciones[i].nota);
          }
        }
      }
      return acum.toFixed(1)
    }
  },
};
</script>

<style> </style>

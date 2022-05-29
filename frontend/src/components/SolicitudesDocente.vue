<template>
    <td>{{solicitud_revision.id_evaluacion.id_coordinacion.coordinacion}}-{{solicitud_revision.id_evaluacion.id_coordinacion.seccion}}</td>
    <td>{{solicitud_revision.id_evaluacion.id_coordinacion.id_asignatura.nombre}}</td>
    <td>{{solicitud_revision.id_estudiante.id_usuario.first_name}} {{solicitud_revision.id_estudiante.id_usuario.last_name}}</td>
    <td>{{solicitud_revision.id_evaluacion.nombre}}</td>
    <td>{{solicitud_revision.fecha_creacion}}</td>
    <td v-if="solicitud_revision.estado == 'P'"> Pendiente</td>
    <td v-else-if="solicitud_revision.estado == 'A'"> Aprobada</td>
    <td v-else>Rechazada</td>
    <!-- Mantener id Estudiante - id Evaluacion -->
    <td>
        <button 
            type="button" 
            class="botonTabla"
            :disabled = "(solicitud_revision.estado == 'R') || (solicitud_revision.estado == 'A')" 
            @click="Ingresar(solicitud_revision.id_estudiante.id, solicitud_revision.id_evaluacion.id)">
        Responder
        </button>
    </td>
</template>

<script>
export default {
    props:{ 
        solicitud_revision: Object,
    },
    emits: ['EventIdEvaluacion'],
    methods:{
        Ingresar(idEstudiante, idEvaluacion){
            //this.$emit('EventIdEstudiante', idEstudiante)
            this.$emit('EventIdEvaluacion', idEstudiante, idEvaluacion)
        }
    }
}
</script>
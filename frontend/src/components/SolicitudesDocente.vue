<template>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
        <td>{{solicitud_revision.id_evaluacion.id_coordinacion.id_asignatura.nombre}}</td>
        <td>{{solicitud_revision.id_evaluacion.nombre}}</td>
        <td>{{solicitud_revision.motivo}}</td>
        <!-- Mantener id Estudiante - id Evaluacion -->
        <td><button type="button" class="btn btn-light" @click="Ingresar(solicitud_revision.id_estudiante.id,solicitud_revision.id_evaluacion.id)">Responder</button></td>
</template>

<script>
export default {
    props:{ 
        solicitud_revision: Array,
    },
    created(){
        console.log(this.solicitud_revision)
    },
    emits: ['EventIdEvaluacion'],
    methods:{
        Ingresar(idEstudiante,idEvaluacion){
            //this.$emit('EventIdEstudiante', idEstudiante)
            this.$emit('EventIdEvaluacion',idEstudiante,idEvaluacion)
        }
    }
}
</script>
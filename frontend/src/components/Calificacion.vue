<template>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
        <td >{{calificacion.id_evaluacion.nombre}}</td>
        <td >{{calificacion.id_observacion}}</td>
        <td>{{calificacion.nota}}</td>
        <td>{{calificacion.id_evaluacion.ponderacion}}</td>
        <td>{{calificacion.id_evaluacion.estado}}</td>
        <td>{{calificacion.fecha_entrega}}</td>
        <!--Saque estado de la evaluacion-->

        <td><button type="button" class="btn btn-light" @click.prevent="eventoClick(calificacion.id)">apelar</button></td>
</template>

<script>
export default {
    props:{ 
        calificacion: Array,
    },
    emits:['EventBoton'],
    created(){
       
    },
    methods:{
        eventoClick(id){
            this.$emit('EventBoton', id )
        }
    }
}
</script>
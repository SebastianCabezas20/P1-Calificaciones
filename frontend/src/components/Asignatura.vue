<template>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
        <td>{{asignatura.id_coordinacion.id_asignatura.codigo}}</td>
        <td>{{asignatura.id_coordinacion.id_asignatura.nombre}}</td>
        <td>{{asignatura.id_coordinacion.id_asignatura.componente}}</td>
        <td>{{asignatura.id_coordinacion.id_asignatura.nivel}}</td>

        <td><button type="button" class="btn btn-light">Más Información</button></td>
</template>

<script>
export default {
    props:{ 
        asignatura: Array,
    },
    created(){
        console.log(this.asignatura)
    }
}
</script>
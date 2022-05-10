<template>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
        <td>{{asignatura.codigo}}</td>
        <td>{{asignatura.nombre}}</td>
        <td>{{asignatura.componente}}</td>

  <button class="btn btn-outline-secondary" type="button" id="button-addon2">Detalles</button>

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
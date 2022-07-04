<template>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
        <td>{{solicitud_revision.id_solicitud_revision}}</td>
        <td>{{solicitud_revision.motivo}}</td>
        <td>{{solicitud_revision.fecha_creacion}}</td>
        <td>{{solicitud_revision.respuesta}}</td>
        <td>{{solicitud_revision.fecha_respuesta}}</td>

        <td><button type="button" class="btn btn-light">apelar</button></td>
</template>

<script>
export default {
    props:{ 
        solicitud_revision: Array,
    },
}
</script>
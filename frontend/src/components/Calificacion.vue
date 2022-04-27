    
<template>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
        <div id="filaEvaluacion" class="row row-cols-7">
            <div class="col">Evaluacion</div>
            <div class="col">Observacion</div>
            <div class="col">Calificacion</div>
            <div class="col">Ponderacion</div>
            <div class="col">Estado</div>
            <div class="col">Fecha</div>
            <button class="col btn btn-light" style="background-color:whitesmoke; padding:5px; margin:10px; border-radius: 45px;">Apelar</button>
        </div> 
    </body>
    
</template>

<script>

export default({
    data() {
        return{
            nombre:"hola"
        }
    },
})
</script>

<style>
div.col{
    font-family: 'Inter';

    font-weight: 300;
    font-size: 16px;
    line-height: 20px;
    margin: 15px;
    
}

</style>
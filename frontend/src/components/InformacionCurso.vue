<template>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
        <div id="filaInformacion" class="row row-cols-4">
            <div class="col">{{informacion.id}}</div>
            <div class="col">{{}}</div>
            <div class="col">{{}}</div>
        </div> 
    </body>
    
</template>

<script>
export default {
    props:{
        informacion:Array,
    }
}
</script>
<style>
div.col{
    font-family: 'Inter';
    font-weight: 300;
    font-size: 16px;
    
}
div.row{
    background-color: #EEEEEE;
     border-radius: 5px;
     padding: 20px;
}

</style>


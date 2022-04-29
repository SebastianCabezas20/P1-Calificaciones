<script setup>

</script>

<template>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>  
<body id="A">
    <div class="container" id="texto">
        <h4 style="color:antiquewhite; padding:10px">Apelaciones</h4>
    </div>
    <div class="container-fluid" id="contenedorTabla">
    <div class="table-responsive" id="tablaApelaciones">
        <table class="table">
            <thead id="encabezado">
                <tr>
                    <th>Titulo Apelacion</th>
                    <th>Curso</th>
                    <th>Evaluacion</th>
                    <th>Estado</th>
                    <th>Respuesta</th>
                    <th>Apelacion</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="i in 10" :key="i">
                    <td>Evaluacion</td>
                    <td>Observacion</td>
                    <td>Ponderacion</td>
                    <td>Estado</td>
                    <td><button type="button" class="btn btn-success">Ver Respuesta</button></td>
                    <td><button type="button" class="btn btn-success">Ver Apelacion</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    </div> 
</body>  
</template>

<style>

div#contenedorTabla{
    position: relative;
    background-color: #00ADB5;
    height: 500px;
    width: 1200px;
    margin-top: 30px;
    border-radius: 5px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    
}
div#tablaApelaciones{
    position: absolute;
    width: 1100px;
    height: 400px;
    background-color: #EEEEEE;
    border-radius: 5px;
    margin-top:30px;
    margin-left: 30px;
    overflow-y: auto;
    
}
thead#encabezado tr th{
    position: sticky;
    top: 0;
    z-index: 10;
    background-color: #755454 !important; 
}
div#texto{
    background-color: #00ADB5;
    margin-top: 50px;
    border-radius: 5px;
    width: 1090px;
}
</style>
<script setup>
import Calificacion from "@/components/Calificacion.vue";
import InformacionCurso from "../components/InformacionCurso.vue";
</script>

<template>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
        <div style="background-color:brown;">
            <div class="container-fluid" id="FondoSuperior">
            <div class="col-11" style="margin-left:20px; border-radius: 5px;">
                <InformacionCurso />
            </div>
            </div>
            <div class="container-fluid" id="ParteInferior">
                <div class="col-11" id="informacion">
                    <h3 id="titulo" style="padding-left:50px">Calificaciones Catedra</h3>
                </div> 
                <div class="col-11" id="Indicadores">
                        <div id="filaEvaluacion" class="row row-cols-7">
                            <div class="col">Evaluacion</div>
                            <div class="col">Observacion</div>
                            <div class="col">Calificacion</div>
                            <div class="col">Ponderacion</div>
                            <div class="col">Estado</div>
                            <div class="col">Fecha</div>
                        </div> 
                </div> 
                    <div class="container" id="filas">
                            <div v-for="i in 10" :key="i">
                                <Calificacion /> 
                            </div>
                    </div>
                <div id="estadoEstudiante" class="col-11">
                    <h4>Estado del estudiante</h4>
                </div>
            </div>
            <br>
            <div class="container-fluid" id="ParteInferior">
                <div class="col-11" id="informacion">
                    <h3 id="titulo" style="padding-left:50px">Calificaciones laboratorio</h3>
                </div> 
                 <div class="col-11" id="Indicadores">
                        <div id="filaEvaluacion" class="row row-cols-7">
                            <div class="col">Evaluacion</div>
                            <div class="col">Observacion</div>
                            <div class="col">Calificacion</div>
                            <div class="col">Ponderacion</div>
                            <div class="col">Estado</div>
                            <div class="col">Fecha</div>
                        </div> 
                </div> 
                    <div class="container" id="filas">
                            <div v-for="i in 10" :key="i">
                                <Calificacion /> 
                            </div>
                    </div>
                <div id="estadoEstudiante" class="col-11">
                    <h4>Estado del estudiante</h4>
                </div>
            </div>
        </div>
    </body>
</template>


<style>
div#Indicadores{
    position: absolute;
    background: #EEEEEE;
    margin-top: 130px;
    margin-left: 20px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 5px;

}
div#FondoSuperior
{
    background: #00ADB5;
    border-radius: 5px;
    width: 1200px;
    margin-top: 100px;
    padding: 10px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: relative;
    
}
div#filas{
    background-color: #EEEEEE;  
    margin-top: 186px;
    margin-bottom: 2cm;
    width: 1100px;
    height: 300px;
    position: absolute;
    display: inline-block;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 5px;
    margin-left: 20px;
    overflow: scroll;
        
}
div#ParteInferior
{
    width: 1200px;
    height: 575px;
    background: #00ADB5;
    border-radius: 5px; 
    position: relative;    
    overflow:visible;
    margin-top: 50px;
    
}

div#informacion{

    background: #EEEEEE;
    margin-top: 50px;
    margin-left: 20px;
    padding: 0;
    display: inline-block;
    position: absolute ;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 5px;

   
}

div#estadoEstudiante{
    background-color: #EEEEEE;  
    position: absolute;
    display: inline-block;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 5px;
    position:absolute;
    padding-left: 30px;
    bottom: 0;
    margin-bottom: 20px;
    margin-left: 20px;
    
}
</style>
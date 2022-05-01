<script setup>
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
</script>

<template>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body id="A">
    <div class="flex flex-wrap bg-gray-100 w-full h-screen">
        <Sidebar></Sidebar>
        <div class="w-5/6">
            <Navbar> </Navbar>

            <div class="container-fluid" id="FondoSuperior">
                <div class="col-11" style="margin-left:20px; border-radius: 5px;">
                    <InformacionCurso />
                </div>
                </div>
                <div class="container-fluid" id="ParteInferior">
                    <div class="col-11" id="informacion">
                        <h3 id="titulo" style="padding-left:50px">Calificaciones Catedra</h3>
                    </div> 
                        <div class="table-responsive" id="tabla">
                            <table class="table">
                            <thead id="a">
                                <tr>
                                <th>Evaluacion</th>
                                <th>Observacion</th>
                                <th>Calificacion</th>
                                <th>Ponderacion</th>
                                <th>Estado</th>
                                <th>Fecha</th>
                                <th>Apelar</th>
                                </tr>
                            </thead>
                        <tbody>
                            <tr v-for="i in 5" :key="i">
                                <CalificacionInfo />
                            </tr>
                        </tbody>
    
                    </table>
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
                        <div class="table-responsive" id="tabla">
                            <table class="table">
                            <thead id="a">
                                <tr>
                                <th>Evaluacion</th>
                                <th>Observacion</th>
                                <th>Calificacion</th>
                                <th>Ponderacion</th>
                                <th>Estado</th>
                                <th>Fecha</th>
                                <th>Apelar</th>
                                </tr>
                            </thead>
                        <tbody>
                            <tr v-for="i in 5" :key="i">
                                <CalificacionInfo />
                            </tr>
                        </tbody>
    
                    </table>
                    </div> 
                    <div id="estadoEstudiante" class="col-11">
                        <h4>Estado del estudiante</h4>
                    </div>
                </div>
                <br>
                <br>


        </div>

    </div>
            

    </body>
</template>

<style>
body#A{
    background-color:#222831;
;
}
div#tabla{
    position: absolute;
    background: #EEEEEE;
    margin-top: 130px;
    margin-left: 20px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 5px;
    width: 1100px;
    height: 300px;
    overflow-y: auto;
    overflow-x: hidden;

}

thead#a tr th{
    position: sticky;
            top: 0;
            z-index: 10;
            background-color: #755454 !important; 
}
div#FondoSuperior
{
    background: #00ADB5;
    border-radius: 5px;
    width: 1200px;
    padding: 10px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: relative;
    
}

div#ParteInferior
{
    width: 1200px;
    height: 575px;
    background: #00ADB5;
    border-radius: 5px; 
    position: relative;    
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
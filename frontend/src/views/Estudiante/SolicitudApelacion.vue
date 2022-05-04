<template>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body id="A">
    <div class="flex flex-wrap bg-gray-100">
        <Sidebar></Sidebar>
        <div class="w-5/6 ml-80">
            <Navbar> </Navbar>

            <div class="container-fluid" id="ThisParteInferior">    
                <div class="col-11" id="informacion">
                    <h3 id="titulo" style="padding-left:50px">Solicitud de Apelación</h3>
                </div>
                    <div class="col-11" style="margin-left:350px; border-radius: 5px;" id="apelacion">
                        <h5 id="titulo" style="padding-left:20px; padding-top:20px">Titulo de la Evaluación</h5>
                        <h5 id="titulo" style="padding-left:20px">Nombre de la asignatura</h5>
                        <h5 id="titulo" style="padding-left:20px">Nota</h5>
                        <h5 id="titulo" style="padding-left:20px; padding-bottom:20px">Profesor:</h5>
                        <h5 id="titulo" style="padding-left:20px">Motivo de la solicitud</h5>
                        <textarea class="ml-5 p-2.5 w-10/12 rounded-lg placeholder-gray-400" placeholder="Escriba acá su solicitud"></textarea>
                        <div>
                            <div class="col-11" style="padding-left:20px; padding-top:20px">
                                <button class="bg-azul-usach hover:bg-gray-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
                                    Apelar
                                </button>
                            </div>
                        </div>
                    </div>
            </div>

        </div>

    </div>
            

    </body>
</template>

<script>
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";

export default {
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
};
</script>

<style>
body#A{
    background-color:#222831;
;
}
div#apelacion{
    position: absolute;
    background: #EEEEEE;
    margin-top: 130px;
    margin-left: 20px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 5px;
    width: 500px;
    height: 350px;
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

div#ThisParteInferior
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

div#contenidoApelación{
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
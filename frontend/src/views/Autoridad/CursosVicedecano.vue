<template>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </head>
  <body id="A">
    <div class="flex flex-wrap bg-gray-100 w-full h-screen">
      <Sidebar> </Sidebar>

      <div class="w-5/6 ml-80">
        <Navbar> </Navbar>
        
            <div class="container-fluid" id="ThisParteInferior">    
                  <div class="col-11" id="informacion">
                      <h3 id="titulo" style="padding-left:50px">Vicedecano: Revision de Asignaturas</h3>
                  </div>
                  <div class="table-responsive" id="tabla">
                      <table class="table">
                        <thead id="a">
                          <tr>
                            <th>Código</th>
                            <th>Nombre</th>
                            <th>Nivel</th>
                            <th>Componente</th>
                            <th>Calificaciones</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="asignatura in asignaturas" :key="asignatura.id">
                            <Asignatura
                            :asignatura="asignatura" />
                          </tr>
                        </tbody>
                      </table>
                  </div>
            </div>
      </div>
    </div>
  </body>
</template>

<script>
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    Navbar,
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

div#curso{

    background: #EEEEEE;
    margin-top: 125px;
    margin-left: 20px;
    padding: 0;
    display: inline-block;
    position: absolute ;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

   
}

div#tabla {
  position: absolute;
  background: #eeeeee;
  margin-top: 130px;
  margin-left: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  width: 1100px;
  height: 300px;
  overflow-y: auto;
  overflow-x: hidden;
}
</style>


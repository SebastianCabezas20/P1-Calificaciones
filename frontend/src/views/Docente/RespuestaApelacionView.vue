<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSection">
        <h4 class="textTitle">Responder Apelacion</h4>
      </div>

      <div class="formApelacion">
        <h6 class="textoFormulario">{{apelacion[0].id_evaluacion.id_coordinacion.id_asignatura.nombre}}</h6>
        <h6 class="textoFormulario">{{apelacion[0].id_evaluacion.nombre}}</h6>
        <h6 class="textoFormulario">{{notaJson[0].nota}}</h6>

        <form>
          <input
            class="form-control relative block w-full"
            type="text"
            :value="apelacion[0].id_estudiante.id_usuario.username"
            disabled
            readonly
          />
          <label
            class="form-label relative block w-full"
            for="ApelacionContenido"
            >Apelacion del Estudiante</label
          >
          <textarea
            class="form-control relative block w-full"
            id="ApelacionContenido"
            :value="apelacion[0].motivo"
            rows="4"
            disabled
            readonly
            
          >
          </textarea
          >
          <label for="Respuesta" class="form-label relative block w-full"
            >Respuesta</label
          >
          <textarea
            class="form-control relative block w-full"
            id="ContenidoRespuesta"
            placeholder="Respuesta del Docente"
            rows="5"
            v-model="respuestaActual"
          ></textarea
          >
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="Estado"
              id="RadioAceptar"
              value="A"
              v-model="EstadoActual"
              @click="cambiarAceptado"
            />
            <label class="form-check-label" for="RadioAceptar"> Aceptar </label>
          </div>
          <div class="form-check" >
            <input
              class="form-check-input"
              type="radio"
              name="Estado"
              id="RadioRechazar"
              v-model="EstadoActual"
              value="R"
              @click="cambiarRechazado"
            />
            <label class="form-check-label" for="RadioRechazar">
              Rechazar
            </label>
          </div>
            <input type="number" v-model="notaActual" class="form-control relative" style="width:120px" v-if="isAceptar"/>
          <button class="buttonForm" @click.prevent="send">Enviar Respuesta</button>
          <h2>{{notaActual}}</h2>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';

export default {
  components: {
    Sidebar,
    Navbar,
  },
  data(){
    return{
      apelacion:[],
      notaJson:[],
      isAceptar: false,
      respuestaActual: "",
      notaActual: null,
      EstadoActual:"",


    };
  },
  methods:{
    cambiarRechazado(){
      this.isAceptar = false
    },
    cambiarAceptado(){
      this.isAceptar = true
    },
    send(){
      if(this.respuesta == ""){
        alert("NO")
      }
      else{
          let solicitud ={
          motivo: this.apelacion[0].motivo,
          fecha_creacion: "2022-05-07T00:08:23-04:00",
          respuesta: this.respuestaActual,
          estado: this.EstadoActual,
          id_estudiante:2,
          id_docente: 1,
          id_evaluacion: 2,

        } 
      
        axios.put('http://localhost:8000/actualizar/solicitud', solicitud).then(function (response){
          console.log(response.data);
        });

        if(this.isAceptar == true){
          if(this.notaActual != null){
            let notaNueva ={
              nota:this.notaActual,
              fecha_entrega:this.notaJson[0].fecha_entrega,
              id_estudiante: this.notaJson[0].id_estudiante,
              id_evaluacion: this.notaJson[0].id_evaluacion,
              id_observacion:this.notaJson[0].id_observacion,
            }
            axios.put('http://localhost:8000/actualizar/calificacion', notaNueva).then(function (response){
            console.log(response.data);
          });
          }
          else{
            alert("ingrese una nota")
          }
          
        }
      }
      
    },
  },
  created() {
    let ins = this;
    axios.get("http://localhost:8000/solicitudRespuesta").then(function (response) {
      console.log(response.data);
      ins.apelacion = response.data[0];
      ins.notaJson = response.data[1];
    });
},
};
</script>

<style></style>

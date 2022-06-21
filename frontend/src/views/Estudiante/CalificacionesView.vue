<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSectionV2" v-if="mostrarInformacionTeoria">
        <h3 class="textTitleV2">Teoría</h3>
      </div>

      <div
        class="row"
        style="margin: 0px 2px 20px 2px; padding: 10px 0px; background-color: #fff"
        v-if="mostrarInformacionTeoria"
      >
        <div class="col-sm" style="margin: 0px; padding: 0px">
          <p class="informationCalification">
            Asignatura:
            {{ informacionTeoria[0].id_coordinacion.id_asignatura.nombre }}
          </p>
          <p class="informationCalification">
            Nivel:
            {{ informacionTeoria[0].id_coordinacion.id_asignatura.nivel }}
          </p>
        </div>

        <div class="col-sm">
          <div
            class="col-sm"
            v-for="(info, id) in informacionTeoria"
            :key="info.id"
          >
            <label v-if="id == 0" class="informationCalification"
              >Docente: {{ info.id_docente.id_usuario.first_name }}
              {{ info.id_docente.id_usuario.last_name }}</label
            >
            <label
              v-else
              style="margin-left: 79px"
              class="informationCalification"
              >{{ info.id_docente.id_usuario.first_name }}
              {{ info.id_docente.id_usuario.last_name }}</label
            >
          </div>
        </div>
      </div>

      <div class="componentCourse" 
      v-if="mostrarInformacionTeoria">
        <div class="titleSectionV2">
          <h3 class="textSubTitleV2">Evaluaciones calificadas</h3>
        </div>

        <table class="tableV2">
          <thead>
            <tr>
              <th style="width: 20%">Evaluación</th>
              <th style="width: 10%">Calificación</th>
              <th style="width: 10%">Pondera</th>
              <th style="width: 20%">Fecha de realización</th>
              <th style="width: 20%">Fecha de entrega</th>
              <th style="width: 10%"></th>
              <th style="width: 10%"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="calificacion in calificacionesTeoria"
              :key="calificacion.id"
            >
              <CalificacionInfo
                :calificacion = "calificacion"
                :CalificacionSolicitudes = "this.idsCalificacionesSolicitudesTeoria"
                @EventBoton = "(id) => ingresar(id)"
                @EventMostrarInformacion = "(calificacion) => mostrarInformacion(calificacion)"
                
              />
            </tr>
            <!-- Modal que permite ver las observaciones privadas y generales de una calificación. -->
            <transition name="fase" appear>
              <div
                class="modal-overlay"
                v-if="showModalObservaciones"
                :data="modalData"
              >
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title">Observaciones</h5>
                      <button
                        type="button"
                        class="btn-close"
                        @click="showModalObservaciones = false"
                      ></button>
                    </div>
                    <div class="modal-body">
                      
                      <!-- Observación General -->
                      <div>
                        <p>Observación general: {{modalData.id_evaluacion.obs_general}}</p>
                        
                        <template v-if="modalData.id_evaluacion.adjunto !== null && modalData.id_evaluacion.adjunto !== ''">
                          <label for="obsGeneral">Archivo adjunto: {{modalData.id_evaluacion.adjunto.slice(32)}}</label>
                          <button id="obsGeneral" class="botonDescarga" @click="descargarArchivo(modalData.id_evaluacion.adjunto, 32)">
                            <i class="fa fa-download"></i>
                            Descargar
                          </button>
                        </template>
                        
                        <label v-else for="obsPrivada">Archivo adjunto: -</label>
                        
                        
                      </div>
                      
                      <div class="lineaSeparatoria"></div>
                      
                      <!-- Observación Privada -->
                      <div class="mb-3">
                        <p>Observación privada: {{modalData.obs_privada}}</p>
                        
                        <template v-if="modalData.adjunto !== null && modalData.adjunto !== ''">
                          <label for="obsPrivada">Archivo adjunto: {{modalData.adjunto.slice(33)}}</label>
                          <button id="obsPrivada" class="botonDescarga" @click="descargarArchivo(modalData.adjunto, 33)">
                            <i class="fa fa-download"></i>
                            Descargar
                          </button>
                        </template>
                        <label v-else for="obsPrivada">Archivo adjunto: -</label>
                        
                      </div>

                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-primary"
                          v-on:click="showModalObservaciones = false"
                        >
                          Cerrar
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </tbody>
        </table>

        <div class="titleSectionV2">
          <h3 class="textSubTitleV2">Evaluaciones pendientes</h3>
        </div>

        <table class="tableV2">
          <thead>
            <tr>
              <th>Evaluación</th>
              <th>Pondera</th>
              <th>Fecha de evaluación</th>
              <th>Fecha limite de entrega de notas</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="evaluacion in evaluacionesSinNotaTeoria"
              :key="evaluacion.id"
            >
              <td>{{ evaluacion.nombre }}</td>
              <td>{{ evaluacion.ponderacion * 100 }}%</td>
              <td>{{ evaluacion.fechaEvActual }}</td>
              <td>{{ evaluacion.fechaEntrega }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="lineaSeparatoria"></div>

      <div v-if="this.mostrar">
        <div class="titleSectionV2">
          <h3 class="textTitleV2">Laboratorio</h3>
        </div>

        <div
          class="row"
          style="margin: 0px 2px 20px 2px; padding: 10px 0px; background-color: #fff"
        >
          <div class="col-sm" style="margin: 0px; padding: 0px">
            <p class="informationCalification">
              Asignatura:
              {{
                informacionLaboratorio[0].id_coordinacion.id_asignatura.nombre
              }}
            </p>
            <p class="informationCalification">
              Nivel:
              {{
                informacionLaboratorio[0].id_coordinacion.id_asignatura.nivel
              }}
            </p>
          </div>
          <div class="col">
            <div
              class="col"
              v-for="(info, id) in informacionLaboratorio"
              :key="info.id"
            >
              <label v-if="id == 0" class="informationCalification"
                >Docente: {{ info.id_docente.id_usuario.first_name }}
                {{ info.id_docente.id_usuario.last_name }}</label
              >
              <label
                v-else
                style="margin-left: 79px"
                class="informationCalification"
                >{{ info.id_docente.id_usuario.first_name }}
                {{ info.id_docente.id_usuario.last_name }}</label
              >
            </div>
          </div>
        </div>

        <div class="componentCourse">
          <div class="titleSectionV2">
            <h3 class="textSubTitleV2">Evaluaciones calificadas</h3>
          </div>
          <table class="tableV2">
            <thead>
              <tr>
                <th style="width: 20%">Evaluación</th>
                <th style="width: 10%">Calificación</th>
                <th style="width: 10%">Pondera</th>
                <th style="width: 20%">Fecha de realización</th>
                <th style="width: 20%">Fecha de entrega</th>
                <th style="width: 10%"></th>
                <th style="width: 10%"></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="calificacion in calificacionesLaboratorio"
                :key="calificacion.id"
              >
                <CalificacionInfo
                  :calificacion = "calificacion"
                  :CalificacionSolicitudes = "this.idsCalificacionesSolicitudesLab"
                  @EventBoton = "(id) => ingresar(id)" 
                  @EventMostrarInformacion = "(calificacion) => mostrarInformacion(calificacion)"
                />
              </tr>
            </tbody>
          </table>

          <div class="titleSectionV2">
            <h3 class="textSubTitleV2">Evaluaciones pendientes</h3>
          </div>

          <table class="tableV2">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Ponderacion</th>
                <th>Fecha de evaluación</th>
                <th>Fecha limite de entrega de notas</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="evaluacion in evaluacionesSinNotaLaboratorio"
                :key="evaluacion.id"
              >
              <td>{{ evaluacion.nombre }}</td>
              <td>{{ evaluacion.ponderacion * 100 }}%</td>
              <td>{{ evaluacion.fechaEvActual }}</td>
              <td>{{ evaluacion.fechaEntrega }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";
import axios from "axios";
import router from "../../router";

export default {
  data() {
    return {
      calificacionesTeoria: [],
      evaluacionesSinNotaTeoria: [],
      informacionTeoria: [],
      calificacionesLaboratorio: [],
      evaluacionesSinNotaLaboratorio: [],
      informacionLaboratorio: [],
      mostrar: false,
      mostrarInformacionTeoria: false,
      idsCalificacionesSolicitudesTeoria: [],
      idsCalificacionesSolicitudesLab: [],
      modalData: null,
      showModalObservaciones: false,
    };
  },
  props: ["codigoAsignatura"],
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
  created() {
    let ins = this;
    let codigoAsig = this.codigoAsignatura;
    const idUsuario = this.$store.getters.idUsuario;

    axios
      .get(
        `http://localhost:8000/calificacionesTeoria/${codigoAsig}/${idUsuario}`
      )
      .then(function (response) {
        ins.calificacionesTeoria = response.data[0];
        ins.evaluacionesSinNotaTeoria = response.data[1];
        ins.idsCalificacionesSolicitudesTeoria = response.data[2];
        ins.informacionTeoria = response.data[3]
        ins.mostrarInformacionTeoria = true
      });

    axios
      .get(
        `http://localhost:8000/calificacionesLaboratorio/${codigoAsig}/${idUsuario}`
      )
      .then(function (response) {
        if (response.data[0].length != 0) {
          ins.calificacionesLaboratorio = response.data[0];
          ins.evaluacionesSinNotaLaboratorio = response.data[1];
          ins.idsCalificacionesSolicitudesLab = response.data[2];
          ins.informacionLaboratorio = response.data[3]
          ins.mostrar = true;
        }
      });

  },
  methods: {
    ingresar(idCalificacion) {
      router.push(`/estudiante/add/solicitud/${idCalificacion}`);
    },

    mostrarInformacion(calificacion) {
      this.modalData = calificacion;
      this.showModalObservaciones = true;
    },
    
    /* Método que descarga un archivo. Se debe entregar el nombre 
    del archivo guardado en la bd (atributo adjunto) e indicar
    la cantidad de caracteres que tiene la ruta en la cual está
    almacenada dicho archivo.  */
    descargarArchivo(archivo, indexSlice) {
      let nombreArchivo = archivo.slice(indexSlice);
      axios.get(`http://localhost:8000${archivo}`, {
        responseType: 'blob',
      }).then((response) => {
        const downloadUrl = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.setAttribute('download', nombreArchivo);
        document.body.appendChild(link);
        link.click();
    });
    }
  },
};
</script>

<style></style>

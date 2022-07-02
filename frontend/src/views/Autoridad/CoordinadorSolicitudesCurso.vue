<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSectionV2">
        <h4 class="textTitleV2">Solicitudes de revisión</h4>
      </div>
      <!--Filtros-->
      <div class="row" style="background-color: #ffffff">
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Evaluación</span>
            <input
              type="text"
              class="form-control"
              v-model="evaluacionFiltro"
              placeholder="Evaluación a buscar"
            />
            <span class="input-group-text mt-4">Docente</span>
            <input
              type="text"
              class="form-control"
              v-model="docenteFiltro"
              placeholder="Docente a buscar"
            />
          </div>
        </div>
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Estudiante</span>
            <input
              type="text"
              class="form-control"
              v-model="estudianteFiltro"
              placeholder="Estudiante a buscar"
            />
          </div>
          <div class="input-group row">
            <h6>Estados posibles</h6>
            <!-- Botones para la seleccion de estados -->
            <div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic checkbox toggle button group"
              >
                <input
                  type="checkbox"
                  class="btn-check"
                  v-model="rechazadas"
                  value="R"
                  id="rechazada"
                  autocomplete="off"
                />
                <label class="btn btn-outline-primary" for="rechazada">
                  Rechazadas</label
                >
              </div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic checkbox toggle button group"
                style="margin-left: 30px"
              >
                <input
                  type="checkbox"
                  class="btn-check"
                  v-model="aprobadas"
                  value="A"
                  id="aprobadas"
                  autocomplete="off"
                />
                <label class="btn btn-outline-primary" for="aprobadas">
                  Aprobadas</label
                >
              </div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic checkbox toggle button group"
                style="margin-left: 30px"
              >
                <input
                  type="checkbox"
                  class="btn-check"
                  v-model="pendientes"
                  value="P"
                  id="pendiente"
                  autocomplete="off"
                />
                <label class="btn btn-outline-primary" for="pendiente">
                  Pendientes</label
                >
              </div>
              <div class="btn-group" role="group" aria-label="Basic checkbox toggle button group" style="margin-left:30px">
              <input type="checkbox" class="btn-check" v-model="revisions" value="E" id="revision" autocomplete="off">
              <label class="btn btn-outline-primary" for="revision"> En revision</label>
            </div>
            </div>
          </div>
        </div>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th>Evaluación</th>
            <th>Docente</th>
            <th>Fecha de creación</th>
            <th>Estudiante</th>
            <th>Detalle</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody v-for="solicitud in solicitudes" :key="solicitud.id">
          <ApelacionesCoordinador
            :solicitud="solicitud"
            :pendiente="this.pendientes"
            :aprobada="this.aprobadas"
            :rechazada="this.rechazadas"
            :evaluacionFiltro="this.evaluacionFiltro"
            :docente="this.docenteFiltro"
            :estudiante="this.estudianteFiltro"
            :revision="this.revisions"
          />
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import ApelacionesCoordinador from "../../components/ApelacionesCoordinador.vue";
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
    ApelacionesCoordinador,
  },
  props: ["idCurso"],
  data() {
    return {
      solicitudes: [],
      estudianteFiltro: "",
      evaluacionFiltro: "",
      docenteFiltro: "",
      aprobadas: true,
      rechazadas: true,
      pendientes: true,
      revisions: true,
    };
  },
  created() {
    let ins = this;
    let IDcurso = this.idCurso;
    axios
      .get(`http://localhost:8000/coordinacion/solicitudes/${IDcurso}`)
      .then(function (response) {
        console.log(response.data);
        ins.solicitudes = response.data;
      });
  },
};
</script>

<style></style>

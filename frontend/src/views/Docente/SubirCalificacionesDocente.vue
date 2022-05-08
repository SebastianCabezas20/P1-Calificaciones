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
        <h3 class="textTitle">Calificación de Estudiantes</h3>
      </div>

      <div class="container-fluid">
        <div class="row">
          <div class="col-sm">
            <p class="informationCalification">Nombre de la Asignatura</p>
            <p class="informationCalification">Coordinación - Sección</p>
            <p class="informationCalification">Nombre de la Evaluacion</p>
            <p class="informationCalification">Fecha de la Evaluacion</p>
          </div>

          <div class="col-sm">
            <span class="input-group-text">Observación General</span>
            <textarea
              class="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>

          <div class="col-sm">
            <label for="formFile" class="form-label">Adjuntar planilla</label>
            <input
              class="form-control"
              type="file"
              id="formFile"
              @change="onChange"
            />
          </div>
        </div>

        <div class="tableContent">
          <table class="table">
            <thead>
              <tr>
                <th></th>
                <th>Nombre</th>
                <th>Rut</th>
                <th>Calificación</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="calificacion in calificacionesEstudiantes"
                :key="calificacion.id"
              >
                <CalificacionEstudiante :calificacionEstudiante="calificacion" />
              </tr>
            </tbody>
          </table>
        </div>

        <div class="w-25">
          <button type="button" class="btn btn-primary">
            Subir calificaciones
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import * as XLSX from "xlsx";
import axios from "axios";
import CalificacionEstudiante from "../../components/CalificacionesEstudiante.vue";

export default {
  components: {
    Sidebar,
    Navbar,
    CalificacionEstudiante,
  },
  data() {
    return {
      calificacionesEstudiantes: [],
      estudiantesPlanilla: [],
    };
  },
  mounted() {
    let ins = this;
    axios
      .get("http://localhost:8000/calificacionesEstudiantes")
      .then(function (response) {
        ins.calificacionesEstudiantes = response.data;
      });
  },
  methods: {
    onChange(event) {
      this.file = event.target.files ? event.target.files[0] : null;

      if (this.file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          /* Analizar el excel */
          const bstr = e.target.result;
          const wb = XLSX.read(bstr, { type: "binary" });
          
          /* Obtener primera hoja. */
          const wsname = wb.SheetNames[0];
          const ws = wb.Sheets[wsname];

          /* Convertir los datos en un arreglo de arreglos. */
          this.estudiantesPlanilla  = XLSX.utils.sheet_to_json(ws, { header: 1, range: 1 });
          console.log(this.estudiantesPlanilla);
        };

        reader.readAsBinaryString(this.file);
      }
    },
  },
};
</script>

<style>
.algo {
  border: 2px solid blue;
}

.informationCalification {
  color: #000;
  font-size: 17px;
  font-weight: bold;
  margin: 0;
  padding: 4px;
}
</style>

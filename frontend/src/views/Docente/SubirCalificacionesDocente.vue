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
            <p class="informationCalification">
              Nombre: {{ this.informacionEvaluacion.nombre }}
            </p>

            <p
              v-if="this.informacionEvaluacion.estado == 'P'"
              class="informationCalification"
            >
              Estado: Pendiente
            </p>
            <p v-else class="informationCalification">Estado: Evaluada</p>

            <p class="informationCalification">
              Fecha de realización:
              {{ this.informacionEvaluacion.fechaEvActual }}
            </p>
            <p class="informationCalification">
              Fecha tentativa de entrega de notas:
              {{ this.informacionEvaluacion.fechaEntrega }}
            </p>
          </div>

          <div class="col-sm">
            <span class="input-group-text">Observación General</span>
            <textarea
              class="form-control"
              aria-label="With textarea"
              v-model="observacion"
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
                <th>Apellido</th>
                <th>Rut</th>
                <th>D. Verificador</th>
                <th>Calificación</th>
              </tr>
            </thead>

            <!-- Docente sube una planilla de notas.  -->
            <tbody>
              <tr
                v-for="(calificacion, index) in calificacionesEstudiantes"
                :key="calificacion.id"
              >
                <td>
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="defaultCheck1"
                  />
                </td>
                <td>
                  {{ calificacion.id_estudiante.id_usuario.first_name }}
                </td>
                <td>
                  {{ calificacion.id_estudiante.id_usuario.last_name }}
                </td>
                <td>
                  {{ calificacion.id_estudiante.rut }}
                </td>
                <td>
                  {{ calificacion.id_estudiante.dig_verificador }}
                </td>
                <td>{{ calificacion.nota }}</td>

                <td>
                  <input
                    class="form-control"
                    type="text"
                    placeholder="Calificación"
                    required
                    v-model="calificacionesEstudiantes[index].nota"
                  />
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="w-25">
          <button
            v-on:click="submitCalificaciones"
            type="button"
            class="btn btn-primary"
          >
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

export default {
  props: ["idEvaluacion", "idCurso"],
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      calificacionesEstudiantes: [],
      estudiantesPlanilla: [],
      calificaciones: [],
      observacion: "",
      informacionEvaluacion: [],
    };
  },
  mounted() {
    let identificacionEvaluacion = this.idEvaluacion;
    let identificacionCurso = this.idCurso;
    let ins = this;
    axios
      .get(
        `http://localhost:8000/calificacion/coordinacion/${identificacionCurso}`
      )
      .then(function (response) {
        ins.calificacionesEstudiantes = response.data;
      });
    axios
      .get(`http://localhost:8000/evaluacion/${identificacionEvaluacion}`)
      .then(function (response) {
        ins.informacionEvaluacion = response.data;
      });
  },

  updated() {
    let ins = this;
    let identificacionEvaluacion = this.idEvaluacion;
    axios
      .get(`http://localhost:8000/evaluacion/${identificacionEvaluacion}`)
      .then(function (response) {
        ins.informacionEvaluacion = response.data;
      });
  },
  methods: {
    onChange(event) {
      this.file = event.target.files ? event.target.files[0] : null;

      if (this.file) {
        const reader = new FileReader();
        let that = this;
        reader.onload = function (e) {
          /* Analizar el excel */
          const bstr = e.target.result;
          const wb = XLSX.read(bstr, { type: "array" });

          /* Obtener primera hoja. */
          const wsname = wb.SheetNames[0];
          const ws = wb.Sheets[wsname];

          /* Convertir los datos en un arreglo de arreglos. */
          const data = XLSX.utils.sheet_to_json(ws, {
            header: 1,
            range: 1,
          });
          console.log(data);
        };
        reader.readAsArrayBuffer(this.file);
      }
    },
    // Funcionando. Falta ver el tema de las observaciones,
    // cambiar el estado de la evaluacion y bloquear la calificacion en aquel caso
    submitCalificaciones() {
      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);
      let nuevaCalificacion;

      for (var i = 0; i < this.calificacionesEstudiantes.length; i++) {
        nuevaCalificacion = {
          nombre: this.calificacionesEstudiantes[i].id_estudiante.rut,
          nota: this.calificacionesEstudiantes[i].nota,
          fecha_entrega: fechaActual,
          id_estudiante: this.calificacionesEstudiantes[i].id_estudiante.id,
          id_evaluacion: this.idEvaluacion,
          id_observacion: null,
        };
        axios
          .post("http://localhost:8000/add/calificacion", nuevaCalificacion)
          .then(function (response) {});
      }

      let nuevaEvaluacion = {
        nombre: this.informacionEvaluacion.nombre,
        fechaEvActual: this.informacionEvaluacion.fechaEvActual,
        fechaEntrega: this.informacionEvaluacion.fechaEntrega,
        ponderacion: this.informacionEvaluacion.ponderacion,
        estado: "E",
        id_tipoEvaluacion: this.informacionEvaluacion.id_tipoEvaluacion,
        id_docente: this.informacionEvaluacion.id_docente,
        id_observacion: this.informacionEvaluacion.id_observacion,
        id_coordinacion: this.informacionEvaluacion.id_coordinacion,
      };
      axios
        .put(
          `http://localhost:8000/update/evaluacion/${this.idEvaluacion}`,
          nuevaEvaluacion
        )
        .then(function (response) {});
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

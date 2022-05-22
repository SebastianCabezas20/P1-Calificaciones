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
        <h3 class="textTitleV2">Calificación de Estudiantes</h3>
      </div>

      <!-- Modificar el diseño con el que se muestra la información, por algo mas moderno. -->
      <div class="row" style="background-color: #ffffff">
        <div class="col-sm-8 p-0">
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
            Fecha límite de entrega de notas:
            {{ this.informacionEvaluacion.fechaEntrega }}
          </p>
        </div>

        <div class="col-sm-4">
          <label for="formFile" class="form-label">Adjuntar planilla</label>
          <input
            class="form-control"
            type="file"
            id="formFile"
            @change="onChange"
          />
        </div>
      </div>

      <form @submit.prevent="submitCalificaciones" action="POST">
        <table class="tableV2">
          <thead>
            <tr>
              <th style="width: 4%"></th>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>Rut</th>
              <th>D. Verificador</th>
              <th>Calificación</th>
              <th></th>
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
                  type="number"
                  min="1"
                  max="7"
                  step="0.1"
                  placeholder="Calificación"
                  required
                  v-model="calificacionesEstudiantes[index].nota"
                />
              </td>
            </tr>
          </tbody>
        </table>
        <button type="submit" class="submitButton">Subir calificaciones</button>
      </form>
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

          // Carga de datos en la tabla.
          for (var i = 0; i < that.calificacionesEstudiantes.length; i++) {
            for (var j = 0; j < data.length; j++) {
              if (
                that.calificacionesEstudiantes[i].id_estudiante.rut ==
                  data[j][0] &&
                that.calificacionesEstudiantes[i].id_estudiante
                  .dig_verificador == data[j][1]
              ) {
                that.calificacionesEstudiantes[i].nota = data[j][2];
              }
            }
          }
        };
        reader.readAsArrayBuffer(this.file);
      }
    },
    // Funcionando. Falta ver el tema de las observaciones (Sprint 2 o 3),
    // Falta bloquear la calificacion cuando se califica (Sprint 2 o 3)
    submitCalificaciones() {
      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);
      let nuevaCalificacion;
      let that = this;

      for (var i = 0; i < this.calificacionesEstudiantes.length; i++) {
        nuevaCalificacion = {
          nombre: this.calificacionesEstudiantes[i].id_estudiante.rut,
          nota: this.calificacionesEstudiantes[i].nota,
          fecha_entrega: fechaActual,
          obs_privada: '',
          id_estudiante: this.calificacionesEstudiantes[i].id_estudiante.id,
          id_evaluacion: this.idEvaluacion,
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
        obs_general: this.informacionEvaluacion.obs_general,
        adjunto: this.informacionEvaluacion.adjunto,
        id_tipoEvaluacion: this.informacionEvaluacion.id_tipoEvaluacion,
        id_docente: this.informacionEvaluacion.id_docente,
        id_coordinacion: this.informacionEvaluacion.id_coordinacion,
      };
      axios
        .put(
          `http://localhost:8000/update/evaluacion/${this.idEvaluacion}`,
          nuevaEvaluacion
        )
        .then(function (response) {
          that.$swal
            .fire({
              icon: "success",
              title: "Calificación exitosa",
              text: "Los estudiantes fueron calificados satisfactoriamente",
            })
            .then((result) => {
              that.$router.push({ path: `/docente/curso/${that.idCurso}` });
            });
        });
    },
  },
};
</script>

<style></style>

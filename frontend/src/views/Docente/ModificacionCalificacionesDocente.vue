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
        <h3 class="textTitle">Evaluaciones</h3>
      </div>

      <div class="tableContent">
            <table class="table">
              <thead class="text-center">
                <tr>
                  <th>Rut</th>
                  <th>Dígito Verificador</th>
                  <th>Nota</th>
                  <th>Modificar Calificación</th>
                </tr>
              </thead>
              <tbody class="text-center">
                <tr v-for="(calificacion, index) in calificaciones" :key="index">
                  <td>{{ calificacion.id_estudiante.rut }}</td>
                  <td>{{ calificacion.id_estudiante.dig_verificador }}</td>
                  <td>{{ calificacion.nota }}</td>
                  <td>
                    <div class="text-center">
                      <button
                        @click="(showModal = true), (modalIndex = index)"
                        class="fa-solid fa-pencil botonTabla"
                        title="Modificar calificación"
                      ></button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Modal Modificar Fecha-->
          <transition name="fase" appear>
            <div class="modal-overlay" v-if="showModal">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">
                      Modificar Calificación
                    </h5>
                    <button
                      type="button"
                      class="btn-close"
                      @click="showModalFecha = false"
                    ></button>
                  </div>

                  <div class="modal-body">
                    <form
                      action="#"
                      method="PUT"
                      v-on:submit.prevent="modificarCalificacion($event, modalIndex)"
                    >
                      <div class="mb-3">
                        <label class="form-label"
                          >Nueva Calificacion</label
                        >
                        <input
                          v-model="nuevaCalificacion"
                          class="form-control"
                          placeholder="1.0"
                          required
                        />
                      </div>

                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-secondary"
                          v-on:click="showModalFecha = false"
                        >
                          Cancelar
                        </button>
                        <button type="submit" class="btn btn-primary">
                          Guardar Cambios
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </transition>
        </div>
      </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  // Aqui estan las variables capturadas del url.
  data() {
    return {
      calificaciones: [],
      showModal: false,
      indexModal: "",
      nuevaCalificacion: "",
    };
  },
  mounted() {
    let ins = this;
    axios
      .get(`http://localhost:8000/calificacionesDocente/${this.$store.getters.idUsuario}`)
      .then(function (response) {
        console.log(response.data);
        ins.calificaciones = response.data;
        
      });
  },
  methods: {
    modificarCalificacion: function (event, index) {
      console.log(this.calificaciones[index]);
      let idCalificacionModificar = this.calificaciones[index].id;
      let nuevaCalificacion = {
        nota: this.nuevaCalificacion,
        fecha_entrega: this.calificaciones[index].fecha_entrega,
        id_estudiante: this.calificaciones[index].id_estudiante.id,
        id_evaluacion: this.calificaciones[index].id_evaluacion.id,
        id_observacion: this.calificaciones[index].id_observacion,
      };
      console.log(nuevaCalificacion);
      axios
        .put(
          `http://localhost:8000/updateCalificacion/${idCalificacionModificar}`,
          nuevaCalificacion
        )
        .then(function (response) {
          location.reload();
        });
    },
  },
};
</script>

<style>
.centralContent {
  margin: auto;
  width: 98%;
  margin-top: 10px;
  font-family: "Inter", sans-serif;
}

.titleSection {
  display: block;
  background: #c4c4c4;
  border: 2px solid #004883;
  border-radius: 20px;
  padding: 3px;
  margin-bottom: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.textTitle {
  text-align: center;
  font-size: 30px;
  color: #000;
  font-weight: 600;
}

.tableContent {
  background: #c4c4c4;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  border: 2px solid #004883;
  overflow-y: auto;
  overflow-x: hidden;
  margin-bottom: 20px;
}

.tableContent .table {
  border-collapse: collapse;
}

.tableContent .table thead tr {
  text-align: center;
}

.tableContent .table thead tr th {
  padding: 8px;
}
</style>

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
        <h4 class="textTitle">Apelaciones</h4>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Titulo Apelacion</th>
              <th>Curso</th>
              <th>Evaluacion</th>
              <th>Estado</th>
              <th>Respuesta</th>
              <th>Apelacion</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in 10" :key="i">
              <td>Evaluacion</td>
              <td>Observacion</td>
              <td>Ponderacion</td>
              <td>Estado</td>
              <td>
                <button type="button" class="btn btn-success">
                  Ver Respuesta
                </button>
              </td>
              <td>
                <button type="button" class="btn btn-success">
                  Ver Apelacion
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarAutoridad.vue";
import Navbar from "../../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    Navbar,
  },
};
</script>

<style></style>

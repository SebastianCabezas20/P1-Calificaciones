<template>
  <div class="mt-5 titleSectionV2">
    <h3 class="textTitleV2">Modificaciones</h3>
  </div>
  <table class="tableV2">
    <thead>
      <tr>
        <th>Evaluación</th>
        <th>Fecha de rendición</th>
        <th>Estado</th>
        <th>Pondera</th>
        <th>Acción</th>
        <th class="row-ButtonIcon"></th>
      </tr>
    </thead>
    <tbody>
      <!-- Evaluaciones creadas momentáneamente. -->
      <tr
        v-for="(evaluacion, index) in evaluacionesCreadas"
        style="background-color: #b8daba"
      >
        <td>{{ evaluacion.nombre }}</td>
        <td>{{ evaluacion.fechaEvActual }}</td>
        <td v-if="evaluacion.estado === 'P'">Pendiente</td>
        <td v-else>Evaluada</td>
        <td>{{ evaluacion.ponderacion * 100 }}%</td>
        <td>Crear</td>
        <td>
          <div class="text-center">
            <button
              class="fa-solid fa-trash-can botonTabla"
              @click="deshacerAccion(1, index)"
            ></button>
          </div>
        </td>
      </tr>
      <!-- Evaluaciones elimindas momentáneamente. -->
      <tr
        v-for="(evaluacion, index) in evaluacionesEliminadas"
        style="background-color: #ffbfaa"
      >
        <td>{{ evaluacion.nombre }}</td>
        <td>{{ evaluacion.fechaEvActual }}</td>
        <td v-if="evaluacion.estado === 'P'">Pendiente</td>
        <td v-else>Evaluada</td>
        <td>{{ evaluacion.ponderacion * 100 }}%</td>
        <td>Eliminar</td>
        <td>
          <div class="text-center">
            <button
              class="fa-solid fa-trash-can botonTabla"
              @click="deshacerAccion(2, index)"
            ></button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>

  <button
    id="botonGuardar"
    type="button"
    class="submitButton mb-5"
    @click="guardarCambios()"
  >
    Guardar cambios
  </button>
</template>

<script>
export default {
  props: {
    evaluacionesCreadas: Array,
    evaluacionesEliminadas: Array,
  },
  emits: ["EventGuardarCambios"],
  methods: {
    deshacerAccion(numArray, index) {
      // Arreglo de evaluaciones creadas.
      if (numArray === 1) {
        this.evaluacionesCreadas.splice(index, 1);
      }
      // Arreglo de evaluaciones eliminadas.
      else if (numArray === 2) {
        this.evaluacionesEliminadas.splice(index, 1);
      } 
      // Posibilidad para agregar la modificación de ponderaciones.
      else {
      }
    },
    guardarCambios() {
      this.$emit("EventGuardarCambios");
    },
  },
};
</script>

<style></style>

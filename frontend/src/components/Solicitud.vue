<template>
  <td>{{ solicitud.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
  <td>{{ solicitud.id_evaluacion.nombre }}</td>
  <td v-if="solicitud.estado == 'P'">Pendiente</td>
  <td v-else-if="solicitud.estado == 'A'">Aceptada</td>
  <td v-else-if="solicitud.estado == 'E'">En revisión</td>
  <td v-else>Rechazada</td>
  <td>{{ solicitud.motivo }}</td>
  <td>{{ solicitud.respuesta }}</td>
  <td @click="showTrack = true">
    <span class="fa-solid fa-info botonTabla"></span>
  </td>

  <transition name="fase" appear>
    <div class="modal-overlay" v-if="showTrack">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Seguimiento de solicitud</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
              @click="showTrack = false"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col-12 pt-1 pb-1">
                <div class="row justify-content-between">
                  <div class="track completed">
                    <span class="is-complete"></span>
                    <p>
                      Enviado<br /><span
                        >La solicitud de revisión fue enviada
                        satisfactoriamente</span
                      >
                    </p>
                  </div>

                  <!-- Segundo paso. -->
                  <div v-if="solicitud.estado == 'P'" class="track">
                    <span class="is-complete"></span>
                    <p>
                      En revisión<br /><span
                        >La o él docente se encuentra revisando la
                        solicitud</span
                      >
                    </p>
                  </div>
                  <div v-else class="track completed">
                    <span class="is-complete"></span>
                    <p>
                      En revisión<br /><span
                        >La o él docente se encuentra revisando la
                        solicitud</span
                      >
                    </p>
                  </div>

                  <!-- Último paso. -->
                  <!-- Se verifica si la solicitud fue aprobada o rechazada.-->
                  <div v-if="solicitud.estado == 'R'" class="track rejected">
                    <span class="is-complete"></span>
                    <p>
                      Rechazada<br /><span
                        >Su solicitud de revisión fue rechazada y su
                        calificación se mantiene</span
                      >
                    </p>
                  </div>

                  <div
                    v-else-if="solicitud.estado == 'A'"
                    class="track completed"
                  >
                    <span class="is-complete"></span>
                    <p>
                      Aprobada<br /><span
                        >Su solicitud de revisión fue aprobada y su calificación
                        ya se encuentra actualizada</span
                      >
                    </p>
                  </div>

                  <div v-else class="track">
                    <span class="is-complete"></span>
                    <p>
                      Respuesta<br /><span
                        >La o él docente aprueba o rechaza la solicitud de
                        revisión enviada</span
                      >
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
              @click="showTrack = false"
            >
              Cerrar
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    solicitud: Object,
  },
  data() {
    return {
      showTrack: false,
    };
  },
};
</script>

<style></style>

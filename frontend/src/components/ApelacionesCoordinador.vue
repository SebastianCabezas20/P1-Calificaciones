<template>
    <tr >
        <td>{{solicitud.id_evaluacion.nombre}}</td>
        <td v-if="solicitud.estado == 'A'">Aprobada</td>
        <td v-else-if="solicitud.estado == 'R'" >Rechazado</td>
        <td v-else >Pendiente</td>
        <td>{{solicitud.fecha_creacion}}</td>
        <td>{{solicitud.id_estudiante.id_usuario.username}}</td>
        <td>
        <button type="button" @click="showModal = !showModal" class="btn btn-success">
            Detalles
        </button>
        </td>
    </tr>
    <transition name="fase" appear >
            <div class="modal-overlay" v-if="showModal">
                <div class="modal-dialog" >
                <div class="modal-content" style="width:1000px">
                    <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">
                        Detalles
                    </h5>
                    <button
                        type="button"
                        class="btn-close"
                        @click="showModal = false"
                    ></button>
                    </div>

                    <div class="modal-body">
                    <div class="container">
                        <div class="row">
                            <div class="col-5">Motivo</div>
                            <div class="col-5">{{solicitud.motivo}}</div>
                        </div>
                        <div class="row">
                            <div class="col-5">Respuesta</div>
                            <div class="col-5">{{solicitud.respuesta}}</div>
                        </div>
                        <div class="row">
                            <div class="col-5">Fecha Respuesta</div>
                            <div class="col-5">{{solicitud.fecha_respuesta}}</div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
    </transition>
</template>

<script>
export default {
    data(){
        return{
            showModal: false,
        }
    },
    props:{
        solicitud: Array,

    }
}
</script>
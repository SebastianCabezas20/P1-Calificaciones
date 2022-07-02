<template>
    <tr  :style="[solicitud.estado == 'A' ? {'background-color':'#90EE90'} : solicitud.estado == 'R' ? {'background-color': '#ffbfaa'} : solicitud.estado == 'E' ? {'background-color':'#86aad3'} : {'background-color':'null'}]"
    v-show="filtroEstado(solicitud.estado) && filtroEvaluacion(solicitud.id_evaluacion.nombre)
    && filtroDocente(solicitud.id_docente.id_usuario.first_name,solicitud.id_docente.id_usuario.last_name)
    && filtroEstudiante(solicitud.id_estudiante.id_usuario.first_name,solicitud.id_estudiante.id_usuario.last_name)">
        <td>{{solicitud.id_evaluacion.nombre}}</td>
        <td>{{solicitud.id_docente.id_usuario.first_name}} {{solicitud.id_docente.id_usuario.last_name}}</td>
        
        <td>{{solicitud.fecha_creacion}}</td>
        <td>{{solicitud.id_estudiante.id_usuario.first_name}} {{solicitud.id_estudiante.id_usuario.last_name}}</td>
        <td v-if="solicitud.estado == 'A'">Aprobada</td>
        <td v-else-if="solicitud.estado == 'R'" >Rechazado</td>
        <td v-else-if="solicitud.estado == 'E'" >En revision</td>
        <td v-else >Pendiente</td>
        <td>
        <button type="button" @click="showModal = !showModal" class="btn btn-success">
            Detalles
        </button>
        </td>
    </tr>
    
    <transition name="fase" appear>
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
                            <div class="col">Estudiante solicitante</div>
                            <div class="col">{{solicitud.id_estudiante.id_usuario.username}}</div>
                        </div>
                        <div class="row">
                            <div class="col">Profesor responsable</div>
                            <div class="col">{{solicitud.id_docente.id_usuario.username}}</div>
                        </div>
                        <div class="row">
                            <div class="col">Estado</div>
                            <div class="col" v-if="solicitud.estado == 'A'" >Aprobada</div>
                            <div class="col" v-else-if="solicitud.estado == 'R'" >Rechazado</div>
                            <div class="col" v-else-if="solicitud.estado == 'E'" >En revision</div>
                            <div class="col" v-else>Pendiente</div>
                        </div>
                        <div class="row">
                            <div class="col">Motivo</div>
                            <div class="col">{{solicitud.motivo}}</div>
                        </div>
                        <div class="row">
                            <div class="col">Fecha de creación</div>
                            <div class="col">{{solicitud.fecha_creacion}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado != 'P' && solicitud.estado != 'E'">
                            <div class="col">Respuesta</div>
                            <div class="col">{{solicitud.respuesta}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado != 'P' && solicitud.estado != 'E'">
                            <div class="col">Fecha de respuesta</div>
                            <div class="col">{{solicitud.fecha_respuesta}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado == 'P' || solicitud.estado == 'R' ||  solicitud.estado == 'E'">
                            <div class="col-3">Calificación actual</div>
                            <div class="col-3">{{solicitud.actual_nota}}</div>
                            <div class="col-3">Fecha de publicación</div>
                            <div class="col-3">{{solicitud.id_calificacion.fecha_entrega}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado == 'A'">
                            <div class="col-3">Nueva calificación</div>
                            <div class="col-3">{{solicitud.actual_nota}}</div>
                            <div class="col-3">Fecha de publicación</div>
                            <div class="col-3">{{solicitud.fecha_respuesta}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado == 'A'">
                            <div class="col-3">Calificación anterior</div>
                            <div class="col-3">{{solicitud.anterior_nota}}</div>
                            <div class="col-3">Fecha de publicación</div>
                            <div class="col-3">{{solicitud.id_calificacion.fecha_entrega}}</div>
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
            color: null
        }
    },
    props:{
        solicitud: Array,
        evaluacionFiltro: String,
        estudiante: String,
        docente: String,
        aprobada: Boolean,
        rechazada: Boolean,
        pendiente: Boolean,
        revision: Boolean,
    },
    methods:{
        filtroEstado(estado){
            if(estado == 'A'){
                return this.aprobada
            }
            else if(estado == 'R'){
                return this.rechazada
            }
            else if(estado == 'P'){
                return this.pendiente
            }
            else if(estado == 'E'){
                return this.revision
            }
            else{
                return false
            }
        },
        filtroEvaluacion(evaluacion){
            let n = Array(evaluacion)
            return n[0].toLocaleLowerCase().indexOf(this.evaluacionFiltro.toLocaleLowerCase()) >= 0
        },
        filtroDocente(nombre,apellido){
            let n = Array(nombre+' '+apellido)
            return n[0].indexOf(this.docente) >= 0
        },
        filtroEstudiante(nombre,apellido){
            let n = Array(nombre+' '+apellido)
            return n[0].indexOf(this.estudiante) >= 0
        }

    }
}
</script>
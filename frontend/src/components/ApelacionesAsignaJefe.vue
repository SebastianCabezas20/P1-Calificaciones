<template>
    <tr
    v-show="filterSecciones(solicitud.id_evaluacion.id_coordinacion.coordinacion,solicitud.id_evaluacion.id_coordinacion.seccion) &&
    filterEvaluacion(solicitud.id_evaluacion.nombre) && filterEstado(solicitud.estado) &&
    filterDocente(solicitud.id_docente.id_usuario.first_name, solicitud.id_docente.id_usuario.last_name)" 
    :style="[solicitud.estado == 'A' ? {'background-color':'#90EE90'} : solicitud.estado == 'R' ? {'background-color': '#ffbfaa'} : {'background-color':'null'}]">
    
        <td>{{solicitud.id_evaluacion.nombre}}</td>
        <td v-if="solicitud.estado == 'A'">Aprobada</td>
        <td v-else-if="solicitud.estado == 'R'" >Rechazado</td>
        <td v-else >Pendiente</td>
        <td>{{solicitud.fecha_creacion}}</td>
        <td>{{solicitud.id_estudiante.id_usuario.first_name}} {{solicitud.id_estudiante.id_usuario.last_name}}</td>
        <td>{{solicitud.id_evaluacion.id_coordinacion.coordinacion}}-{{solicitud.id_evaluacion.id_coordinacion.seccion}}</td>
        <td> {{solicitud.id_docente.id_usuario.first_name}} {{solicitud.id_docente.id_usuario.last_name}}</td>
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
                            <div class="col-5">Estudiante solicitante</div>
                            <div class="col-5">{{solicitud.id_estudiante.id_usuario.username}}</div>
                        </div>
                        <div class="row">
                            <div class="col-5">Profesor responsable</div>
                            <div class="col-5">{{solicitud.id_docente.id_usuario.username}}</div>
                        </div>
                        <div class="row">
                            <div class="col-5">Estado</div>
                            <div class="col-5" v-if="solicitud.estado == 'A'" >Aprobada</div>
                            <div class="col-5" v-else-if="solicitud.estado == 'R'" >Rechazado</div>
                            <div class="col-5" v-else>Pendiente</div>
                        </div>
                        <div class="row">
                            <div class="col-5">Motivo</div>
                            <div class="col-5">{{solicitud.motivo}}</div>
                        </div>
                        <div class="row">
                            <div class="col-5">Fecha creacion</div>
                            <div class="col-5">{{solicitud.fecha_creacion}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado != 'P'">
                            <div class="col-5">Respuesta</div>
                            <div class="col-5">{{solicitud.respuesta}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado != 'P'">
                            <div class="col-5">Fecha Respuesta</div>
                            <div class="col-5">{{solicitud.fecha_respuesta}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado == 'P' || solicitud.estado == 'R'">
                            <div class="col-3">Nota actual</div>
                            <div class="col-3">{{solicitud.actual_nota}}</div>
                            <div class="col-3">Fecha Publicacion</div>
                            <div class="col-3">{{solicitud.id_calificacion.fecha_entrega}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado == 'A'">
                            <div class="col-3">Nota modificada</div>
                            <div class="col-3">{{solicitud.actual_nota}}</div>
                            <div class="col-3">Fecha publicacion</div>
                            <div class="col-3">{{solicitud.fecha_respuesta}}</div>
                        </div>
                        <div class="row" v-if="solicitud.estado == 'A'">
                            <div class="col-3">Nota anterior</div>
                            <div class="col-3">{{solicitud.anterior_nota}}</div>
                            <div class="col-3">Fecha publicacion</div>
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
        }
    },
    props:{
        solicitud: Array,
        coordinaciones: Array,
        secciones: Array,
        nombreEvaluacion: String,
        nombreDocente: String,
        aprobada: Boolean,
        rechazada: Boolean,
        pendiente: Boolean
    },
    methods:{
        filterSecciones(coordinacion,seccion){
        if(this.secciones.includes(seccion) && this.coordinaciones.includes(coordinacion)){
            return true
        }
        else{
            return false
        }
        },
        filterEvaluacion(evaluacion){
        let n = Array(evaluacion)
        return n[0].toLocaleLowerCase().indexOf(this.nombreEvaluacion.toLocaleLowerCase()) >= 0
        },
        filterDocente(nombre,apellido){
        let n = Array(nombre+' '+apellido)
        return n[0].indexOf(this.nombreDocente) >= 0
        },
        filterEstado(estado){
            if(estado == 'A'){
                return this.aprobada
            }
            else if(estado == 'R'){
                return this.rechazada
            }
            else if(estado == 'P'){
                return this.pendiente
            }
            else{
                return false
            }
        }
    }
}
</script>
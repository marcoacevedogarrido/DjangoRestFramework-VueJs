<template>
  <div class="edit">
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-left">
            <h4>Detalle de Documento</h4>
          </div>
        </div>
      <div class="row">
        <div class="col">
          <form>
            <b-container>

              <div class="container">
                <div class="row justify-content-center align-items-center">
                    <table class="table table-striped table-bordered table-hover text-center">
                        <thead class="thead-dark">
                            <tr>
                                <th>Nombre</th>
                                <th>Codigo</th>
                                <th>Precio</th>
                                <th>{{ }}</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(item, x) in procesos" v-bind:key="x">
                                <td>
                                  <span v-if="!item.editando">
                                    {{ item.producto_obj.nombre }}
                                  </span>
                                  <span v-if="item.editando">
                                    <b-form-input
                                    v-model="item.producto_obj.nombre"
                                    size="sm">
                                    </b-form-input>
                                  </span>
                                </td>
                                <td>
                                  <span v-if="!item.editando">
                                    {{ item.producto_obj.codigo }}
                                  </span>
                                  <span v-if="item.editando">
                                    <b-form-input
                                    v-model="tem.producto_obj.codigo"
                                    size="sm">
                                    </b-form-input>
                                  </span>
                                </td>
                                <td>
                                  <span v-if='!item.editando'>
                                   {{ item.producto_obj.precio }}
                                  </span>
                                  <span v-if='item.editando'>
                                    <b-form-input
                                    v-model="item.producto_obj.precio"
                                    size="sm">
                                    </b-form-input>
                                  </span>
                                </td>
                                <td>
                                  <b-button
                                    v-on:click='editar(item)'
                                    size='sm'
                                    squared
                                    variant='black'>
                                    <font-awesome-icon icon="pencil-alt" />
                                  </b-button>
                                  <b-button
                                    v-if='item.editando'
                                    v-on:click='save(item)'
                                    size='sm'
                                    squared
                                    variant='transparent'>
                                    <font-awesome-icon icon="check" style="color: black"/>
                                  </b-button>
                                  <b-button
                                    v-on:click='cancelar(item)'
                                    size='sm'
                                    squared
                                    variant='black'>
                                    <font-awesome-icon icon="times"/>
                                  </b-button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
              </div>
              <div class="rows">
                <div class="text-left">
                    <!--<b-button v-on:click='DeleteDocumento' size='sm'  variant="danger">
                      Eliminar
                    </b-button> -->
                    <b-button
                      size='sm'
                      variant="primary"
                      :to="{ name:'ListaCliente'}">
                      Volver
                    </b-button>
                </div>
              </div>
            </b-container>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
const Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  ifConfirmButton: false,
  timer: 2500,
  timerProgressBar: true,
  onOpen: (toast) => {
    toast.addEventListener('mouseenter', Swal.stopTimer)
    toast.addEventListener('mouseleave', Swal.resumeTimer)
  }
})
/* eslint-disable */

const Savepath = 'http://localhost:8000/api/documentos/?documento=${this.documentoId}/'

export default {
  components: {},
  data () {
    return {
      documentoId: this.$route.params.documentoId,
      item: {
         producto_obj: '',
         nombre: '',
         fecha_creacion: '',
         fecha_envio: ''
      },
      procesos: []
    }
  },
  methods: {
    getCliente () {
      const Getdocpath = `http://localhost:8000/api/documentos/?documentos=${this.documentoId}/`
      axios.get(Getdocpath).then((response) => {
        this.item = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    editar (item) {
      this.$set(item, 'editando', true)
    },
    cancelar (item) {
      this.$set(item, 'editando', false)
    },
    save (item) {
      axios.put(Savepath, item).then((response) => {
        this.item = response.data
        this.getCliente = response.data
        Toast.fire({
          icon: 'success',
          title: 'Cliente editado existosamente!'
        })
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getProceso () {
      const getprocesopath = `http://localhost:8000/api/procesos/?documento=${this.documentoId}`
      axios.get(getprocesopath).then((response) => {
        this.procesos = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.getCliente()
    this.getProceso()
  }
}
</script>

<style lang='css' scoped>
.detalle {
  margin-bottom: 3%;
}
table {
  background-color: #fff;
}
th {
  background-color: #1E376D;
  color: rgba(255,255,255,0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.table td {
  padding-top: 8px !important;
  padding-bottom: 8px !important;
}
.table-bordered th, .table-bordered td {
  border-color: #F3F3F3;
}

.table {
  margin-bottom: 2%;
}
.botonenvio {
  padding-bottom: 1%;
}
.total {
  margin-top: -2%;
}
.form-group {
  margin-bottom: -1.5%;
}
.table th {
  padding-top: 1%;
  padding-bottom: 1%;
}

.col-md-12 h4 {
  padding-top: 3% !important;
  padding-bottom: 3% !important;
}
.edit {
  padding-top: 0.1px !important;
  padding-bottom: 0.1px !important;
}
.my-4 {
  margin-top: 0.5rem !important;
}
.table th {
  padding-top: 2px !important;
  padding-bottom: 2px !important;
}
</style>

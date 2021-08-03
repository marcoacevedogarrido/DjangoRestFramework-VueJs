<template>
  <div class="edit">
    <NavBar></NavBar>
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-left">
            <h4>Detalle de Cliente</h4>
          </div>
        </div>
      <div class="row">
        <div class="col">
          <form>
            <b-container>
              <div class="detalle">
                <div class="form-group row text-left">
                  <label
                    for="id"
                    class="col-sm-6 col-form-label">
                    <strong>
                      Id
                    </strong> : {{ item.id }}
                  </label>
                </div>
                <div class="form-group row text-left">
                  <label
                    for="nombre"
                    class="col-sm-6 col-form-label">
                    <strong>
                      Nombre
                    </strong> : {{ item.nombre }}
                  </label>
                </div>
                <div class="form-group row text-left">
                  <label
                    for="razon_social"
                    class="col-sm-6 col-form-label">
                    <strong>
                      Razon social
                    </strong> : {{ item.razon_social }}
                  </label>
                </div>
                <div class="form-group row text-left">
                  <label
                    for="rut"
                    class="col-sm-6 col-form-label">
                    <strong>
                      Rut
                    </strong> : $ {{ item.rut }}
                  </label>
                </div>
              </div>
              <div class="botonenvio text-right">
                <template>
                  <b-button
                  v-if='!item.fecha_envio'
                  size='sm'
                  variant="primary"
                  :to="{ name:'' }">
                    Enviar Documento
                  </b-button>
                </template>
              </div>
              <div class="container">
                <div class="row justify-content-center align-items-center">
                    <table class="table table-striped table-bordered table-hover text-center">
                        <thead class="thead-dark">
                            <tr>
                                <th>id</th>
                                <th>Nombre</th>
                                <th>Razon Social</th>
                                <th>rut</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(item, x) in lineas" v-bind:key="x">
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
                                    {{ item.cantidad }}
                                  </span>
                                  <span v-if="item.editando">
                                    <b-form-input
                                    v-model="item.cantidad"
                                    size="sm">
                                    </b-form-input>
                                  </span>
                                </td>
                                <td>
                                  <span v-if='!item.editando'>
                                   {{ formato_totales(item.producto_obj.precio) }}
                                  </span>
                                  <span v-if='item.editando'>
                                    <b-form-input
                                    v-model='item.producto_obj.precio'
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
              <div class="total" v-if='item.lineas'>
                <div class="form-group row text-right">
                  <label class="col-sm-11 col-form-label">
                    <strong>
                      Total
                    </strong> : $ {{ formato_totales(item.lineas[0].precio_total_linea) }}
                  </label>
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
                      :to="{ name:'ListarDocumento' }">
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
const Getdocpath = 'http://localhost:8000/api/clientes/?clientes=${this.clienteId}/'
const Savepath = 'http://localhost:8000/api/clientes/?cliente=${this.clienteId}/'
export default {
  components: {},
  data () {
    return {
      clienteId: this.$route.params.clienteId,
      item: {
         razon_social: '',
         fecha_creacion: '',
         rut: ''
      },
      clientes: []
    }
  },
  methods: {
    getCliente () {
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
    getLinea () {
      const getclientepath = `http://localhost:8000/api/lineas/?cliente=${this.ClienteId}`
      axios.get(getclientepath).then((response) => {
        this.clientes = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    formato_totales (cantidad, decimales) {
    cantidad += ''
    cantidad = parseFloat(cantidad.replace(/[^0-9.]/g, ''))
    decimales = decimales || 0
    if (isNaN(cantidad) || cantidad === 0) {
        return parseFloat(0).toFixed(decimales)
      }
      cantidad = '' + cantidad.toFixed(decimales)
    var cantidadpartes = cantidad.split('.')
    var regexp = /(\d+)(\d{3})/
    while (regexp.test(cantidadpartes[0])) {
      cantidadpartes[0] = cantidadpartes[0].replace(regexp, '$1' + ',' + '$2')
      }
      return cantidadpartes.join('.')
    }
  },
  created () {
    this.getCliente()
    this.getLinea()
  }
}
</script>

<style lang='css' scoped>
.detalle {
  margin-bottom: 3%;
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
.table td {
  padding-top: 8px !important;
  padding-bottom: 8px !important;
}
.table-bordered th, .table-bordered td {
  border-color: #F3F3F3;
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

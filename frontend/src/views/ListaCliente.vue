<template>
  <div class="lista">
    <div class="container">
      <div class='row'>
        <div class="col-md-12 text-left">
          <h4>Listado de Clientes</h4>
        </div>
          <div class="col-sm-12 text-center">
            <div class="container">
              <paginate name="clientes" :list="clientes" :per="5">
              <div class="row justify-content-center align-items-center">
                <table id='Table' class="table table-striped table-bordered table-hover text-center">
                    <thead class="thead-dark">
                      <tr>
                        <th>Id</th>
                        <th>Nombre</th>
                        <th>Razon Social</th>
                        <th>Rut</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, x) in paginated('clientes')" v-bind:key="x">
                        <td>
                          <router-link :to="{path: item.id.toString()}">
                            {{ item.id }}
                          </router-link>
                        </td>
                        <td>
                          {{ item.nombre }}
                        </td>
                        <td>
                          {{ item.razon_social }}
                        </td>
                        <td>
                          {{ item.rut }}
                        </td>
                      </tr>
                    </tbody>
                </table>
              </div>
            </paginate>
            </div>
          </div>
        </b-container>
      </div>
    </div>

  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

const Listarpath = 'http://localhost:8000/api/clientes/'
export default {
  components: {},
  data () {
    return {
      paginate:['clientes'],
      id: '',
      nombre:'',
      razon_social:'',
      rut:'',
      clientes: []
    }
  },
  methods: {
    getCliente () {
      axios.get(Listarpath).then((response) => {
        this.clientes = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.getCliente()
  }
}
</script>

<style lang='css' scoped>
table {
  border: 2px solid #1E376D;
  background-color: #fff;
}

.botoningreso {
  height: 40px;
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
.col-md-12 h4 {
  padding-top: 3% !important;
  padding-bottom: 3% !important;
}
.lista {
  padding-top: 0.1px !important;
  padding-bottom: 0.1px !important;
}
table th[data-v-c8477b52] {
  padding-top: 2px !important;
  padding-bottom: 2px !important;
}
.my-4 {
  margin-top: 0.5rem !important;
}

</style>

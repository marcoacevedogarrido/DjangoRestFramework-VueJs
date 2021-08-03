import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/Login.vue'
import ListaCliente from '@/views/ListaCliente.vue'
import EditarCliente from '@/views/EditarCliente.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/listacliente',
      name: 'ListaCliente',
      component: ListaCliente,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/:clienteId',
      name: 'EditarCliente',
      component: EditarCliente,
      meta: {
        requiresAuth: true
      }
    },
  ]
})

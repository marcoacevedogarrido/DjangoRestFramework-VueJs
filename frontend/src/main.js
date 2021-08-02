/* eslint-disable */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import IdleVue from 'idle-vue'
import BootstrapVue from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus, faPencilAlt, faTimes, faCheck } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VuePaginate from 'vue-paginate'

library.add(faPlus, faPencilAlt, faTimes, faCheck)

const eventsHub = new Vue()

Vue.use(VuePaginate);
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(BootstrapVue)
Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 720000
})
Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  }
  else if (to.matched.some(record => record.meta.requiresLogged)) {
    if (store.getters.loggedIn) {
      next({ name: 'home' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

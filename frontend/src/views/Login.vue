<template>
  <div class='container'>
    <div class="row">
      <div class="col">
        <div class="login-form">
          <div class='lg'>
            <div class="row">
              <div class="col-md-12 text-center">
                <h4>Login Usuario</h4>
              </div>
            </div>
            <form v-on:submit.prevent="loginUser">
              <small id="emailHelp" class="form-text text-muted">Ingrese solamente numeros y letras.</small>
              <input type="text" class='form-control form-control-sm' name="username" v-model="username" placeholder="Username" autocomplete="current-username" aria-describedby="emailHelp">
              <small id="passwordHelp" class="form-text text-muted">Password debe tener al menos 4 digitos.</small>
              <input type="password" class='form-control form-control-sm' name="password" v-model="password" placeholder="Password" aria-describedby="passwordHelp">
              <button class="btn btn-primary btn-sm btn-block" square type="submit">Ingresar</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
const Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  showConfirmButton: false,
  timer: 2500,
  timerProgressBar: true,
  onOpen: (toast) => {
    toast.addEventListener('mouseenter', Swal.stopTimer)
    toast.addEventListener('mouseleave', Swal.resumeTimer)
  }
})
export default {
  name: 'login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    loginUser () { // call loginUSer action
      this.$store.dispatch('loginUser', {
        username: this.username,
        password: this.password
      }).then(() => {
          this.$router.push({ name: '7' })
        }).catch(e => {
          Toast.fire({
            icon: 'error',
            title: 'Credenciales invalidas!'
          })
        })
      }
    }
  }
</script>

<style scoped>
.lg {
 background-color: white;
 padding: 20px;
 box-shadow: 1px 0 4px 4px rgba(0, 0, 0, 0.17);
 text-decoration: none;
 width: 500px;
 height: 270px;
 margin: auto auto;
}
input {
  margin-bottom: 2%;
}
.btn-primary {
  background-color: #1E376D;
  border-color: #1E376D;
  margin-top: 4%;
}
.container {
  margin-top: 10%;
}
form {
  margin-top: 7%;
}
form small {
  text-align: left;
}
.col-md-12 h4 {
  margin-bottom: 1%;
}
</style>

<template>
  <div class="container">
    <h1 class="title">LOGIN</h1>
    <form action="" class="form-group" @submit.prevent="login">
      <label for="email">Email:</label>
      <input class="form-control" type="email" id="email" v-model="email" required/>
      <label for="password">Password:</label>
      <input class="form-control" type="password" id="password" v-model="password" required>
      <hr v-if="error">
      <div v-if="error" class="alert alert-danger" role="alert">Email or Password wrong!</div>
      <hr/>
      <input class="btn btn-primary" type="submit" value="Login">
      
    </form>
     <p class="msg">¿No tienes cuenta?
      <router-link to="/register">Regístrate</router-link>
    </p>
  </div>
</template>

<script>
import auth from '@/libs/auth'

export default {
  data: () => ({
    email: "",
    password: "",
    error: false,
  }),
  methods: {
    async login() {
      try{
        await auth.login(this.email, this.password)
        auth.setUserLogged({
          email:this.email
        })
        this.$router.push('/')
      }catch(error){
        this.error = true
      }
    }
  }
}
</script>
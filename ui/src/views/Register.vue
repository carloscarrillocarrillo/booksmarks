<template>
  <div class="container">
    <h1 class="title">Register</h1>
    <form action="" class="form-group" @submit.prevent="register">
      <label for="email">Email:</label>
      <input class="form-control" type="email" id="email" v-model="email" required/>
      <label for="password">Password:</label>
      <input class="form-control" type="password" id="password" v-model="password" required>
      <label for="password">Confirm password:</label>
      <input class="form-control" type="password" id="confirm_password" v-model="confirm" required>
      
      <hr/>
      <input class="btn btn-primary" type="submit" value="Register">
    </form>
  </div>
</template>

<script>
import auth from '@/libs/auth'

export default {
  data: () => ({
    email: "",
    password: "",
    confirm: "",
    error: false
  }),
  methods: {
    async register() {
      try{
        await auth.register(this.email, this.password)
        this.$router.push('/')
      } catch (error){
        console.log(error)
      }
    }
  }
}
</script>
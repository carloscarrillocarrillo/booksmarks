<template>
  <div class="home">
    <p v-if="user">User loggued: {{user}}</p>
    <HelloWorld msg="Welcome to Booksmarks App"/>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import auth from '@/libs/auth'
export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  computed: {
    user() {
      return auth.getUserLogged()
    }
  }
}
</script>

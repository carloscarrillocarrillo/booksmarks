<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/login">Login</router-link> | 
      <router-link to="/register">Register</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1a2229;
}

#nav {
  padding: 30px;

  a {
    font-weight: normal;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #5284f0;
    }
  }
}
</style>

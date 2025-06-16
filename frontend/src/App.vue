<template>
  <img alt="Vue logo" src="./assets/logo.png" style="width: 80px; margin: auto; display: block;">
  <InventoryManager />
</template>

<script>
import InventoryManager from './components/InventoryManager.vue'

export default {
  name: 'App',
  components: {
    InventoryManager
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
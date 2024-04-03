<script setup lang="ts">
import FileProcessing from './components/FileProcessing.vue';

</script>

<template>
  <h1>ML DEMO</h1>
  <div class="all">
    <FileProcessing />
  </div>
</template>

<style scoped>
h1 {
  text-align: center;
}
.all {
  display: grid;
  grid-template-columns: 50% 50%;
  grid-gap: 10px;
  justify-content: center;
}

.all::after {
  content: "";
  display: block;
  width: 1px;
  height: 100%;
  background-color: black;
  margin: 0 10px;
  z-index: 1;
}
</style>

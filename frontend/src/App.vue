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
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>

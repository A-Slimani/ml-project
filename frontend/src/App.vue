<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const fileInput = ref()

console.log(fileInput)

const handleFileUpload = () => {
  const file = fileInput.value.files[0];
  console.log(file)
  const formData = new FormData();
  formData.append("file", file);

  axios
    .post("/file_upload", formData)
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.error(error);
    });
};

</script>

<template>
  <div class="main">
    <h1>ML DEMO</h1>
    <label for="ml-file">Choose a file to be processed: </label>
    <input @change="handleFileUpload" ref="fileInput" type="file" id="ml-file" name="ml-file" accept=".csv, application/vnd.ms-excel, text/csv"/>
  </div>
</template>

<style scoped>
.main {
  text-align: center;
}
</style>

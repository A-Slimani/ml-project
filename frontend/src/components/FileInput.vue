<script setup lang="ts">
import { ref } from "vue";
import axios from 'axios';

const fileInput = ref()
const objectName = ref()

function handleFileUpload() {
  const file = fileInput.value.files[0];
  const name = objectName.value.value;
  const formData = new FormData();
  formData.append("file", file);
  formData.append("text", name);

  axios.post("/file_upload", formData,
  ).then(res => {
    console.log(res);
  }).catch(err => {
    console.log(err);
  })
};
</script>

<template>
  <form @submit.prevent="handleFileUpload">
    <label class="form-item" for="ml-file">Choose file to be processed: </label>
    <input class="form-item" ref="fileInput" type="file" id="ml-file" name="ml-file"
      accept=".csv, application/vnd.ms-excel, text/csv" />
    <label class="form-item" for="object-name">Object name (to be created): </label>
    <input class="form-item" ref="objectName" type="text" id="object-name" name="object-name"/>
    <input class="form-item" type="submit" value="Submit" />
  </form>
</template>

<style scoped>
  input[type="file"] {
    padding-left: 80px;
  }

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .form-item {
    margin-bottom: 10px;
  }
</style>
<script setup lang="ts">
import ListBox from 'primevue/listbox'
import { onMounted, ref } from "vue";
import axios from 'axios';

const fileInput = ref()
const objectName = ref()
const fileList = ref([])
const selectedFile = ref()

function handleFileAndObjectUpload() {
  const file = fileInput.value.files[0];
  const name = objectName.value.value;
  const formData = new FormData();
  formData.append("file", file);
  formData.append("text", name);

  axios.post("/api/file_and_object_upload", formData,
  ).then(res => {
    // change this to be stored in a logger
    console.log(res);
  }).catch(err => {
    console.log(err);
  })
};

function handleFileUpload() {
  const file = fileInput.value.files[0]
  const formData = new FormData()
  formData.append("file", file)
  axios.post('/api/file_upload', formData)
    .then(res => {
      // TODO: store these in a logger 
      console.log(res);
    }).catch(err => {
      console.log(err);
    })
}

function getFileList() {
  axios.get('/api/get_files').then(res => {
    fileList.value = res.data;
  })
};

onMounted(() => {
  getFileList()
});

</script>

<template>
  <div>
    <label class="form-item" for="ml-file">Choose file to be processed: </label>
    <Listbox v-model="selectedFile" :options="fileList" class="w-full md:w-14rem" />
    <FileUpload mode="basic" url="/api/file_upload" accept=".csv, application/vnd.ms-excel, text/csv"
      @upload="handleFileUpload" :auto="true" chooseLabel="Browse" />
  </div>
</template>

<style scoped>
div {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-item {
  margin-bottom: 10px;
}
</style>
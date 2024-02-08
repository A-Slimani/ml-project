<script setup lang="ts">
import { onMounted, ref, watch } from "vue";
import axios from 'axios';

const fileInput = ref() // TODO: file the type for this "file"
const fileList = ref<string[]>([])
const selectedFile = ref<string>()
const selectedMLMethod = ref<string>()
const MLOptions = ref<string[]>(['Regression', 'Classification'])
const selectedFileColumns = ref<string[]>()
const targetColumn = ref<string>()
const rowsRemoved = ref<number>()

function getFileList() {
  axios.get('/api/get_files').then(res => {
    fileList.value = res.data;
  })
};

function getFileContent() {
  axios.get(`/api/get_file_columns/${selectedFile.value}`).then(res => {
    selectedFileColumns.value = res.data;
  })
};

function handleFileUpload() {
  getFileList()

  const file = fileInput.value.files[0]
  const formData = new FormData()
  formData.append("file", file)
  formData.append("enctype", "multipart/form-data")
  axios.post('/api/file_upload', formData)
    .then(res => {
      // TODO: store these in a logger 
      console.log(res);
    }).catch(err => {
      console.log(err);
    })
}

function handlePreprocessing() {
  // upload the target column, selected file and selected ML method 
  if (targetColumn.value) {
    axios.post('/api/pre_processing', {
      file: selectedFile.value,
      target_column: targetColumn.value.replace(/\n/g, ''),
      method: selectedMLMethod.value
    }).then(res => {
      rowsRemoved.value = res.data
      // store the console logs in a logger
      console.log(res);
    }).catch(err => {
      console.log(err);
    })
  }
}

function handleMLProcessing() {
  axios.get('/api/run_ml_processing')
    .then(res => {
      console.log(res);
    }).catch(err => {
      console.log(err);
    })
}

watch(selectedFile, () => {
  if (selectedFile.value) {
    getFileContent()
  } else {
    selectedFileColumns.value = []
  }
})

onMounted(() => {
  getFileList()
});

</script>

<template>
  <div class="main">
    <p>Choose file to be processed: </p>
    <div class="upload-items">
      <Listbox v-model="selectedFile" :options="fileList" class="w-full md:w-14rem" />
      <h3> OR </h3>
      <FileUpload mode="basic" url="/api/file_upload" accept=".csv, application/vnd.ms-excel, text/csv"
        @upload="handleFileUpload" :auto="true" chooseLabel="Browse" />
    </div>
    <p>Choose method of machine learning</p>
    <SelectButton v-model="selectedMLMethod" :options="MLOptions" ariaLabelledby="basic" :disabled="!selectedFile"
      class="w-full md:w-14rem" />
    <p>Choose target column to be processed</p>
    <Listbox v-model="targetColumn" :options="selectedFileColumns" class="w-full md:w-14rem"
      listStyle="max-height:250px" />
    <p> Provide other options for preprocessing later here</p>
    <Button label="Submit for preprocessing" @click='handlePreprocessing'
      :disabled="!selectedMLMethod || !targetColumn || !selectedFile" />
    <p v-if="rowsRemoved">Preprocessing complete. Rows removed: {{ rowsRemoved }}</p>
    <Button v-if="selectedMLMethod" v-bind:label="'Run ' + selectedMLMethod" @click="handleMLProcessing"/>
  </div>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin: 10px;
}

.upload-items {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  margin: 10px;
}
</style>
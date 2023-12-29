<script setup lang="ts">
import { ref } from "vue";
import axios from 'axios';

const fileInput = ref()

function handleFileUpload() {
    const file = fileInput.value.files[0];
    const formData = new FormData();
    formData.append("file", file);

    axios.post("/file_upload", formData, {
        headers: {
            "Content-Type": "multipart/form-data"
        }
    }).then(res => {
        console.log(res);
    }).catch(err => {
        console.log(err);
    })
};
</script>

<template>
    <label for="ml-file">Choose file to be processed: </label>
    <input @change="handleFileUpload" ref="fileInput" type="file" id="ml-file" name="ml-file" accept=".csv, application/vnd.ms-excel, text/csv" />
</template>
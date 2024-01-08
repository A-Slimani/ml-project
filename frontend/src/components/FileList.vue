<script setup lang="ts">
import { onMounted, ref } from 'vue'
import axios from 'axios'

const fileList = ref([])

function getFileList() {
  axios.get('/api/get_files').then(res => {
    fileList.value = res.data
  })
}

onMounted(() => {
  getFileList()
})
</script>

<template>
  <div>
    <ul v-for="(file, index) in fileList" :key="index">
      {{ file }}
    </ul>
  </div>
</template>
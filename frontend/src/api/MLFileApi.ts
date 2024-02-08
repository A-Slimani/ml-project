import axios from 'axios'
import { ref } from 'vue'


export const getFileList = async () => {
  axios
    .get('/api/get_files')
    .then(res => {
      return res.data
    })
    .catch(err => {
      console.log(err)
    })
}

export const getFileContent = async () => {
  axios
    .get('/api/get_file_content')
    .then(res => {
      return res.data
    })
    .catch(err => {
      console.log(err)
    })
}

export const handleFileUpload = async (fileInput: any) => {
  getFileList()
  const file = fileInput.value.files[0]
  const formData = new FormData()
  formData.append('file', file)
  formData.append('enctype', 'multipart/form-data')
  axios
    .post('/api/file_upload', formData)
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
}

export const handlePreprocessing = async (targetColumn: string, file: string, method: string) => {
  if (targetColumn) {
    axios
      .post('/api/preprocessing', {
        targetColumn,
        file,
        method
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  }
}

export const handleMLProcessing = async () => {
  axios
    .get('/api/run_ml_processing')
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
}



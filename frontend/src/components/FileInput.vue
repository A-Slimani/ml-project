<script lang="ts">
import { ref } from "vue";
import axios from 'axios';

const fileInput = ref()

function handleFileUpload() {
    const file = fileInput.value.files[0];
    const formData = new FormData();
    formData.append("file", file);

    axios.post("/upload", formData, {
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
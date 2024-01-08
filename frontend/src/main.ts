import 'primevue/resources/themes/lara-light-cyan/theme.css'
import PrimeVue from 'primevue/config'
import { createApp } from 'vue'
import App from './App.vue'
import Listbox from 'primevue/listbox'
import FileUpload from 'primevue/fileupload'
import Dropdown from 'primevue/dropdown'

const app = createApp(App);
app.use(PrimeVue);
app.component('Listbox', Listbox);
app.component('FileUpload', FileUpload)
app.component('Dropdown', Dropdown)
app.mount('#app');
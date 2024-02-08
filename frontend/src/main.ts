import 'primevue/resources/themes/lara-dark-teal/theme.css'
import PrimeVue from 'primevue/config'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import Listbox from 'primevue/listbox'
import FileUpload from 'primevue/fileupload'
import Dropdown from 'primevue/dropdown'
import SelectButton from 'primevue/selectbutton'
import Button from 'primevue/button'

const pinia = createPinia();
const app = createApp(App);
app.use(pinia)
app.use(PrimeVue);
app.component('Listbox', Listbox);
app.component('FileUpload', FileUpload)
app.component('Dropdown', Dropdown)
app.component('SelectButton', SelectButton)
app.component('Button', Button)
app.mount('#app');
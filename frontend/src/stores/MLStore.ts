import { defineStore } from 'pinia'
import { ref } from 'vue'

export const usePreProcessStore = defineStore('preProcess', {
    state: () => ({
        preProcessSuccess: ref<boolean>(false)
    }),
    actions: {
        setPreProcessSuccess(value: boolean) {
            this.preProcessSuccess = value
        }
    }
})

export const useMLSetupStore = defineStore('mlSetup', {
    state: () => ({
        mlSetupSuccess: ref<string>()
    })
})

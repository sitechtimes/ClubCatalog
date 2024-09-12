import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useLoginInfo = defineStore('loginInfo', () => {
    const login = ref(null)

    return { login }
})


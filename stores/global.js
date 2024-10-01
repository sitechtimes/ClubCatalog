import { defineStore } from 'pinia';

export const useGlobalStore = defineStore('global', {
    state: () => ({
        search: '',
    }),

    actions: {
        setSearch(value) {
            this.search = value
        }
    }
})
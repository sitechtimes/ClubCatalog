import { defineStore } from 'pinia';

export const useGlobalStore = defineStore('global', {
    state: () => ({
        searchStore: '',
        selectedCategories: [],
        selectedDays: [],
        meetingFrequencies: [],
        isMenuOpen: false
    }),
})
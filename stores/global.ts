import { defineStore } from "pinia";

interface GlobalState {
  searchStore: string;
  selectedCategories: string[];
  selectedDays: string[];
  meetingFrequencies: string[];
  isMenuOpen: boolean;
}

export const useGlobalStore = defineStore("global", {
  state: (): GlobalState => ({
    searchStore: "",
    selectedCategories: [],
    selectedDays: [],
    meetingFrequencies: [],
    isMenuOpen: false,
  }),
});

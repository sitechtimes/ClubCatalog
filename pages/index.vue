<script setup>
import clubs from "../public/data.json";
import { Tags, Calendar, RefreshCw, Search, Menu } from "lucide-vue-next";
import { ref, computed } from "vue";
import { useGlobalStore } from "~/stores/global";

const clubSearch = ref("");
const selectedCategories = ref([]);
const selectedDays = ref([]);
const meetingFrequencies = ref([]);
const store = useGlobalStore();
const filterDiv = ref();
const isMenuOpen = ref(false);

onMounted(() => {
  const savedSearch = store.searchStore;
  const savedCategories = store.selectedCategories;
  const savedDays = store.selectedDays;
  const savedMeetingFrequencies = store.meetingFrequencies;
  const savedIsMenuOpen = store.isMenuOpen;
  //console.log(savedSearch)
  if (savedSearch) {
    clubSearch.value = savedSearch;
  }
  if (savedCategories) {
    selectedCategories.value = savedCategories;
  }
  if (savedDays) {
    selectedDays.value = savedDays;
  }
  if (savedMeetingFrequencies) {
    meetingFrequencies.value = savedMeetingFrequencies;
  }
  if (savedIsMenuOpen) {
    isMenuOpen.value = savedIsMenuOpen;
  }
});

watch(clubSearch, (newSearchValue) => {
  store.searchStore = newSearchValue;
});

watch(selectedCategories, (newCategories) => {
  store.selectedCategories = newCategories;
});

watch(selectedDays, (newDays) => {
  store.selectedDays = newDays;
});

watch(meetingFrequencies, (newMeetingFrequencies) => {
  store.meetingFrequencies = newMeetingFrequencies;
});

watch(isMenuOpen, (newIsMenuOpen) => {
  store.isMenuOpen = newIsMenuOpen;
});

function toggleMeetingFrequency(meetingFrequency) {
  if (meetingFrequencies.value.includes(meetingFrequency)) {
    meetingFrequencies.value = meetingFrequencies.value.filter(
      (mf) => mf !== meetingFrequency
    );
  } else {
    meetingFrequencies.value.push(meetingFrequency);
  }
}

function toggleDay(day) {
  if (selectedDays.value.includes(day)) {
    selectedDays.value = selectedDays.value.filter((d) => d !== day);
  } else {
    selectedDays.value.push(day);
  }
}

function toggleCategory(category) {
  if (selectedCategories.value.includes(category)) {
    selectedCategories.value = selectedCategories.value.filter(
      (cat) => cat !== category
    );
  } else {
    selectedCategories.value.push(category);
  }
}

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value;
}
</script>

<template>
  <div class="p-4 flex flex-col lg:flex-row gap-6">
    <div class="w-full mb-4 lg:hidden flex flex-row items-center gap-3">
        <button
        class="text-gray-600 hover:text-gray-900 flex flex-col items-center"
        @click="toggleMenu"
      >
        <Menu size="1.75em" id="menu" />
        <input id="menu" class="sr-only">
        <label for="menu" class="font-semibold cursor-pointer">Filters</label>
      </button>
      <div class="relative w-full">
        <label for="clubSearch2" class="sr-only">Search for clubs</label>
        <input
          id="clubSearch2"
          placeholder="Search for clubs"
          class="border border-gray-300 pl-10 py-2 pr-14 rounded-lg w-full text-gray-600"
          v-model="clubSearch"
          type="text"
        />
        <div class="absolute inset-y-0 left-3 flex items-center pointer-events-none">
          <i class="text-gray-500">
            <Search size="1.25em" />
          </i>
        </div>
      </div>
    </div>
    <!-- Sidebar for search and filters -->
    <div
      :class="{
        'hidden lg:block': !isMenuOpen,
      }"
      class="bg-gray-100 p-4 rounded-lg w-full lg:w-1/4"
    >
      <label for="clubSearch" class="sr-only">Search for clubs</label>
      <div class="relative w-full hidden lg:block">
        <input
          id="clubSearch"
          placeholder="Search for clubs"
          class="border border-gray-300 pl-10 py-2 pr-14 rounded-lg w-full text-gray-600"
          v-model="clubSearch"
          type="text"
        />
        <div class="absolute inset-y-0 left-3 flex items-center pointer-events-none">
          <i class="text-gray-500">
            <Search size="1.25em" />
          </i>
        </div>
      </div>
      <div class="mt-3">
        <!-- Categories Filter -->
        <p class="flex gap-2 mb-4 font-semibold text-lg justify-center">
          <Tags /> Categories
        </p>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="category in [
              'STEM',
              'Music',
              'Cultural',
              'Arts & Crafts',
              'Academic/Intellectual',
              'Literary',
              'Special Interest/Hobbies',
              'Health',
              'Leadership',
              'Community Service',
            ]"
            :key="category"
            :class="{
              'bg-gray-200': !selectedCategories.includes(category),
              'bg-gray-500': selectedCategories.includes(category),
            }"
            class="rounded-lg py-1 px-4 cursor-pointer"
            @click="toggleCategory(category)"
          >
            {{ category }}
          </span>
        </div>
      </div>

      <div class="mt-5">
        <!-- Meeting Day Filter -->
        <p class="flex gap-2 mb-4 font-semibold text-lg justify-center">
          <Calendar /> Meeting Day
        </p>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']"
            class="rounded-lg py-1 px-4 cursor-pointer"
            :key="day"
            :class="{
              'bg-gray-200': !selectedDays.includes(day),
              'bg-gray-500': selectedDays.includes(day),
            }"
            @click="toggleDay(day)"
          >
            {{ day }}
          </span>
        </div>
      </div>

      <div class="mt-5">
        <!-- Meeting Frequency Filter -->
        <p class="flex gap-2 mb-4 font-semibold text-lg justify-center">
          <RefreshCw /> Meeting Frequency
        </p>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="frequency in [
              'Weekly',
              'Once a Month',
              'Twice a Month',
            ]"
            :key="frequency"
            class="rounded-lg py-1 px-4 cursor-pointer"
            :class="{
              'bg-gray-200': !meetingFrequencies.includes(frequency),
              'bg-gray-500': meetingFrequencies.includes(frequency),
            }"
            @click="toggleMeetingFrequency(frequency)"
          >
            {{ frequency }}
          </span>
        </div>
      </div>
    </div>
      <!--
      <div ref="filterDiv"></div>
      burger menu
      -->
      

    <!-- Club Catalog -->
    <main class="lg:w-2/3 w-full">
      <h4 class="font-semibold text-xl mb-4 text-center border-b border-gray-400">Catalog</h4>
      <div v-for="club in clubs" :key="club">
        <div
          class="flex items-center gap-6 mb-7"
          v-if="(clubSearch === '' || club['Club Name'].toLowerCase().includes(clubSearch.toLowerCase())) &&
          (selectedCategories.some(category => club['Category'].includes(category)) || selectedCategories.length === 0) &&
          (meetingFrequencies.some(frequency => club['Frequency'].includes(frequency)) || meetingFrequencies.length === 0) &&
          (selectedDays.some(day => club['Day'].includes(day)) || selectedDays.length === 0)"
        >
          <img
            class="rounded-full max-h-32 max-w-32"
            src="https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM="
            alt=""
          />
          <div class="flex flex-col justify-between w-full">
            <div class="flex flex-col gap-3">
              <h4 class="font-semibold text-lg">{{ club["Club Name"] }}</h4>
              <p class="text-sm">
                No club description is currently available
               <!-- club description will go here -->
              </p>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="category in club['Category']"
                  :key="category"
                  class="bg-gray-200 rounded-lg py-2 px-3 text-sm text-gray-600"
                >
                  {{ category }}
                </span>
              </div>
            </div>
            <NuxtLink
              :to="'/' + club['Club Name'].toLowerCase().replace(/\s/g, '')"
              class="btn"
            >
              View More
            </NuxtLink>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

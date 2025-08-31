<template>
  <div class="p-4 flex flex-col lg:flex-row gap-6">
    <div class="w-full mb-4 lg:hidden flex flex-row items-center gap-3">
      <button
        class="text-gray-600 hover:text-gray-900 flex flex-col items-center"
        @click="toggleMenu"
      >
        <Menu :size="28" id="menu" />
        <input id="menu" class="sr-only" />
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
        <div
          class="absolute inset-y-0 left-3 flex items-center pointer-events-none"
        >
          <i class="text-gray-500">
            <Search :size="20" />
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
        <div
          class="absolute inset-y-0 left-3 flex items-center pointer-events-none"
        >
          <i class="text-gray-500">
            <Search :size="20" />
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
            v-for="day in [
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
            ]"
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
            v-for="frequency in ['Weekly', 'Once a Month', 'Twice a Month']"
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
      <h1
        class="font-semibold text-xl mb-4 text-center border-b border-gray-400"
      >
        Catalog
      </h1>
      <div v-for="club in clubs" :key="club.club_name">
        <div
          class="flex items-center gap-6 mb-7"
          v-show="
            (clubSearch === '' ||
              club.club_name
                .toLowerCase()
                .includes(clubSearch.toLowerCase())) &&
            (selectedCategories.some((category) =>
              club.categories.includes(category)
            ) ||
              selectedCategories.length === 0) &&
            (meetingFrequencies.some((frequency) =>
              club.meeting_frequency.includes(frequency)
            ) ||
              meetingFrequencies.length === 0) &&
            (selectedDays.some((day) => club.meeting_day.includes(day)) ||
              selectedDays.length === 0)
          "
        >
          <img
            class="rounded-full h-32 w-40 bg-cover"
            :src="imageExists(club.club_name)"
            @error="
              (event) => {
                const target = event.target as HTMLImageElement;
                if (target) {
                  target.src = 'https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=';
                }
              }
            "
            alt="Club Logo"
          />
          <div class="flex flex-col justify-between w-full">
            <div class="flex flex-col gap-3">
              <h2 class="font-semibold text-lg">{{ club.club_name }}</h2>
              <p class="text-sm">
                {{
                  club.description
                    ? club.description.slice(0, 100) +
                      (club.description.length > 100 ? "..." : "")
                    : "No description available"
                }}
              </p>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="category in club.categories"
                  :key="category"
                  class="bg-gray-200 rounded-lg py-2 px-3 text-sm text-gray-600"
                >
                  {{ category }}
                </span>
              </div>
            </div>
            <NuxtLink
              :to="'/' + club.club_name.toLowerCase().replace(/\s/g, '')"
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

<script setup lang="ts">
import clubs from "../public/clubs.json";
import { Tags, Calendar, RefreshCw, Search, Menu } from "lucide-vue-next";
import { useGlobalStore } from "~/stores/global";
import type { Club } from "@/utils/utils";

const store = useGlobalStore();

const clubSearch = computed({
  get: () => store.searchStore || "",
  set: (value) => (store.searchStore = value),
});

const selectedCategories = computed({
  get: () => (store.selectedCategories || []) as string[],
  set: (value) => ((store as any).selectedCategories = value),
});

const selectedDays = computed({
  get: () => (store.selectedDays || []) as string[],
  set: (value) => ((store as any).selectedDays = value),
});

const meetingFrequencies = computed({
  get: () => (store.meetingFrequencies || []) as string[],
  set: (value) => ((store as any).meetingFrequencies = value),
});

const isMenuOpen = computed({
  get: () => store.isMenuOpen || false,
  set: (value) => (store.isMenuOpen = value),
});

function toggleMeetingFrequency(meetingFrequency: string) {
  if (meetingFrequencies.value.includes(meetingFrequency)) {
    meetingFrequencies.value = meetingFrequencies.value.filter(
      (mf) => mf !== meetingFrequency
    );
  } else {
    meetingFrequencies.value.push(meetingFrequency);
  }
}

function toggleDay(day: string) {
  if (selectedDays.value.includes(day)) {
    selectedDays.value = selectedDays.value.filter((d) => d !== day);
  } else {
    selectedDays.value.push(day);
  }
}

function toggleCategory(category: string) {
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

function imageExists(clubName: string) {
  const imagePath = `/logos/${clubName.toLowerCase().replace(/\s/g, "")}.png`;

  return imagePath;
}
</script>

<script setup>
import clubs from "../assets/data.json";
import { Tags, Calendar, RefreshCw, Search } from "lucide-vue-next";
import { ref, onMounted } from "vue";

const clubSearch = ref("");
const selectedCategories = ref([]);
const selectedDays = ref([]);
const meetingFrequencies = ref([]);

//create a ref with an actual link to all the filters
const filters = ref("FilterDiv");

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
onMounted(() => {
})
</script>

<template>
  <div class="p-4 flex flex-col lg:flex-row gap-6">
    <!-- Sidebar for search and filters -->
    <div class="lg:w-1/3 w-full">
      <div class="relative w-full">
        <input
          placeholder="Search for clubs"
          class="border border-gray-300 pl-10 py-2 pr-14 rounded-lg w-full text-gray-600"
          v-model="clubSearch"
        />
        <div class="absolute inset-y-0 left-3 flex items-center pointer-events-none">
          <i class="text-gray-500">
            <Search size="1.25em" />
          </i>
        </div>
      </div>
      <div class="mt-5">
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
              'Once a Week',
              'Once a Month',
              'Twice a Month',
              'First Week of the Month',
            ]"
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
      <div ref="FilterDiv">
      </div>
      

    <!-- Club Catalog -->
    <div class="lg:w-2/3 w-full">
      <h4 class="font-semibold text-xl mb-4 text-center border-b border-gray-400">Catalog</h4>
      <div v-for="club in clubs">
        <div
          class="flex items-center gap-6 mb-7"
          v-if="(clubSearch === '' || club['Club Name'].toLowerCase().includes(clubSearch.toLowerCase())) &&
          (selectedCategories.some(category => club['Category'].includes(category)) || selectedCategories.length === 0) &&
          (meetingFrequencies.some(frequency => club['Meeting Frequency'].includes(frequency)) || meetingFrequencies.length === 0)"
        >
          <img
            class="rounded-full h-32 w-32"
            src="https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM="
            alt=""
          />
          <div class="flex flex-col justify-between w-full">
            <div class="flex flex-col gap-3">
              <h4 class="font-semibold text-lg">{{ club["Club Name"] }}</h4>
              <p class="text-sm">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="category in club['Category']"
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
    </div>
  </div>
</template>

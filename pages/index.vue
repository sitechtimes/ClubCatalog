<script setup>
import Navbar from "../components/Navbar.vue";
import clubs from "../assets/data.json";
import { Tags, Calendar, RefreshCw, Search } from "lucide-vue-next";
</script>

<template>
  <Navbar />
  <Button></Button>
  <div class="flex flex-col items-center justify-center">
    <div class="flex justify-start items-start w-[1300px] gap-x-16 max-h-screen">
      <div class="flex sticky flex-col justify-start items-start gap-y-5 w-[400px]">
        <div class="relative">
          <input
            placeholder="Search for clubs"
            class="border border-[#CBD5E1] pl-10 py-2 pr-[56px] rounded-[6px] text-[#94A3B8] w-[400px]"
          />
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <i class="text-[#94A3B8]">
              <Search size="1.25em" />
            </i>
          </div>
        </div>
        <div class="flex flex-col justify-start items-start">
          <p class="flex gap-x-2 mb-4 font-semibold text-[16px] justify-center">
            <span><Tags /></span>Categories
          </p>
          <div class="flex flex-wrap gap-x-2 gap-y-2">
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
              class="bg-[#E5E7EB] rounded-[16px] py-px px-3 font-medium text-[16px] text-[#6B7280]"
            >
              {{ category }}
            </span>
          </div>
        </div>
        <div class="flex flex-col justify-start items-start">
          <p class="flex gap-x-2 mb-4 font-semibold text-[16px] justify-center">
            <span><Calendar /></span>Meeting Day
          </p>
          <div class="flex flex-wrap gap-x-2 gap-y-2">
            <span
              v-for="day in [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
              ]"
              class="bg-[#E5E7EB] rounded-[16px] py-px px-3 font-medium text-[16px] text-[#6B7280]"
            >
              {{ day }}
            </span>
          </div>
        </div>
        <div class="flex flex-col justify-start items-start">
          <p class="flex gap-x-2 mb-4 font-semibold text-[16px] justify-center">
            <span><RefreshCw /></span>Meeting Frequency
          </p>
          <div class="flex flex-wrap gap-x-2 gap-y-2">
            <span
              v-for="frequency in [
                'Once a Week',
                'Once a Month',
                'Twice a Month',
                'First Week of the Month',
              ]"
              class="bg-[#E5E7EB] rounded-[16px] py-px px-3 font-medium text-[16px] text-[#6B7280]"
            >
              {{ frequency }}
            </span>
          </div>
        </div>
      </div>
      <div class="flex flex-col w-[836px]">
        <h4 class="font-semibold text-[20px] mb-5">Catalog</h4>
        <div v-for="club in clubs" class="flex gap-x-6 mb-7">
          <img
            class="rounded-full h-[130px] w-[130px]"
            src="https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM="
            alt=""
          />
          <div class="flex flex-col gap-y-px justify-between py-3">
            <h4 class="font-semibold text-[20px]">{{ club["Club Name"] }}</h4>
            <p class="text-[14px]">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam.
            </p>
            <div class="flex gap-x-1 w-full pt-1">
              <span v-for="category in club['Category']" 
                class="bg-[#E5E7EB] rounded-[16px] py-px px-3 font-medium text-[16px] text-[#6B7280]"
              >
                {{ category }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ChevronLeft } from "lucide-vue-next"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import data from '@/public/data.json'
import { ref } from 'vue'

const route = useRoute()

const club = data.find(club => club["Club Name"].toLowerCase().replace(/\s/g, '') === route.params.name)

console.log(club)
let presidents = club["Club President(s)"].split(", ")

const coVnoco = ref(presidents.length > 1 ? "Co-Presidents" : "President")
</script>

<template>
  <div class="flex flex-col items-center mb-[-4rem]">
    <img 
      class="w-full h-64 object-cover rounded-lg" 
      src="https://t3.ftcdn.net/jpg/04/86/29/98/360_F_486299886_4aXrDh0LPy7BK4SUJvhCkKpnnExNDsLX.jpg" 
      alt="Club Banner"
    />
    <div class="relative -top-20 px-6 flex flex-col lg:flex-row items-center gap-6 w-full">
      <img 
        class="w-48 h-48 object-cover rounded-full shadow-md"
        src="https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg"
        alt="Club Logo"
      />
      <div class="flex flex-col lg:flex-row lg:items-center w-full">
        <h1 class="text-4xl font-semibold text-center lg:text-left lg:mr-4">{{ club["Club Name"] }}</h1>
        <sub class="text-gray-700 text-center lg:text-left text-lg">Room {{ club["Room"] }}</sub>
      </div>
    </div>
  </div>

  <div class="flex flex-col lg:flex-row justify-between px-6 py-4">
    <div class="flex items-start justify-center lg:hidden">
      <RouterLink to="/" class="btn">
        <ChevronLeft class="h-6 w-6" />
        Back to Club List
      </RouterLink>
    </div>
    <div class="w-full lg:w-1/2">
      <h3 class="text-lg font-semibold mb-2">About Us</h3>
      <p class="mb-4">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam.
      </p>
      <h3 class="text-lg font-semibold mb-2">Leaders</h3>
      <div class="flex flex-col gap-4">
        <div class="flex gap-4" v-for="president in presidents" :key="president">
          <Avatar>
            <AvatarImage src="https://github.com/radix-vue.png" alt="Avatar" />
            <AvatarFallback>CN</AvatarFallback>
          </Avatar>
          <div class="flex flex-col">
            <p class="font-semibold text-base">{{ president }}</p>
            <p class="text-sm text-gray-600">{{ coVnoco }}</p>
          </div>
        </div>
      </div>
      <h3 class="text-lg font-semibold mt-4 mb-2">Advisors</h3>
      <div class="flex items-center gap-4">
        <Avatar>
          <AvatarImage src="https://github.com/radix-vue.png" alt="Avatar" />
          <AvatarFallback>CN</AvatarFallback>
        </Avatar>
        <div class="flex flex-col">
          <p class="font-semibold text-base">{{ club["Club Advisor"] }}</p>
          <p class="text-sm text-gray-600">Advisor</p>
        </div>
      </div>
    </div>
    
    <div class="w-full lg:w-1/4">
      <h3 class="text-lg font-semibold mb-2">Events</h3>
      <div class="flex flex-col gap-4">
        <div class="flex items-center justify-between gap-4 border border-gray-300 rounded-lg p-4">
          <div class="flex flex-col items-center">
            <h2 class="text-lg font-semibold">TUE</h2>
            <h2 class="text-lg font-semibold">02/20</h2>
          </div>
          <div class="w-full">
            <h3 class="text-lg font-semibold">Meeting</h3>
            <p>After school | Room {{ club["Room"] }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="flex items-start justify-center hidden lg:flex">
      <RouterLink to="/" class="btn">
        <ChevronLeft class="h-6 w-6" />
        Back to Club List
      </RouterLink>
    </div>
  </div>
</template>

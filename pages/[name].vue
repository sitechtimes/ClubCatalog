<script setup>
import { ChevronLeft } from "lucide-vue-next"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import data from '@/public/data.json'
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()

let club = {
      "Club Name": "NA",
      "Club President(s)": "NA",
      "Start After SING": "NA",
      "Type": "NA",
      "Room": "NA",
      "Club Advisor": "NA",
      "Day": "NA",
      "Meeting Frequency": "NA",
      "Category": ["NA"]
  }

let presidents = []

let coVnoco = "Co-Presidents"


try {
  const clubData = data.find(club => club["Club Name"].toLowerCase().replace(/\s/g, '') === route.params.name)
  if (!clubData) throw new Error('Club not found'); 
  club = clubData;

  if (club["Club President(s)"] !== undefined) {
    const presidentsTemp = club["Club President(s)"].split(" & ");
    presidents = presidentsTemp;
    console.log(presidents);
    coVnoco = presidents.length > 1 ? "Co-Presidents" : "President";
  }
} catch (e) {
  useRouter().push('/404');
}
//console.log(club, club["Club Name"].toLowerCase().replace(/\s/g, ''))
</script>

<template>
  <div class="flex flex-col items-center mb-[-4rem]">
    <img 
      class="w-full h-64 object-cover rounded-lg" 
      src="https://t3.ftcdn.net/jpg/04/86/29/98/360_F_486299886_4aXrDh0LPy7BK4SUJvhCkKpnnExNDsLX.jpg" 
      alt="Club Banner"
    />
    <div class="relative -top-20 px-6 flex flex-col lg:flex-row items-center gap-6">
      <img 
        class="w-48 h-48 object-cover rounded-full shadow-md"
        src="https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg"
        alt="Club Logo"
      />
      <div class="lg:flex lg:flex-col lg:items-center lg:justify-center w-full lg:mt-12">
        <h1 class="text-4xl font-semibold text-center lg:text-left lg:mr-4">{{ club["Club Name"] }}</h1>
        <p class="text-gray-700 text-center lg:text-left flex sm:flex-row flex-col text-lg gap-3">
          <span>Room: <span class="font-semibold">{{ club["Room"] }}</span></span>
          <span>Meeting Day: <span class="font-semibold">{{ club["Day"] }}</span></span>
          <span>Meeting Frequency: <span class="font-semibold">{{ club["Meeting Frequency"] }}</span></span>
        </p>
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
        <!-- club description will go here -->
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
    <!-- Events
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
    -->
    <div class="items-start justify-center hidden lg:flex">
      <RouterLink to="/" class="btn">
        <ChevronLeft class="h-6 w-6" />
        Back to Club List
      </RouterLink>
    </div>
  </div>
</template>

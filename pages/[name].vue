<template>
  <div class="flex flex-col items-center mb-[-4rem]">
    <img
      class="w-full h-64 object-cover rounded-lg"
      src="https://t3.ftcdn.net/jpg/04/86/29/98/360_F_486299886_4aXrDh0LPy7BK4SUJvhCkKpnnExNDsLX.jpg"
      alt="Club Banner"
    />
    <div
      class="relative -top-20 px-6 flex flex-col lg:flex-row items-center gap-6"
    >
      <img
        class="w-48 h-48 object-cover rounded-full shadow-md"
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
      <div
        class="lg:flex lg:flex-col lg:items-center lg:justify-center w-full lg:mt-12"
      >
        <h1 class="text-4xl font-semibold text-center lg:text-left lg:mr-4">
          {{ club.club_name }}
        </h1>
        <p
          class="text-gray-700 text-center lg:text-left flex sm:flex-row flex-col text-lg gap-3"
        >
          <span
            >Room:
            <span class="font-semibold">{{ club.room_number }}</span></span
          >
          <span
            >Meeting Day:
            <span class="font-semibold">{{ club.meeting_day }}</span></span
          >
          <span
            >Meeting Frequency:
            <span class="font-semibold">{{
              club.meeting_frequency
            }}</span></span
          >
        </p>
      </div>
    </div>
  </div>

  <div class="flex flex-col lg:flex-row justify-between px-6">
    <RouterLink to="/" class="btn btn-secondary">
      <ChevronLeft class="h-6 w-6" />
      Back to Club List
    </RouterLink>
    <div class="w-full lg:w-1/2 pt-4">
      <h3 class="text-lg font-semibold mb-2">About Us</h3>
      <p class="mb-4">
        {{ club.description || "No description available" }}
      </p>
      <h3 class="text-lg font-semibold mb-2">Leaders</h3>
      <div class="flex flex-col gap-4">
        <div
          class="flex gap-4"
          v-for="president in presidents"
          :key="president"
        >
          <Avatar>
            <AvatarImage src="https://github.com/radix-vue.png" alt="Avatar" />
            <AvatarFallback>CN</AvatarFallback>
          </Avatar>
          <div class="flex flex-col">
            <p class="font-semibold text-base">{{ president }}</p>
            <p class="text-sm text-gray-600">{{ president_or_copresident }}</p>
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
          <p class="font-semibold text-base">{{ club.club_adviser }}</p>
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
      <RouterLink to="/" class="btn btn-secondary">
        <ChevronLeft class="h-6 w-6" />
        Back to Club List
      </RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ChevronLeft } from "lucide-vue-next";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import clubs from "@/public/clubs.json";
import { useRouter, useRoute } from "vue-router";
import type { Club } from "@/utils/utils";
import { createDefaultClub } from "@/utils/utils";

const route = useRoute();

let club: Club = createDefaultClub();

let presidents: string[] = [];

let president_or_copresident = "Co-Presidents";

try {
  const clubInfo = clubs.find(
    (club) =>
      club.club_name.toLowerCase().replace(/\s/g, "") === route.params.name
  );
  if (!clubInfo) throw new Error("Club not found");
  club = clubInfo;

  if (club.club_presidents !== undefined) {
    const presidentsTemp = club.club_presidents.split(" & ");
    presidents = presidentsTemp;
    //console.log(presidents);
    president_or_copresident =
      presidents.length > 1 ? "Co-President" : "President";
  }
} catch (e) {
  useRouter().push("/404");
}

function imageExists(clubName: string) {
  const imagePath = `/logos/${clubName.toLowerCase().replace(/\s/g, "")}.png`;

  return imagePath;
}
</script>

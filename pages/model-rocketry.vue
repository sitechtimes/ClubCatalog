<script setup>
import Navbar from "../components/Navbar.vue";
import { File, Instagram, ChevronRight  } from "lucide-vue-next";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
</script>

<template>
  <Navbar />
  <div>
    <img class="rounded-[6px] w-[1300px] h-[250px] object-cover" src="https://cdn.shopify.com/s/files/1/0568/7489/3503/files/privacy-policy.jpg?v=1621664345" />
    <div class="px-10 flex items-center">
      <img class="rounded-full h-[200px] w-[200px] object-cover" src="https://ventureasheville.com/wp-content/uploads/2015/09/logo-placeholder.jpg">
      <div class="flex">
        <h1 class="font-semibold text-[48px]">Model Rocketry</h1>
        <Button>Request to Join</Button>
      </div>
    </div>
  </div>
  <div class="flex justify-between">
  <div class="w-3/12">
    <h3 class="font-semibold text-[18px]">About Us</h3>
    <p class="mt-2 mb-3">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam.
    </p>
    <Dialog>
      <DialogTrigger class="flex gap-x-1 font-medium"><File /> Club Charter </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Club Charter</DialogTitle>
        </DialogHeader>
        <embed src="../public/Homerooms.pdf" />
      </DialogContent>
    </Dialog>
    <h3 class="font-semibold text-[18px] mt-3 mb-2">Leaders</h3>
    <div class="flex flex-col gap-y-2">
        <div class="flex gap-x-3">
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <div class="flex flex-col">
        <p class="font-semibold text-[14px]">John Doe</p>
        <p class="text-[14px] color-[#525252] mt-[-3px]">Co-President</p>
      </div>
    </div>
    <div class="flex gap-x-3">
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <div class="flex flex-col">
        <p class="font-semibold text-[14px]">John Doe</p>
        <p class="text-[14px] color-[#525252] mt-[-3px]">Co-President</p>
      </div>
    </div>
    </div>
    <h3 class="font-semibold text-[18px] mt-3 mb-2">Advisors</h3>
    <div class="flex gap-x-3">
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <div class="flex flex-col">
        <p class="font-semibold text-[14px]">John Doe</p>
        <p class="text-[14px] color-[#525252] mt-[-3px]">Co-President</p>
      </div>
    </div>
    <h3 class="font-semibold text-[18px] mt-3 mb-2">Members</h3>
    <div class="flex gap-x-1">
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <Avatar>
        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
      <Avatar>
        <AvatarFallback>10+</AvatarFallback>
      </Avatar>
    </div>
  </div>
  <div class="w-5/12">
    <h3 class="font-semibold text-[18px] mb-2">Events</h3>
    <div class="flex flex-col gap-4">
    <div class="flex justify-between items-center gap-x-7 w-full rounded-[12px] border border-[#E5E7Eb] px-4 py-3">
        <div class="flex flex-col items-center">
            <h2 class="font-semibold text-[18px]">TUE</h2>
            <h2 class="font-semibold text-[18px]">02/20</h2>
        </div>
        <div class="w-full">
            <h3 class="font-semibold text-[18px]">Meeting</h3>
            <p>After school  |  Room 259</p>
        </div>
        <ChevronRight/>
    </div>
    <div class="flex justify-between items-center gap-x-7 w-full rounded-[12px] border border-[#E5E7Eb] px-4 py-3">
        <div class="flex flex-col items-center">
            <h2 class="font-semibold text-[18px]">TUE</h2>
            <h2 class="font-semibold text-[18px]">02/20</h2>
        </div>
        <div class="w-full">
            <h3 class="font-semibold text-[18px]">Meeting</h3>
            <p>After school  |  Room 259</p>
        </div>
        <ChevronRight/>
    </div>
    <div class="flex justify-between items-center gap-x-7 w-full rounded-[12px] border border-[#E5E7Eb] px-4 py-3">
        <div class="flex flex-col items-center">
            <h2 class="font-semibold text-[18px]">TUE</h2>
            <h2 class="font-semibold text-[18px]">02/20</h2>
        </div>
        <div class="w-full">
            <h3 class="font-semibold text-[18px]">Meeting</h3>
            <p>After school  |  Room 259</p>
        </div>
        <ChevronRight/>
    </div>
    <div class="flex justify-between items-center gap-x-7 w-full rounded-[12px] border border-[#E5E7Eb] px-4 py-3">
        <div class="flex flex-col items-center">
            <h2 class="font-semibold text-[18px]">TUE</h2>
            <h2 class="font-semibold text-[18px]">02/20</h2>
        </div>
        <div class="w-full">
            <h3 class="font-semibold text-[18px]">Meeting</h3>
            <p>After school  |  Room 259</p>
        </div>
        <ChevronRight/>
    </div>
    <div class="flex justify-between items-center gap-x-7 w-full rounded-[12px] border border-[#E5E7Eb] px-4 py-3">
        <div class="flex flex-col items-center">
            <h2 class="font-semibold text-[18px]">TUE</h2>
            <h2 class="font-semibold text-[18px]">02/20</h2>
        </div>
        <div class="w-full">
            <h3 class="font-semibold text-[18px]">Meeting</h3>
            <p>After school  |  Room 259</p>
        </div>
        <ChevronRight/>
    </div>
</div>
</div>
  <div class="w-3/12">
    <h3 class="font-semibold text-[18px] mb-2">Follow Us!</h3>
    <div class="flex gap-x-2 text-[14px]">
        <Instagram />
        <NuxtLink href="https://instagram.com/siths_model_rocketry" target="_blank" class="font-semibold">@siths_model_rocketry</NuxtLink>
    </div>
    <h3 class="font-semibold text-[18px] mt-3 mb-2">Suggested Clubs</h3>
</div>
  </div>
</template>

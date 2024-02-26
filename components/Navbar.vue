<script setup>
  import { Home, Calendar, Users, Newspaper } from 'lucide-vue-next';
  import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

</script>

<template>
    <div class="flex w-full justify-between items-center mb-8">
        <p class="font-semibold text-[16px]">Student Life</p>
        <div class="flex gap-x-8">
            <NuxtLink to="/">
                <p class="flex gap-x-2 font-semibold text-[16px] justify-center"><span><Home/></span>Home</p>
            </NuxtLink>
            <p class="flex gap-x-2 font-semibold text-[16px] justify-center"><span><Calendar/></span>Events</p>
            <p class="flex gap-x-2 font-semibold text-[16px] justify-center"><span><Users/></span>Clubs</p>
            <p class="flex gap-x-2 font-semibold text-[16px] justify-center"><span><Newspaper/></span>News</p>
        </div>
            <Avatar>
            <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
            <AvatarFallback>CN</AvatarFallback>
        </Avatar>
        
    </div>
</template>
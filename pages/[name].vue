<script setup>
import { File, Instagram, ChevronRight } from "lucide-vue-next";
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
import data from '../../assets/data.json'

const route = useRoute()

let club = data.find(club => club["Club Name"].toLowerCase().replace(/\s/g, '') === route.params.name)

console.log(club)

let presidents = club["Club President(s)"].split(", ")

console.log(presidents)

</script>

<template>
    <div class="flex w-full flex-col items-center mb-[-60px]">
        <img class="rounded-[6px] w-full h-[250px] object-cover"
            src="https://t3.ftcdn.net/jpg/04/86/29/98/360_F_486299886_4aXrDh0LPy7BK4SUJvhCkKpnnExNDsLX.jpg" />
        <div class="relative bottom-20 px-10 flex w-full gap-x-4">
            <img class="rounded-full h-[200px] w-[200px] object-cover shadow-md"
                src="https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg">
            <div class="flex items-center w-full justify-between relative top-6">
                <h1 class="font-semibold text-4xl">{{ club["Club Name"] }}</h1>
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
                <DialogTrigger class="flex gap-x-1 font-medium">
                    <File /> Club Charter
                </DialogTrigger>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Club Charter</DialogTitle>
                    </DialogHeader>
                    <embed src="../../Homerooms.pdf" />
                </DialogContent>
            </Dialog>
            <h3 class="font-semibold text-[18px] mt-3 mb-2">Leaders</h3>
            <div class="flex flex-col gap-y-2">
                <div class="flex gap-x-3" v-for="president in presidents">
                    <Avatar>
                        <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
                        <AvatarFallback>CN</AvatarFallback>
                    </Avatar>
                    <div class="flex flex-col">
                        <p class="font-semibold text-[14px]">{{president}}</p>
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
                    <p class="font-semibold text-[14px]">{{ club["Club Advisor"] }}</p>
                    <p class="text-[14px] color-[#525252] mt-[-3px]">Advisor</p>
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
                <div
                    class="flex justify-between items-center gap-x-7 w-full rounded-[12px] border border-[#E5E7Eb] px-4 py-3">
                    <div class="flex flex-col items-center">
                        <h2 class="font-semibold text-[18px]">TUE</h2>
                        <h2 class="font-semibold text-[18px]">02/20</h2>
                    </div>
                    <div class="w-full">
                        <h3 class="font-semibold text-[18px]">Meeting</h3>
                        <p>After school | Room {{ club["Room"] }}</p>
                    </div>
                    <ChevronRight />
                </div>
            </div>
        </div>
        <div class="w-3/12">
            <h3 class="font-semibold text-[18px] mb-2">Follow Us!</h3>
            <div class="flex gap-x-2 text-[14px]">
                <Instagram />
                <NuxtLink href="https://instagram.com" target="_blank" class="font-medium text-[16px]">@handle</NuxtLink>
            </div>
            <h3 class="font-semibold text-[18px] mt-3 mb-2">Suggested Clubs</h3>
        </div>
</div></template>
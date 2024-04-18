<script setup>
import { ArrowUpRight } from 'lucide-vue-next';
</script>

<template>
    <div class="flex flex-row h-[98vh] gap-x-4 w-full pb-2">
        <div class="flex h-full w-8/12 bg-slate-500 text-white items-end p-4">
            <h1 class="scroll-m-20 text-8xl font-extrabold tracking-tight lg:text-8xl">Explore Opportunities at Staten Island Tech</h1>
        </div>
        <div class="flex flex-col w-4/12 gap-y-4">
            <div class="h-1/2 bg-[url('https://www.solarcarchallenge.org/challenge/teams2022/staten_island.jpg')]" id="card">
                <NuxtLink to="/clubs">
                    <div class="flex w-full h-full items-end px-4 py-4" id="hover">
                        <div class="flex justify-between text-white items-center w-full" id="info">
                            <h2 class="scroll-m-20 text-3xl font-extrabold tracking-tight lg:text-4xl">Clubs</h2>
                            <ArrowUpRight class="arrow-icon" color="white" size="50" stroke-width="1.25"/>
                        </div>
                    </div>
                </NuxtLink>
            </div>
            <div class="h-1/2 bg-[url('/event.jpg')]" id="card">
                <NuxtLink to="/events">
                    <div class="flex w-full h-full items-end px-4 py-4" id="hover">
                        <div class="flex justify-between text-white items-center w-full" id="info">
                            <h2 class="scroll-m-20 text-3xl font-extrabold tracking-tight lg:text-4xl">Events</h2>
                            <ArrowUpRight class="arrow-icon" color="white" size="50" stroke-width="1.25"/>
                        </div>
                    </div>
                </NuxtLink>
            </div>
        </div>  
    </div>
</template>

<style scoped>
#card {
    background-size: cover;
    background-position-y: top;
    background-repeat: no-repeat;
    transition: 0.3s ease-in;
}

#hover {
    background-image: linear-gradient(45deg, rgba(23, 23, 24, 0.658) 50%, rgba(0, 255, 255, 0) 50%);
    background-size: 300% 100%;
    background-position: right bottom;
    z-index: 2;
    transition: 0.3s ease-in;
}

#card:hover #hover {
    background-position: left top;
}

h2 {
    transition: 0.3s ease-in;
}

#card:hover #info h2 {
    font-size: 48px;
    font-size-adjust: 10px;
    z-index: 3;
}

.arrow-icon {
    transition: 0.3s ease-in;
}
#card:hover #info .arrow-icon {
    width: 64px;
    height: 64px;
}

</style>
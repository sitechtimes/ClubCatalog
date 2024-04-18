<template>
    <div class="flex w-full justify-between items-center mb-2">
        <p class="font-bold text-[16px]">Club Catalog</p>
        <div class="flex gap-x-8">
            <NuxtLink to="/">
                <p class="font-medium text-[16px]">Home</p>
            </NuxtLink>
            <NuxtLink to="/events">
                <p class="font-medium text-[16px]">Events</p>
            </NuxtLink>
            <NuxtLink to="/clubs">
                <p class="font-medium text-[16px]">Clubs</p>
            </NuxtLink>
        </div>
        <Button>Sign In</Button>   
    </div>
</template>

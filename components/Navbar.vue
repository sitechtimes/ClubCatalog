<template>
    <div class="flex w-full justify-between items-center mb-2 main-container">
        <p class="font-bold text-[16px]">Club Catalog</p>
        <div class="flex gap-x-3">
            <NuxtLink to="/">
                <p class="font-medium text-[16px]">Home</p>
            </NuxtLink>
            <NuxtLink to="/clubs">
                <p class="font-medium text-[16px]">Clubs</p>
            </NuxtLink>
        </div>
        <a href="siths.org">SITHS Page</a>   
    </div>
</template>

<style scoped>

a {
    padding: 0.3rem;
    border-radius: 0.5rem;
    cursor: pointer;
    background-color: #033597;
    color: white;
}

a:hover {
    animation: fadein 0.3s;
    animation-fill-mode: forwards;
}

a:not(:hover) {
    animation: fadeout 0.3s;
    animation-fill-mode: forwards;
}


@keyframes fadein {
    0% { }
    100% { opacity: 0.7;
    }
}

@keyframes fadeout {
    0% {
        opacity: 0.7;
    }
    100% {
        opacity: 1;
    }
}

</style>

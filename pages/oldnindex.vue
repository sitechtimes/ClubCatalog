<script setup>
import Navbar from "../components/Navbar.vue";
</script>

<template>
    <div ID="container">
        <Navbar />
        <div id="container-main">
            <h1 id="home">Explore Opportunities at Staten Island Tech</h1>
            <div style="display: flex; flex-direction: row; gap: 1rem;">
                <NuxtLink to="/clubs">Browse Clubs</NuxtLink>
                <NuxtLink to="/">Contact Staff</NuxtLink>
            </div>
        </div>
    </div>
    
</template>

<style scoped>

    h1 {
        text-align: center;
    }
    #container {
        position: absolute;
        width: 100vw;
        height: 100vh;
        padding:1rem;
        background-image: linear-gradient(to bottom right, #7ceef9, #1594de);
        background-size: cover;
    } 
    #home {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 3rem;
        font-weight: bold;
    }

    #container-main {
        display: flex;
        flex-direction: column;
        justify-content: center;
            align-items: center;
            height: 90%;
    }

    a {
        background-color: #033597;
        text-decoration: none;
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        width: fit-content;
        align-self: center;
    }

    a:hover {
        animation: buttonfadein 0.3s;
        animation-fill-mode: forwards;
    }

    a:not(:hover) {
        animation: buttonfadeout 0.3s;
        animation-fill-mode: forwards;
    }

    @media (min-width: 600px) {
        #home {
            font-size: 5rem;
        }

        a {
            font-size: 2.3rem;
        }
    }

    @keyframes buttonfadein {
        0% {
            opacity: 1;
        }
        100% {
            opacity: 0.7;
        }
    }

    @keyframes buttonfadeout {
        0% {
            opacity: 0.7;
        }
        100% {
            opacity: 1;
        }
    }
</style>
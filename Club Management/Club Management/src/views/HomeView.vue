<script setup>
import clubs from "../assets/data.json";
import { ref } from "vue";
import login from '../components/login.vue'

const clubSearch = ref("");
const loginactive = ref(false);

</script>

<template>
  <main>
    <h1 style="display: flex; justify-content: center;">Club List</h1>
    <div id="clublist">
      <div v-for="club in clubs" class="clubitem">
        <p :to="`/${club['Club Name']}`" style="display: flex; justify-content: center;">
          {{ club["Club Name"] }}
        </p>
        <button id="presidentlogin" @click="loginactive = true">Login as President/Advisor</button>
      </div>
    </div>
  </main>
  <login v-if="loginactive" @close="loginactive = false" />
</template>

<style scoped>
  #clublist {
    display: flex;
    flex-direction: column;
    
  }

  a {
    text-decoration: none;
  }

  .clubitem {
    
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: bold;
    color: #ffffff;
    padding: 0.5rem;
    border-radius: 0.5rem;
    border: 2px solid #2c3e50;
    margin-bottom: 1.5rem;
    background-image: linear-gradient(to bottom right, #000000, #FFD700);    
  }

  #presidentlogin {
    font-size: 1.5rem;
    font-weight: bold;
    color: #2c3e50;
    padding: 0.5rem;
    border-radius: 0.5rem;
    border: 2px solid #2c3e50;
    margin-bottom: 0.5rem;
    cursor: pointer;
    background-color: white;
    transition: all 0.3s ease;
  }

  #presidentlogin:hover {
    background-color: #2c3e50;
    color: white;
  }

</style>

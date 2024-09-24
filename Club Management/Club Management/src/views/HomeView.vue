<template>
   <login v-if="loginactive" @close="loginactive = false"/>
    <h1 style="display: flex; justify-content: center;">Club List</h1>
    <div id="clublist">
      <div v-for="club in clubs" :key="club" class="clubitem">
        <a href="`/${club['Club Name']}`" style="display: flex; justify-content: center;">
          {{ club["Club Name"] }}
        </a>
        <button id="presidentlogin" @click="loginactive = true; updateCurrentClub(club)">Login as President/Advisor</button>
      </div>
    </div>
</template>

<script setup>
import clubs from "../assets/data.json";
import { ref, computed } from "vue";
import login from '../components/login.vue'
import { useLoginInfo } from '../stores/loginInfo'

const loginInfo = useLoginInfo();

function updateCurrentClub(clubName) {
  loginInfo.currentClub = clubName
}

const loginactive = ref(false)
const clubSearch = ref("");

</script>

<style scoped>
  #clublist {
    display: flex;
    flex-direction: column;
    
  }

  a {
    text-decoration: none;
    color: white;
  }

  .clubitem {
    
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
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

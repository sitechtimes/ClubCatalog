<template>
  <div @click.self="$emit('close')" id="backgroundLogin" style="width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); position: fixed; top: 0; left: 0;">
    <div id="loginPop">
      <label>Passkey{{ loginInfo.currentClub["Pass"] }}</label>
      <form v-on:submit.prevent="login">
        <input id="passEnter" v-model="passkey" type="password"/>
        <button type="submit">Login</button>
      </form>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useLoginInfo } from '../stores/loginInfo'
import data from '../assets/data.json'
import { useRouter } from 'vue-router'

const router = useRouter()
const passkey = ref('')
const loginInfo = useLoginInfo()

function login() {
  if (passkey.value === loginInfo.currentClub["Pass"]) {
    loginInfo.loggedIn = loginInfo.currentClub["Club Name"]
    passkey.value = ''
    router.push(`/${loginInfo.currentClub["Club Name"]}`)
  } else {
    alert("Incorrect Passkey")
  }
}
</script>

<style scoped>

button {
  background-color: #2c3e50;
  color: white;
  font-size: 1.5rem;
  border-radius: 0.5rem;
  padding: 0.5rem;
  margin-top: 0.5rem;
  cursor: pointer;
  margin: 0.2rem;
}

#passEnter {
  background-color: #2453d38c;
  color: white;
  font-size: 1.4rem;
  border-radius: 0.5rem;
  padding: 0.5rem;
  margin-top: 0.5rem;
  max-width: 70%;
}

label {
  font-size: 3rem;
  color: white;
  font-weight: bold;
}

#backgroundLogin {
  display: flex;
  align-items: center;
  justify-content: center;
}

#loginPop {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #2c3e50;
  border-radius: 0.5rem;
  padding: 2rem;
  width: 20rem;
  animation: grow 0.2s ease-in-out;
}

@keyframes grow {
  0% {
    transform: scale(0.1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

</style>

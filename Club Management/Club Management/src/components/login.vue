<template>
  <div @click.self="this.$emit('close')" id="backgroundLogin" style="width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); position: fixed; top: 0; left: 0;">
    <div>
      <label ID="LABEL">Passkey</label>
      <input v-model="passkey" type="password" :placeholder="clubName"/>
      <button @click="login">Login</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLoginInfo } from '../stores/loginInfo'
import data from '../assets/data.json'

const clubName = ref('')

defineProps({
  clubName: {
    type: String,
    required: true
  }
})
console.log(clubName)

const passkey = ref('')
const loginInfo = useLoginInfo()

function login() {
  console.log(clubName)
}
</script>

<style>

#LABEL {
  font-size: 3rem;
  color: white;
}

#backgroundLogin {
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>

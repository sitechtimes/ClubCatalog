<template>
    <h1 style="display: flex; justify-content: center">{{ $route.params.club }}</h1>
    <div v-if="permitted">
        <div id="eventlist">
          <div v-for="event in ['event1', 'event2', 'event3']" class="eventitem">
            <p>{{ event }}</p>
          </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useLoginInfo } from '../stores/loginInfo'
import { useRouter } from 'vue-router'


const loginInfo = useLoginInfo()
const router = useRouter()
const eventdata = ref(null)
const permitted = ref(false)
const apiKey = ''
const spreadsheetId = '1qG5AABVm3aLNkJjxizqjNjyE5jvyyvRZER8Icap4bLs'
const sheetName = 'ClubData'

onMounted(() => {
  if (loginInfo.loggedIn === router.currentRoute.value.params.club ) {
    permitted.value = true
  } else {
    permitted.value = false
  }
  console.log(permitted.value)
  fetch(`https://sheets.googleapis.com/v4/spreadsheets/${spreadsheetId}?key=${apiKey}`)
  .then(response => console.log(response.json()))
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
})


</script>

<style>

</style>
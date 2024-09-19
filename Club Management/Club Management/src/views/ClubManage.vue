<template>
    <h1 style="display: flex; justify-content: center">{{ $route.params.club }}</h1>
    <thead>
        <tr>
          <th v-for="(header, index) in data[0]" :key="index">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, rowIndex) in data.slice(1)" :key="rowIndex">
          <td v-for="(cell, cellIndex) in row" :key="cellIndex">{{ cell }}</td>
        </tr>
      </tbody>
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
import axios from 'axios';


const loginInfo = useLoginInfo()
const router = useRouter()
const eventdata = ref(null)
const permitted = ref(false)
const spreadsheetId = '1qG5AABVm3aLNkJjxizqjNjyE5jvyyvRZER8Icap4bLs'
const sheetName = 'ClubData'

const data = ref([]);

// Function to fetch data from Google Sheets API
const fetchSpreadsheetData = async () => {
  const spreadsheetId = '1qG5AABVm3aLNkJjxizqjNjyE5jvyyvRZER8Icap4bLs'; // Replace with your Spreadsheet ID
  const range = 'Sheet1!A1:Z100'; // Adjust as necessary
  const apiKey = ''; // Replace with your API key
  const url = `https://sheets.googleapis.com/v4/spreadsheets/${spreadsheetId}/values/${range}?key=${apiKey}`;

  try {
    const response = await axios.get(url);
    data.value = response.data.values;
  } catch (error) {
    console.error('Error fetching data from Google Sheets:', error);
  }
};

// Automatically fetch the spreadsheet data when the component is mounted
onMounted(fetchSpreadsheetData);
</script>


<style>

</style>
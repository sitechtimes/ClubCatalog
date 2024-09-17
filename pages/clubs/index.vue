<template>
  <div id="container-cat">
    <Navbar />
    <div id="container-main-cat">
      <h1 id="home">Explore Clubs</h1>
      <NuxtLink to="/clubs/oldindex">Browse Clubs</NuxtLink>
      <div id="catelog">
        <div v-for="club in clubs">
          <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.75rem;">
            <img
              style="border-radius: 50%; height: 130px;"
              src="https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM="
              alt=""
            />
            <div style="display: flex; flex-direction: column; gap: 0.25rem; align-items: baseline; padding: 0.75rem 0 0.75rem 1.25rem;">
                <NuxtLink :to="'/clubs/' + club['Club Name'].toLowerCase().replace(/\s/g, '')"><h4 style="font-weight: 600; font-size: 1.25rem;">{{ club["Club Name"] }}</h4></NuxtLink>
              <p style="font-size: 0.875rem;">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam.
              </p>
              <div style="display: flex; gap: 0.5rem; padding-top: 0.25rem;">
                <span v-for="category in club['Category']" 
                  style="background-color: #E5E7EB; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem; color: #6B7280"
                >
                  {{ category }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Navbar from "../../components/Navbar.vue";
import clubs from "../../assets/data.json";
import { Tags, Calendar, RefreshCw, Search } from "lucide-vue-next";
</script>

<style>

* {
}

a {
    width: fit-content;
}

#container-cat {
    position: absolute;
    width: 100vw;
    height: 100vh;
    padding:1rem;
    background-image: linear-gradient(to bottom right, #7ceef9, #1594de);
    background-size: cover;
}

#container-main-cat {
  display: flex;
  flex-direction: column;
  height: 90%;
  opacity: 0;
  animation: loadin 0.3s forwards;
}

#catelog {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 1rem;
  overflow-y: scroll;
  height: 100%;
  border : 1px solid #E5E7EB;
  border-radius: 0.5rem;
  -ms-overflow-style: none;
  scrollbar-width: none;
  width: fit-content;
  max-width: 1200px;
  margin: auto;
}

@keyframes loadin {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}
</style>
<template>
  <header>
    <div id="left">
      <div v-if="mainFocus">
        <img src="../assets/profilImage.png" alt>
        <p>{{ user }}</p>
        <div class="theend"></div>
      </div>
      <div v-if="!mainFocus" v-on:click="goBack">
        <img src="../assets/arrow.png" alt>
        <p>Go Back</p>
        <div class="theend"></div>
      </div>
    </div>
    <div id="right">
      <v-touch v-on:swipeleft="onSwipeLeft" v-on:swiperight="onSwipeRight">
        <DateBox :date="currentDate"></DateBox>
      </v-touch>
    </div>
  </header>
</template>

<script>
import DateBox from "../components/DateBox.vue";

export default {
  name: "Header",
  data: function() {
    return {
      user: "Ninna"
    };
  },
  props: {
    mainFocus: Boolean,
    currentDate: Date
  },
  components: {
    DateBox
  },
  methods: {
    goBack() {
      this.$emit("closeSeeMore", "someValue");
    },
    onSwipeLeft() {
      this.$emit("moveOneDay", "Minus");
    },
    onSwipeRight() {
      this.$emit("moveOneDay", "Plus");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding: 15px;
}

#left {
  text-align: left;
}

#left img {
  width: 50px;
  float: left;
  margin-right: 15px;
}

#left p {
  padding: 12px;
  font-family: "Inconsolata", monospace;
  text-transform: uppercase;
  letter-spacing: 2px;
}

#right {
  text-align: right;
}
</style>

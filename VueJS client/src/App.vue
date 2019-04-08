<template>
  <div id="app">
    <Header
      :currentDate="currentDate"
      :mainFocus="eyeInFocus"
      @closeSeeMore="closeSeeMore"
      @moveOneDay="moveOneDay"
    />
    <transition name="fade">
      <Timeline :usage="usage" :useToday="useToday" v-if="!eyeInFocus"/>
    </transition>
    <Eye :mainFocus="eyeInFocus" :status="statusOfTheDay"/>
    <transition name="slideDown">
      <MainDashboard
        v-if="eyeInFocus"
        @seemore="seeMore"
        :useToday="useToday"
        :useLimit="useLimit"
      />
    </transition>
  </div>
</template>

<script>
import axios from "axios";

import Header from "./components/Header.vue";
import Eye from "./components/Eye.vue";
import Timeline from "./components/Timeline.vue";
import MainDashboard from "./components/MainDashboard.vue";

export default {
  name: "app",
  components: {
    Header,
    Eye,
    Timeline,
    MainDashboard
  },
  data: function() {
    return {
      statusOfTheDay: 10,
      currentDate: new Date("2019-04-06"), // Used because of the stop of data
      useToday: 0,
      useLimit: 104,
      eyeInFocus: true,
      urlToDb:
        "ec2co-ecsel-mzvv3nxtei5-530863203.eu-west-1.elb.amazonaws.com:5000",
      usage: null
    };
  },
  created: function() {
    this.updateInformations();
  },
  methods: {
    seeMore() {
      this.eyeInFocus = !this.eyeInFocus;
      this.showBackBtn = !this.showBackBtn;
    },
    closeSeeMore() {
      this.eyeInFocus = !this.eyeInFocus;
      this.showBackBtn = !this.showBackBtn;
    },
    updateInformations() {
      // GETTING THE DAY'S ACCUMULATED
      var accumulatedRequestString =
        "http://" +
        this.urlToDb +
        "/api/accumulated/0" +
        (this.currentDate.getMonth() + 1) +
        "/" +
        this.currentDate.getDate();

      axios
        .get(accumulatedRequestString)
        .then(response => {
          this.useToday = Math.round(response.data.total);
          this.statusOfTheDay = response.data.todaysUse;
        })
        .catch();

      // GETTING THE DAILY USAGES - PR HOUR
      var dayRequestString =
        "http://" +
        this.urlToDb +
        "/api/day/0" +
        (this.currentDate.getMonth() + 1) +
        "/" +
        this.currentDate.getDate();

      axios
        .get(dayRequestString)
        .then(response => {
          this.usage = response.data;
        })
        .catch();
    },
    moveOneDay(direction) {
      if (direction == "Plus") {
        var oldDate = this.currentDate.getDate();
        var newDate = this.currentDate.setDate(this.currentDate.getDate() + 1);
        var today = new Date();

        // If the new date is greater then today's date - it resets...
        if (newDate > today) {
          this.currentDate = new Date(this.currentDate.setDate(oldDate));
        } else {
          this.currentDate = new Date(newDate);
        }
      } else {
        this.currentDate = new Date(
          this.currentDate.setDate(this.currentDate.getDate() - 1)
        );
      }
      this.updateInformations();
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Inconsolata");
@import url("assets/reset.css");

body {
  background: #343a4a;
}

#app {
  font-family: "Inconsolata", monospace, "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin-top: 60px;
  max-width: 500px;
  margin: 0 auto;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.theend {
  clear: both;
  width: 100%;
}

.slideDown-enter-active,
.slideDown-leave-active {
  transition: all 0.4s;
}
.slideDown-enter,
.slideDown-leave-to {
  transform: translateY(200px);
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s;
}

.fade-enter-active {
  transition-delay: 0.8s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

@font-face {
  font-family: "aarhusregular";
  src: url("assets/aarhus-webfont.woff2") format("woff2"),
    url("assets/aarhus-webfont.woff") format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>

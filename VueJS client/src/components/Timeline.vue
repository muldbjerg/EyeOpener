<template>
  <div>
    <div id="timelineArea">
      <div id="timeline">
        <div
          v-for="hour in usage"
          :key="hour.total"
          style="display: grid;align-self: end; border-bottom: solid 3px #fff;"
        >
          <div class="coldwater waterIndicator" :dataHeight="hour.cold"></div>
          <div class="hotwater waterIndicator" :dataHeight="hour.hot"></div>
        </div>
        <div v-for="(hour, index) in usage" :key="index">
          <div class="hourPin"></div>
          <span class="hourText" style>{{ hour.hour}}</span>
        </div>
      </div>
      <div class="theend"></div>
    </div>
    <div id="timelineBottom">
      {{ useToday }}
      <span>l</span>
      <br>
      <p>used today</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Timeline",
  props: ["usage", "useToday"],
  data: function() {
    return {
      active: true
    };
  },
  methods: {
    updateHeight() {
      setTimeout(function() {
        var x = document.getElementsByClassName("waterIndicator");
        for (var i = 0; i < x.length; i++) {
          x[i].style.height = x[i].getAttribute("dataHeight") * 20 + "px";
        }
      }, 50);
    }
  },
  mounted() {
    this.updateHeight();
  },
  watch: {
    usage() {
      this.updateHeight();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#timelineArea {
  position: absolute;
  width: 100vw;
  overflow-x: scroll;
  padding-top: 30px;
}

#timeline {
  display: grid;
  grid-template-columns: repeat(24, 1fr);
  grid-template-rows: 1fr 80px;
  width: 2400px;
}

.hourPin {
  width: 3px;
  height: 20px;
  background: #fff;
  margin: 0 auto 10px auto;
}

.hourText {
  font-family: "aarhusregular", sans-serif;
  font-size: 24px;
}

.waterIndicator {
  align-self: end;
}

.coldwater {
  width: 30px;
  margin: 0 auto;
  border: 2px solid #8593aa;
  margin-bottom: 5px;
  /* transition: 0.3s all; */
}

.hotwater {
  width: 30px;
  margin: 0 auto;
  border: 2px solid #cdabab;
  background-image: url(../assets/pattern.png);
  background-size: 30px;
  margin-bottom: 5px;
}

#timelineBottom {
  position: absolute;
  font-family: "aarhusregular";
  bottom: 50px;
  text-align: center;
  text-transform: uppercase;
  width: 100%;
  z-index: 99;
  font-size: 90px;
}

#timelineBottom span {
  font-size: 40%;
  color: #fff;
}

#timelineBottom p {
  font-family: "Inconsolata", monospace, "Avenir", Helvetica, Arial, sans-serif;
  font-size: 20px;
  margin-top: 10px;
}
</style>

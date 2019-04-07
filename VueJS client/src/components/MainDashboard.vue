<template>
  <div id="mainDashboard">
    <div>
      <div id="todaysNumber">
        {{ useToday }}
        <span>L</span>
        <p>Out of {{ useLimit }} L</p>
      </div>

      <div id="seeMore" v-on:click="onClickButton">
        <img src="../assets/arrowRight.png" alt>
        <br>See more
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainDashboard",
  components: {},
  props: {
    useToday: Number,
    useLimit: Number
  },
  data: function() {
    return {
      show: true
    };
  },
  methods: {
    onClickButton() {
      this.$emit("seemore", "someValue");
    }
  }
};
</script>

<style scoped>
#mainDashboard {
  position: absolute;
  max-width: 500px;
  margin: 0 auto;
  width: 100%;
  bottom: 0px;
  text-transform: uppercase;
}

#todaysNumber {
  font-family: "aarhusregular";
  position: relative;
  bottom: 0px;
  padding: 50px 90px;
  background: #8593aa;
  font-size: 80px;
  float: left;
  z-index: 10;
}

#todaysNumber span {
  font-size: 40%;
  color: #343a4a;
}

#todaysNumber p {
  font-family: "Inconsolata", monospace, "Avenir", Helvetica, Arial, sans-serif;
  font-size: 20px;
  margin-top: 10px;
}

#seeMore {
  position: relative;
  background-color: #cdabab;
  color: #343a4a;
  text-transform: uppercase;
  float: right;
  text-align: center;
  z-index: 92;
  height: 100px;
  margin-top: -140px;
  padding-top: 30px;
  padding-bottom: 10px;
  bottom: 0px;
  width: 40%;
}

#seeMore img {
  width: 70px;
}
</style>

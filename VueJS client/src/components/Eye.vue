<template>
  <div id="eyeArea">
    <div id="eye" v-bind:class="{ notInFocus: !mainFocus }" :style="statusStyle"></div>
  </div>
</template>

<script>
export default {
  name: "Eye",
  props: {
    status: Number,
    mainFocus: Boolean
  },
  data: function() {
    return {};
  },
  computed: {
    statusStyle() {
      return (
        " background: linear-gradient( rgba(223, 208, 184, 1) 0%, rgba(223, 208, 184, 1) " +
        (100 - this.status) +
        "%, rgba(23, 18, 10, 1) " +
        (100 - this.status) +
        "%, rgba(23, 18, 10, 1) 100%);"
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#eyeArea {
  padding: 80px 0;
}

#eye {
  width: 280px;
  height: 280px;
  border-radius: 140px;
  background-color: #dfd0b8;
  margin: 0 auto;
  box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.8);

  transition: all 1s;
}

#eye::before,
#eye::after {
  content: "";
  position: absolute;
  width: 30px;
  background-color: #000;
  height: 20px;
  margin-top: 135px;
}

#eye::before {
  margin-left: -170px;
  z-index: -1;
}

#eye::after {
  margin-left: 140px;
  z-index: -1;
}

#eye.notInFocus {
  position: relative;
  margin-top: 800px;
  transform: scale(4);
}
</style>

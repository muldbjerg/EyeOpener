<template>
  <div id="datebox">
    <div id="dateboxLeft">
      <p>{{ date.getDate() }}</p>
    </div>
    <div id="dateboxRight">
      <div id="dateboxRightTop">{{ months[date.getMonth()] }}</div>
      <div id="dateboxRightBottom">{{ date.getFullYear() }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DateBox",
  props: {
    date: Date
  },
  data: function() {
    return {
      months: [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
      ]
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#datebox {
  display: grid;
  justify-content: end;
  grid-template-columns: 60px 80px;
  text-align: center;
}

#dateboxLeft {
  border: 1px solid #8b95ae;
  border-right: none;
  font-family: "aarhusregular";
  /* padding: 7px 0; */
  font-size: 32px;
}

#dateboxLeft p {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  margin: 0px;
}

#dateboxRight {
  font-family: "Inconsolata", monospace;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 12px;
}

#dateboxRight div {
  border: 1px solid #8b95ae;
  padding: 6px 0;
}

div#dateboxRightTop {
  border-bottom: none;
}
</style>

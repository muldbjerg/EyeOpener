import Vue from "vue";
import App from "./App.vue";

Vue.config.productionTip = false;

var VueTouch = require("vue-touch");
Vue.use(VueTouch, { name: "v-touch" });

new Vue({
  render: h => h(App)
}).$mount("#app");

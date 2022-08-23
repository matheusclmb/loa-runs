import Help from "../views/Help.vue";
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Argos from "../views/Argos.vue";
import Valtan from "../views/Valtan.vue";
import Vykas from "../views/Vykas.vue";
import Submit from "../views/Submit.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/help",
    name: "help",
    component: Help,
  },
  {
    path: "/submitrun",
    name: "submitrun",
    component: Submit,
  },
  {
    path: "/abyss/argos",
    name: "argos",
    component: Argos,
  },
  {
    path: "/legion/valtan",
    name: "valtan",
    component: Valtan,
  },
  {
    path: "/legion/vykas",
    name: "vykas",
    component: Vykas,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

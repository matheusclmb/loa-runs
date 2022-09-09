<template>
  <RaidInfo v-bind:raid="raid" />
  <div class="tabs is-toggle is-centered">
    <ul>
      <li
        v-on:click="getActive('normal')"
        v-bind:class="{ 'is-active': isActive === 'normal' }"
      >
        <a>
          <span class="icon is-small"
            ><i class="fas fa-smile" aria-hidden="true"></i
          ></span>
          <span>Normal</span>
        </a>
      </li>
      <li
        v-on:click="getActive('hard')"
        v-bind:class="{ 'is-active': isActive === 'hard' }"
      >
        <a>
          <span class="icon is-small"
            ><i class="fa fa-ghost" aria-hidden="true"></i
          ></span>
          <span>Hard</span>
        </a>
      </li>
      <li
        v-on:click="getActive('inferno')"
        v-bind:class="{ 'is-active': isActive === 'inferno' }"
      >
        <a>
          <span class="icon is-small"
            ><i class="fas fa-fire" aria-hidden="true"></i
          ></span>
          <span>Inferno</span>
        </a>
      </li>
    </ul>
  </div>

  <div class="box">
    <h1 class="is-size-4 has-text-centered">Times</h1>
    <div class="is-flex is-align-items-center">
      <table
        v-if="isActive === 'normal'"
        class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth has-text-centered"
      >
        <thead>
          <tr class="has-text-centered">
            <th>Position</th>
            <th>Name</th>
            <th>Avg. iLvl</th>
            <th>Time</th>
            <th>Deathless</th>
            <th>Proof</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(run, index) in runData" v-bind:key="run.id">
            <td>{{ index + 1 }}</td>
            <td>
              {{ run.playerOne }} - {{ run.playerTwo }} -
              {{ run.playerThree }} - {{ run.playerFour }} -
              {{ run.playerFive }} - {{ run.playerSix }} -
              {{ run.playerSeven }} -
              {{ run.playerEight }}
            </td>
            <td>{{ run.averageIlvl }}</td>

            <td>{{ run.time }}</td>
            <td>{{ run.deathless }}</td>
            <td>
              <a v-bind:href="run.youtube">Video</a> /
              <a v-bind:href="run.screenshot">Screenshot</a>
            </td>
          </tr>
        </tbody>
      </table>

      <table
        v-if="isActive === 'hard'"
        class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth has-text-centered"
      >
        <thead>
          <tr class="has-text-centered">
            <th>Position</th>
            <th>Name</th>
            <th>Avg. iLvl</th>
            <th>Time</th>
            <th>Deathless</th>
            <th>Proof</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(run, index) in hardData" v-bind:key="run.id">
            <td>{{ index + 1 }}</td>
            <td>
              {{ run.playerOne }} - {{ run.playerTwo }} -
              {{ run.playerThree }} - {{ run.playerFour }} -
              {{ run.playerFive }} - {{ run.playerSix }} -
              {{ run.playerSeven }} -
              {{ run.playerEight }}
            </td>
            <td>{{ run.averageIlvl }}</td>

            <td>{{ run.time }}</td>
            <td>{{ run.deathless }}</td>
            <td>
              <a v-bind:href="run.youtube">Video</a> /
              <a v-bind:href="run.screenshot">Screenshot</a>
            </td>
          </tr>
        </tbody>
      </table>

      <table
        v-if="isActive === 'inferno'"
        class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth has-text-centered"
      >
        <thead>
          <tr class="has-text-centered">
            <th>Position</th>
            <th>Name</th>
            <th>Avg. iLvl</th>
            <th>Time</th>
            <th>Deathless</th>
            <th>Proof</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(run, index) in infernoData" v-bind:key="run.id">
            <td>{{ index + 1 }}</td>
            <td>
              {{ run.playerOne }} - {{ run.playerTwo }} -
              {{ run.playerThree }} - {{ run.playerFour }} -
              {{ run.playerFive }} - {{ run.playerSix }} -
              {{ run.playerSeven }} -
              {{ run.playerEight }}
            </td>
            <td>{{ run.averageIlvl }}</td>

            <td>{{ run.time }}</td>
            <td>{{ run.deathless }}</td>
            <td>
              <a v-bind:href="run.youtube">Video</a> /
              <a v-bind:href="run.screenshot">Screenshot</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import RaidInfo from "@/components/RaidInfo.vue";
import axios from "axios";

export default {
  name: "Valtan",
  data() {
    return {
      count: 0,
      raid: [],
      runData: [],
      hardData: [],
      infernoData: [],
      isActive: "normal",
    };
  },
  components: {
    RaidInfo,
  },
  mounted() {
    this.getRunsData();
    this.getHardData();
    this.getInfernoData();
    this.getData();
  },
  methods: {
    getActive(difficulty) {
      this.isActive = difficulty;
    },
    getData() {
      axios
        .get("/api/v1/legionraids/")
        .then((response) => {
          this.raid = response.data[0];

          document.title = this.raid.name + " | LOA.runs";
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getRunsData() {
      axios
        .get("/api/v1/legionraids/valtan/normal/")
        .then((response) => {
          this.runData = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getHardData() {
      axios
        .get("/api/v1/legionraids/valtan/hard/")
        .then((response) => {
          this.hardData = response.data;
        })

        .catch((error) => {
          console.log(error);
        });
    },
    getInfernoData() {
      axios
        .get("/api/v1/legionraids/valtan/inferno/")
        .then((response) => {
          this.infernoData = response.data;
        })

        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

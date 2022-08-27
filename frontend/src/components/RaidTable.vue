<template>
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
            <th>iLvl</th>
            <th>Time</th>
            <th>Deathless</th>
            <th>Proof</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ count }}</td>
            <td>
              {{ run.playerOne }} - {{ run.playerTwo }} -
              {{ run.playerThree }} - {{ run.playerFour }} -
              {{ run.playerFive }} - {{ run.playerSix }} -
              {{ run.playerSeven }} -
              {{ run.playerEight }}
            </td>
            <td>1468</td>
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
            <th>iLvl</th>
            <th>Time</th>
            <th>Deathless</th>
            <th>Proof</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>a</td>
            <td>1468</td>
            <td>12:41</td>
            <td>Yes</td>
            <td><a href="#">Click</a></td>
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
            <th>iLvl</th>
            <th>Time</th>
            <th>Deathless</th>
            <th>Proof</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>
              Inferno - Mario - Kalleb - Otto - Unpleasant - Persa - Bob - Gus
            </td>
            <td>1468</td>
            <td>12:41</td>
            <td>Yes</td>
            <td><a href="#">Click</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "RaidTable",
  props: {
    run: Object,
    hard: Object,
  },
  data() {
    return {
      count: 1,
      isActive: "normal",
    };
  },
  methods: {
    getActive(difficulty) {
      this.isActive = difficulty;
    },
  },
};
</script>

<style>
thead,
td,
tr,
th {
  text-align: center !important;
  vertical-align: middle !important;
}
</style>

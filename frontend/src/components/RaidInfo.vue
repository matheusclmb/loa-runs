<template>
  <div class="box">
    <div class="is-flex is-align-items-center">
      <img src="../assets/argos.jpeg" alt="Argos" class="mr-6" />
      <ul>
        <li class="is-size-1">Argos</li>
        <li><strong>Type:</strong> Abyss Raid</li>
        <li><strong>Comp:</strong> 8 players</li>
        <li><strong>Gates:</strong> 3</li>
        <li><strong>Minimum iLvl:</strong> 1370 (normal)</li>
      </ul>
    </div>
  </div>

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
            <td>1</td>
            <td>
              Player - Mario - Kalleb - Otto - Unpleasant - Persa - Bob - Gus
            </td>
            <td>1468</td>
            <td>12:41</td>
            <td>Yes</td>
            <td><a href="#">Click</a></td>
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
            <td>
              Jonas - Mario - Kalleb - Otto - Unpleasant - Persa - Bob - Gus
            </td>
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
              Iferno - Mario - Kalleb - Otto - Unpleasant - Persa - Bob - Gus
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
  name: "Raidinfo",
  data() {
    return {
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

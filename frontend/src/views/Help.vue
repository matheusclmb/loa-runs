<template>
  <div class="box has-text-centered">
    <h1 class="is-size-4">
      <strong> How to submit a run</strong>
    </h1>
    <ul>
      <li>Click on <router-link to="/submitrun">Submit Run</router-link></li>
      <li>
        Fill in the form with valid information (Name of players, time,
        deathless, ilvl and etc)
      </li>
      <li>
        Submit a proof of time (Either a video or a screenshot of the end of
        raid)
      </li>
      <li>
        Wait for the admin to approve your run. If approved, your run will be
        shown at the respective category,time and position.
      </li>
      <li class="has-text-grey">
        OBS: If you want to submit a bus run, you should type
        <span class="has-text-danger" style="border-bottom: 1px solid red"
          >Player</span
        >
        in the form and
        <span class="has-text-danger" style="border-bottom: 1px solid red"
          >0 (Zero)</span
        >
        as ilvl of the player that was afk.
      </li>
    </ul>

    <h1 class="is-size-4 mt-6">Example</h1>
    <img src="../assets/formexample.png" alt="" />
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Help",
  mounted() {
    document.title = "Help | LOA.runs";
  },
};
</script>

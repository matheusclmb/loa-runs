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
        shown at the respective category and time.
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

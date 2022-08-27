<template>
  <div class="box">
    <div class="is-flex is-align-items-center">
      <img v-bind:src="raid.get_image" alt="Argos" class="mr-6" />
      <ul>
        <li class="is-size-1">{{ raid.name }}</li>
        <li><strong>Type:</strong> {{ raid.type }}</li>
        <li><strong>Comp:</strong> {{ raid.comp }} players</li>
        <li><strong>Gates:</strong> {{ raid.gates }}</li>
        <li>
          <strong>Minimum iLvl:</strong> {{ raid.minimum_level }} /
          {{ raid.minimum_level2 }} / {{ raid.minimum_level3 }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Raidinfo",
  props: {
    raid: Object,
    run: Object,
  },
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

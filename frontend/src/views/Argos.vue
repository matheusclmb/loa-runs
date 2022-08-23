<template>
  <RaidInfo v-bind:raid="raid" />
</template>

<script>
import RaidInfo from "@/components/RaidInfo.vue";
import axios from "axios";

export default {
  name: "Argos",
  data() {
    return {
      raid: [],
    };
  },
  components: {
    RaidInfo,
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      axios
        .get("/api/v1/abyssraids/")
        .then((response) => {
          this.raid = response.data[0];

          document.title = this.raid.name + " | LOA.runs";
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

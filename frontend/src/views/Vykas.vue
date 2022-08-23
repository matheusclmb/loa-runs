<template>
  <RaidInfo v-bind:raid="raid" />
</template>

<script>
import RaidInfo from "@/components/RaidInfo.vue";
import axios from "axios";

export default {
  name: "Vykas",
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
        .get("/api/v1/legionraids/")
        .then((response) => {
          this.raid = response.data[1];

          document.title = this.raid.name + " | LOA.runs";
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

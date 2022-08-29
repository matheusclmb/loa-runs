<template>
  <div class="home">
    <div class="box has-text-centered has-background-dark has-text-primary">
      <h1 class="is-size-3">Welcome to LOA.runs!</h1>
      <p>
        This website was created to track the best times for each raid. Submit a
        run and dispute for the first place!
      </p>
      <p>PS: Website still in development.</p>
    </div>
  </div>

  <h1 class="is-size-3 has-text-centered">Last Updates</h1>

  <div
    v-for="post in blogpost"
    v-bind:key="post"
    class="topthree has-text-centered mb-5"
  >
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          {{ post.title }} ‎
          <time class="has-text-primary"> ({{ post.date }})</time>
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          <p>
            {{ post.body }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      blogpost: [],
    };
  },
  mounted() {
    this.getData();
    document.title = "LOA.runs";
  },
  methods: {
    getData() {
      axios
        .get("/api/v1/blog/")
        .then((response) => {
          this.blogpost = response.data;
          document.title = "LOA.runs";
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

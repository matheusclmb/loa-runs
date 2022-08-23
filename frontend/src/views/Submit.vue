<template>
  <div
    class="form is-flex is-justify-content-center has-text-centered fullclass"
  >
    <form action="">
      <label for="oi">Proof:</label>

      <div class="control social">
        <label class="radio">
          <input
            type="radio"
            name="answer"
            v-on:click="getOption('youtube')"
            v-bind:class="{ 'is-active': isActive === 'youtube' }"
          />
          Youtube/Video
        </label>
        <label class="radio">
          <input
            type="radio"
            name="answer"
            v-on:click="getOption('screenshot')"
            v-bind:class="{ 'is-active': isActive === 'screenshot' }"
          />
          Screenshot
        </label>
      </div>

      <div v-if="isActive === 'screenshot'" class="file has-name social">
        <label class="file-label">
          <input class="file-input" type="file" name="resume" />
          <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-upload"></i>
            </span>
            <span class="file-label"> Choose a file… </span>
          </span>
          <span class="file-name"> No screenshot selected </span>
        </label>
      </div>

      <div v-if="isActive === 'youtube'" class="social">
        <p class="control has-icons-left">
          <input class="input" type="email" placeholder="Youtube/Video" />
          <span class="icon is-small is-left">
            <i class="fab fa-youtube"></i>
          </span>
        </p>
      </div>

      <div class="social is-flex">
        <div class="select">
          <select>
            <option>Abyss Raid</option>
            <option>Legion Raid</option>
          </select>
        </div>

        <div class="select">
          <select>
            <option>Argos</option>
            <option>Valtan</option>
          </select>
        </div>

        <div class="select">
          <select>
            <option>Normal</option>
            <option>Valtan</option>
          </select>
        </div>
      </div>

      <div class="time is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Time (HH:MM:SS)" />
          <span class="icon is-small is-left">
            <i class="fas fa-stopwatch"></i>
          </span>
        </p>

        <div class="select">
          <select>
            <option>Deathless</option>
            <option>No</option>
          </select>
        </div>
      </div>

      <div class="social">
        <p class="control has-icons-left">
          <input class="input" type="email" placeholder="Discord" />
          <span class="icon is-small is-left">
            <i class="fab fa-discord"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 1" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 2" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 3" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 4" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 5" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 6" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 7" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input class="input" type="text" placeholder="Player 8" />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input class="input" type="number" placeholder="Item Level" />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="control">
        <button class="button is-link" type="submit">Submit Run</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Submit Run",
  data() {
    return {
      isActive: "none",
    };
  },
  components: {},
  mounted() {
    document.title = "Submit Run | LOA.runs";
  },
  methods: {
    getOption(option) {
      this.isActive = option;
    },
  },
};
</script>

<style>
.players,
.time,
.social {
  gap: 15px !important;
  margin-top: 10px !important;
  justify-content: center !important;
}

button {
  margin-top: 10px !important;
}
</style>

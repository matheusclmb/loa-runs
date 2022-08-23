<template>
  <div class="box has-text-centered">
    <p class="mb-3">
      <strong>
        <i class="fas fa-exclamation-triangle"></i>
        <span class="text-danger"> Submission Rules </span>
      </strong>
    </p>
    <p class="mb-3">
      Enter valid data and attach a proof (Youtube/Twitch/Video or Screenshot),
      runs without proof will be insta declined.
    </p>
    <p class="mb-3">In case you need, here is a template of the form: link</p>
    <p class="mb-3">
      We need your discord for contacting you if anything happens or if we need
      additional information.
    </p>
  </div>

  <div
    class="form is-flex is-justify-content-center has-text-centered fullclass"
  >
    <form method="post" @submit.prevent="postNow">
      <label for="oi">Proof:</label>

      <div class="control social">
        <label class="radio">
          <input
            type="radio"
            name="youtube-choice"
            v-on:click="getOption('youtube-choice')"
            v-bind:class="{ 'is-active': isActive === 'youtube-choice' }"
          />
          Youtube/Video
        </label>

        <label class="radio">
          <input
            type="radio"
            name="screenshot-choice"
            v-on:click="getOption('screenshot-choice')"
            v-bind:class="{ 'is-active': isActive === 'screenshot-choice' }"
          />
          Screenshot
        </label>
      </div>

      <div v-if="isActive === 'screenshot-choice'" class="file has-name social">
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

      <div v-if="isActive === 'youtube-choice'" class="social">
        <p class="control has-icons-left">
          <input
            class="input"
            type="url"
            placeholder="Youtube/Video"
            v-model="youtube"
            name="youtube"
          />
          <span class="icon is-small is-left">
            <i class="fab fa-youtube"></i>
          </span>
        </p>
      </div>

      <div class="social is-flex">
        <div class="select">
          <select name="raid_type" v-model="raid_type">
            <option>Abyss Raid</option>
            <option>Legion Raid</option>
          </select>
        </div>

        <div class="select">
          <select name="raid_name" v-model="raid_name">
            <option>Argos</option>
            <option>Valtan</option>
          </select>
        </div>

        <div class="select">
          <select name="difficulty" v-model="difficulty">
            <option>Normal</option>
            <option>Valtan</option>
          </select>
        </div>
      </div>

      <div class="time is-flex">
        <p class="control has-icons-left">
          <input
            class="input"
            type="text"
            placeholder="Time (HH:MM:SS)"
            required
            name="time"
            v-model="time"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-stopwatch"></i>
          </span>
        </p>

        <div class="select">
          <select name="deathless" v-model="deathless">
            <option>Deathless</option>
            <option>No</option>
          </select>
        </div>
      </div>

      <div class="social">
        <p class="control has-icons-left">
          <input
            class="input"
            type="text"
            placeholder="Discord"
            required
            name="discord"
            v-model="discord"
          />
          <span class="icon is-small is-left">
            <i class="fab fa-discord"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input
            class="input"
            type="text"
            placeholder="Player 1"
            required
            name="playerOne"
            v-model="playerOne"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input
            class="input"
            type="number"
            placeholder="Item Level"
            required
            name="playerOneLVL"
            v-model="playerOneLVL"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-arrow-up-9-1"></i>
          </span>
        </p>
      </div>

      <div class="players is-flex">
        <p class="control has-icons-left">
          <input
            class="input"
            type="text"
            placeholder="Player 2"
            required
            name="playerTwo"
            v-model="playerTwo"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-users"></i>
          </span>
        </p>

        <p class="control has-icons-left">
          <input
            class="input"
            type="number"
            placeholder="Item Level"
            required
            name="playerOneLVL"
            v-model="playerOneLVL"
          />
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
      form: {
        youtube: "",
        screenshot: "",
        raid_type: "",
        difficulty: "",
        time: "",
        deathless: "",
        discord: "",
        playerOne: "",
        playerTwo: "",
        playerThree: "",
        playerFour: "",
        playerFive: "",
        playerSix: "",
        playerSeven: "",
        playerEight: "",
        playerOneLVL: "",
        playerTwoLVL: "",
        playerThreeLVL: "",
        playerFourLVL: "",
        playerFiveLVL: "",
        playerSixLVL: "",
        playerSevenLVL: "",
        playerEightLVL: "",
      },
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
    postNow() {
      axios.post("/api/v1/createrun/", this.form),
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        };
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

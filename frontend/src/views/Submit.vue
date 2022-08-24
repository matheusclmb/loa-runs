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
    <p class="mb-3">
      In case you need, here is a template of the form:
      <routerLink to="/help">Click here</routerLink>
    </p>
    <p class="mb-3">
      We need your discord for contacting you if anything happens or if we need
      additional information.
    </p>
  </div>

  <div
    class="form is-flex is-justify-content-center has-text-centered fullclass"
  >
    <form ref="formrun" method="post" @submit.prevent="postNow">
      <label for="oi">Proof:</label>

      <div class="control social">
        <label class="radio">
          <input
            class="radiovil"
            type="radio"
            value="0"
            name="screenshot-choice"
            v-on:click="getOption('youtube-choice')"
            v-bind:class="{ 'is-active': isActive === 'youtube-choice' }"
          />
          Youtube/Video
        </label>

        <label class="radio">
          <input
            type="radio"
            value="1"
            name="screenshot-choice"
            v-on:click="getOption('screenshot-choice')"
            v-bind:class="{ 'is-active': isActive === 'screenshot-choice' }"
          />
          Screenshot
        </label>
      </div>

      <div v-if="isActive === 'screenshot-choice'" class="file has-name social">
        <label class="file-label">
          <input
            class="file-input"
            type="file"
            name="resume"
            v-on:change="fileUp"
            ref="file"
          />
          <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-upload"></i>
            </span>
            <span class="file-label"> Choose a file… </span>
          </span>
          <span class="file-name"> {{ fileName }}</span>
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
        <div class="field">
          <label class="label">Raid Type</label>
          <div class="select">
            <select name="raid_type" v-model="raid_type">
              <option>Abyss Raid</option>
              <option>Legion Raid</option>
            </select>
          </div>
        </div>

        <div class="field">
          <label class="label">Raid Name</label>
          <div class="select">
            <select name="raid_name" v-model="raid_name">
              <option value="Argos">Argos</option>
              <option value="Valtan">Valtan</option>
              <option value="Vykas">Vykas</option>
            </select>
          </div>
        </div>

        <div class="field">
          <label class="label">Mode</label>
          <div class="select">
            <select name="difficulty" v-model="difficulty">
              <option>Normal</option>
              <option>Hard</option>
              <option>Inferno</option>
            </select>
          </div>
        </div>

        <div class="field">
          <label class="label">Deathless?</label>
          <div class="select">
            <select name="deathless" v-model="deathless">
              <option>True</option>
              <option>False</option>
            </select>
          </div>
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
      </div>

      <div class="social">
        <p class="control has-icons-left">
          <input
            ref="discord"
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
            v-model="playerTwoLVL"
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
            placeholder="Player 3"
            name="playerThree"
            v-model="playerThree"
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
            name="playerThreeLVL"
            v-model="playerThreeLVL"
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
            placeholder="Player 4"
            name="playerFour"
            v-model="playerFour"
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
            name="playerFourLVL"
            v-model="playerFourLVL"
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
            placeholder="Player 5"
            name="playerFive"
            v-model="playerFive"
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
            name="playerFiveLVL"
            v-model="playerFiveLVL"
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
            placeholder="Player 6"
            name="playerSix"
            v-model="playerSix"
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
            name="playerSixLVL"
            v-model="playerSixLVL"
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
            placeholder="Player 7"
            name="playerSeven"
            v-model="playerSeven"
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
            name="playerSevenLVL"
            v-model="playerSevenLVL"
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
            placeholder="Player 8"
            name="playerEight"
            v-model="playerEight"
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
            name="playerEightLVL"
            v-model="playerEightLVL"
          />
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
import { useToast } from "vue-toast-notification";

export default {
  name: "Submit Run",
  data() {
    return {
      isActive: "none",
      fileName: "No screenshot selected",
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

    clearInput() {
      this.$refs["formrun"].reset();
    },
    postNow() {
      const toast = useToast();
      const formData = new FormData();

      if (this.isActive === "screenshot-choice") {
        formData.append("screenshot", this.newfile);
      } else {
        formData.append("youtube", this.youtube);
      }

      formData.append("raid_type", this.raid_type);
      formData.append("raid_name", this.raid_name);
      formData.append("difficulty", this.difficulty);
      formData.append("time", this.time);
      formData.append("deathless", this.deathless);
      formData.append("discord", this.discord);
      formData.append("playerOne", this.playerOne);
      formData.append("playerTwo", this.playerTwo);
      formData.append("playerThree", this.playerThree);
      formData.append("playerFour", this.playerFour);
      formData.append("playerFive", this.playerFive);
      formData.append("playerSix", this.playerSix);
      formData.append("playerSeven", this.playerSeven);
      formData.append("playerEight", this.playerEight);
      formData.append("playerOneLVL", this.playerOneLVL);
      formData.append("playerTwoLVL", this.playerTwoLVL);
      formData.append("playerThreeLVL", this.playerThreeLVL);
      formData.append("playerFourLVL", this.playerFourLVL);
      formData.append("playerFiveLVL", this.playerFiveLVL);
      formData.append("playerSixLVL", this.playerSixLVL);
      formData.append("playerSevenLVL", this.playerSevenLVL);
      formData.append("playerEightLVL", this.playerEightLVL);

      axios
        .post("/api/v1/createrun/", formData)
        .then(() => {
          this.clearInput(), toast.success("Your run has been submitted!");
        })
        .catch((error) => {
          toast.error("Something went wrong, please try again.");
        }),
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        };
    },
    fileUp(e) {
      this.newfile = e.target.files[0];
      this.fileName = this.newfile.name;
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

input[type="radio"] {
  accent-color: hsl(229deg, 53%, 53%) !important;
}
</style>

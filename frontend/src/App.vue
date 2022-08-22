<template>
  <nav class="navbar is-transparent">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <img
          src="./assets/loa-logo.png"
          alt="LOA.runs: there always a better time."
          width="112"
          height="28"
        />
      </router-link>
      <div class="navbar-burger" data-target="navbarExampleTransparentExample">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>

    <div id="navbarExampleTransparentExample" class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item"> Home </router-link>
        <div class="navbar-item has-dropdown is-hoverable">
          <router-link to="/abyss" class="navbar-link">
            Abyss Raids
          </router-link>
          <div class="navbar-dropdown is-boxed">
            <router-link to="/abyss/argos" class="navbar-item is-active">
              Argos
            </router-link>
          </div>
        </div>
        <div class="navbar-item has-dropdown is-hoverable">
          <router-link to="/legion" class="navbar-link">
            Legion Raids
          </router-link>
          <div class="navbar-dropdown is-boxed">
            <router-link to="/legion/valtan" class="navbar-item has-text-link">
              Valtan
            </router-link>

            <router-link to="/legion/vykas" class="navbar-item has-text-danger">
              Vykas
            </router-link>

            <router-link
              to="/legion/kakulsaydon"
              class="navbar-item has-text-success"
            >
              Kakul-Saydon
            </router-link>
          </div>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="field is-grouped">
            <p class="control">
              <a
                class="bd-tw-button button"
                data-social-network="Twitter"
                data-social-action="tweet"
                data-social-target="https://bulma.io"
                target="_blank"
                href="https://twitter.com/intent/tweet?text=Bulma: a modern CSS framework based on Flexbox&amp;hashtags=bulmaio&amp;url=https://bulma.io&amp;via=jgthms"
              >
                <span class="icon">
                  <i class="fas fa-circle-question"></i>
                </span>
                <span> Help </span>
              </a>
            </p>
            <p class="control">
              <a
                class="button is-link"
                href="https://github.com/jgthms/bulma/releases/download/0.9.4/bulma-0.9.4.zip"
              >
                <span class="icon">
                  <i class="fas fa-upload"></i>
                </span>
                <span>Submit Run</span>
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>

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
          <router-link to="#" class="navbar-link"> Abyss Raids </router-link>
          <div class="navbar-dropdown is-boxed">
            <router-link to="/abyss/argos" class="navbar-item is-active">
              Argos
            </router-link>
          </div>
        </div>
        <div class="navbar-item has-dropdown is-hoverable">
          <router-link to="#" class="navbar-link"> Legion Raids </router-link>
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
              <router-link class="bd-tw-button button" to="/help">
                <span class="icon">
                  <i class="fas fa-circle-question"></i>
                </span>
                <span> Help </span>
              </router-link>
            </p>
            <p class="control">
              <router-link class="button is-link" to="/submitrun">
                <span class="icon">
                  <i class="fas fa-upload"></i>
                </span>
                <span>Submit Run</span>
              </router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <section class="section">
    <router-view />
  </section>

  <footer class="footer">
    <div class="content has-text-centered">
      <p>
        <strong>LOA.runs</strong> by
        <a href="https://github.com/matheusclmb/">CLMB</a>. This website is not
        affiliated or endorsed with/by
        <a href="https://www.amazongames.com/">Amazon Games</a>
        or
        <a href="https://smilegate.com/">SmileGate</a>. All rights reserved to
        those companies.
      </p>
      <div class="field is-grouped is-justify-content-center">
        <p class="control">
          <a
            class="button is-link"
            href="https://github.com/matheusclmb/loa-runs"
            target="_blank"
          >
            <span class="icon">
              <i class="fab fa-github"></i>
            </span>
            <span>GitHub</span>
          </a>
        </p>

        <p class="control">
          <a
            class="button is-link"
            href="https://www.buymeacoffee.com/matheusclmb"
            target="_blank"
          >
            <span class="icon">
              <i class="fas fa-mug-hot"></i>
            </span>
            <span>Buy Me A Coffee</span>
          </a>
        </p>
      </div>
    </div>
  </footer>
</template>

<style lang="scss">
@import "../node_modules/bulma";

html,
body {
  height: 100vh;
}
</style>

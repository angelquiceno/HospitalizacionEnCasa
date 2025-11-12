<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Hospital en Casa G2</h1>
      <nav>
        <button v-if="is_auth" @click="goToDashboard">Inicio</button>
        <button v-if="is_auth" @click="logout">Cerrar Sesión</button>
        <button v-if="!is_auth" @click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" @click="loadSignUp">Registrarse</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view
        @completedLogIn="completedLogIn"
        @completedSignUp="completedSignUp"
      />
    </div>
    <div class="footer">
      <h2>Hospital en Casa G2 2025</h2>
    </div>
  </div>
</template>

<script>
import authService from "./services/auth.service";

export default {
  name: "App",
  data() {
    return {
      is_auth: false,
    };
  },

  computed: {
    isAuthRoute() {
      return this.$route.name === "login" || this.$route.name === "signup";
    },
  },

  methods: {
    verifyAuth() {
      this.is_auth = authService.isAuthenticated();
    },

    loadLogIn() {
      this.$router.push({ name: "login" });
    },

    loadSignUp() {
      this.$router.push({ name: "signup" });
    },

    goToDashboard() {
      this.$router.push({ name: "dashboard" });
    },

    logout() {
      authService.logout();
      this.is_auth = false;
      this.$router.push({ name: "login" });
    },

    completedLogIn(data) {
      this.is_auth = true;
    },

    completedSignUp(data) {
      this.is_auth = true;
    },
  },

  created() {
    this.verifyAuth();
  },

  watch: {
    $route() {
      this.verifyAuth();
    },
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h1 {
  width: 20%;
  text-align: center;
}
.header nav {
  height: 100%;
  width: 20%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
}
.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #fdfefe;
}
.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #e5e7e9;
}
.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

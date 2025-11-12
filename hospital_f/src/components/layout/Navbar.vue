<template>
  <div class="navbar">
    <div class="navbar-brand">
      <h2>Hospital en Casa</h2>
    </div>
    <div class="navbar-user">
      <span v-if="currentUser">{{ currentUser.nombre }} {{ currentUser.apellido }}</span>
      <button @click="logout" class="btn-logout">Cerrar Sesión</button>
    </div>
  </div>
</template>

<script>
import authService from "../../services/auth.service";

export default {
  name: "Navbar",
  data() {
    return {
      currentUser: null,
    };
  },
  async mounted() {
    try {
      this.currentUser = await authService.getCurrentUser();
    } catch (error) {
      console.error("Error al obtener usuario:", error);
    }
  },
  methods: {
    logout() {
      authService.logout();
      this.$router.push({ name: "login" });
    },
  },
};
</script>

<style scoped>
.navbar {
  background-color: #283747;
  color: #e5e7e9;
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.navbar-brand h2 {
  margin: 0;
  font-size: 24px;
}
.navbar-user {
  display: flex;
  align-items: center;
  gap: 15px;
}
.navbar-user span {
  font-size: 16px;
}
.btn-logout {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.btn-logout:hover {
  background-color: #c0392b;
}
</style>

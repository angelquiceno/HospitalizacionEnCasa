<template>
  <div class="sidebar">
    <nav class="sidebar-nav">
      <router-link to="/dashboard" class="nav-item" active-class="active">
        <span>🏠</span> Inicio
      </router-link>
      <router-link to="/dashboard/pacientes" class="nav-item" active-class="active">
        <span>👥</span> Pacientes
      </router-link>
      <router-link to="/dashboard/personal" class="nav-item" active-class="active">
        <span>⚕️</span> Personal de Salud
      </router-link>
      <router-link to="/dashboard/familiares" class="nav-item" active-class="active">
        <span>👨‍👩‍👧</span> Familiares
      </router-link>
      <router-link to="/dashboard/historias" class="nav-item" active-class="active">
        <span>📋</span> Historias Clínicas
      </router-link>
      <router-link to="/dashboard/signos" class="nav-item" active-class="active">
        <span>💓</span> Signos Vitales
      </router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
};
</script>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #34495e;
  min-height: calc(100vh - 60px);
  padding: 20px 0;
}
.sidebar-nav {
  display: flex;
  flex-direction: column;
}
.nav-item {
  color: #ecf0f1;
  text-decoration: none;
  padding: 15px 25px;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: background-color 0.3s;
  font-size: 16px;
}
.nav-item:hover {
  background-color: #2c3e50;
}
.nav-item.active {
  background-color: #1abc9c;
  border-left: 4px solid #16a085;
}
.nav-item span {
  font-size: 20px;
}
</style>

<template>
  <div class="dashboard">
    <Navbar />
    <div class="dashboard-content">
      <Sidebar />
      <div class="main-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../layout/Navbar.vue";
import Sidebar from "../layout/Sidebar.vue";

export default {
  name: "Dashboard",
  components: {
    Navbar,
    Sidebar,
  },
};
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background-color: #ecf0f1;
}
.dashboard-content {
  display: flex;
}
.main-content {
  flex: 1;
  padding: 30px;
  overflow-y: auto;
}
</style>

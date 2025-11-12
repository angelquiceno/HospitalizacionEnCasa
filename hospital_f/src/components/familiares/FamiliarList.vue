<template>
  <div class="list-container">
    <h1>Familiares</h1>
    <router-link to="/dashboard/familiares/nuevo" class="btn">➕ Nuevo</router-link>
    <table v-if="items.length">
      <thead>
        <tr><th>ID</th><th>Nombre</th><th>Email</th><th>Parentezco</th></tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id_Familiar">
          <td>{{ item.id_Familiar }}</td>
          <td>{{ item.usuario?.nombre }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.parentezco }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import familiarService from "../../services/familiar.service";
export default {
  data() {
    return { items: [] };
  },
  async mounted() {
    this.items = await familiarService.getAll();
  },
};
</script>

<style scoped>
.list-container { background: white; padding: 30px; border-radius: 10px; }
table { width: 100%; border-collapse: collapse; margin-top: 20px; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ecf0f1; }
th { background: #34495e; color: white; }
.btn { background: #27ae60; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; }
</style>

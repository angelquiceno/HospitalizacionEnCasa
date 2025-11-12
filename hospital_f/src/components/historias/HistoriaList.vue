<template>
  <div class="list-container">
    <h1>Historias Clínicas</h1>
    <router-link to="/dashboard/historias/nueva" class="btn">➕ Nueva</router-link>
    <table v-if="items.length">
      <thead>
        <tr><th>ID</th><th>Paciente</th><th>Diagnóstico</th><th>Fecha</th></tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id_HistoriaClinica">
          <td>{{ item.id_HistoriaClinica }}</td>
          <td>{{ item.nombre_paciente }} {{ item.apellido_paciente }}</td>
          <td>{{ item.diagnostico }}</td>
          <td>{{ new Date(item.fecha).toLocaleDateString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import historiaService from "../../services/historia.service";
export default {
  data() {
    return { items: [] };
  },
  async mounted() {
    this.items = await historiaService.getAll();
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

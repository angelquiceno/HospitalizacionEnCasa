<template>
  <div class="list-container">
    <h1>Signos Vitales</h1>
    <router-link to="/dashboard/signos/nuevo" class="btn">➕ Nuevo Registro</router-link>
    <table v-if="items.length">
      <thead>
        <tr><th>Paciente</th><th>Temp</th><th>FC</th><th>FR</th><th>Oximetría</th><th>Fecha</th></tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id_vitales">
          <td>{{ item.nombre_paciente }} {{ item.apellido_paciente }}</td>
          <td>{{ item.temperatura }}°C</td>
          <td>{{ item.fCardiaca }}</td>
          <td>{{ item.fRespiratoria }}</td>
          <td>{{ item.oximetria }}%</td>
          <td>{{ new Date(item.fechaHora).toLocaleString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import signosService from "../../services/signos.service";
export default {
  data() {
    return { items: [] };
  },
  async mounted() {
    this.items = await signosService.getAll();
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

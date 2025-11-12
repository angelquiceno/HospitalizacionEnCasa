<template>
  <div class="personal-list">
    <div class="header">
      <h1>Personal de Salud</h1>
      <router-link to="/dashboard/personal/nuevo" class="btn-primary">
        ➕ Nuevo Personal
      </router-link>
    </div>
    <div v-if="loading" class="loading">Cargando...</div>
    <div v-else class="table-container">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Rol</th>
            <th>Especialidad</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="personal in personalList" :key="personal.id_PersonalSalud">
            <td>{{ personal.id_PersonalSalud }}</td>
            <td>{{ personal.usuario?.nombre }} {{ personal.usuario?.apellido }}</td>
            <td>{{ personal.rol }}</td>
            <td>{{ personal.especialidad }}</td>
            <td>
              <router-link :to="`/dashboard/personal/${personal.id_PersonalSalud}`" class="btn-view">
                Ver
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import personalService from "../../services/personal.service";

export default {
  name: "PersonalList",
  data() {
    return {
      personalList: [],
      loading: false,
    };
  },
  async mounted() {
    this.loading = true;
    try {
      this.personalList = await personalService.getAll();
    } catch (error) {
      console.error("Error:", error);
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
.personal-list {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}
h1 {
  margin: 0;
  color: #2c3e50;
}
.btn-primary {
  background: #27ae60;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ecf0f1;
}
th {
  background: #34495e;
  color: white;
}
.btn-view {
  background: #3498db;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  text-decoration: none;
}
</style>

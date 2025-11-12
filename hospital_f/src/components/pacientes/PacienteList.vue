<template>
  <div class="paciente-list">
    <div class="header">
      <h1>Pacientes</h1>
      <router-link to="/dashboard/pacientes/nuevo" class="btn-primary">
        ➕ Nuevo Paciente
      </router-link>
    </div>
    <div v-if="loading" class="loading">Cargando...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="table-container">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Ciudad</th>
            <th>Fecha Nacimiento</th>
            <th>Personal Asignado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="paciente in pacientes" :key="paciente.id_Paciente">
            <td>{{ paciente.id_Paciente }}</td>
            <td>{{ paciente.usuario?.nombre }} {{ paciente.usuario?.apellido }}</td>
            <td>{{ paciente.ciudad }}</td>
            <td>{{ formatDate(paciente.fecha_nacimiento) }}</td>
            <td>{{ paciente.nombre_personal }} {{ paciente.apellido_personal }}</td>
            <td>
              <router-link :to="`/dashboard/pacientes/${paciente.id_Paciente}`" class="btn-view">
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
import pacienteService from "../../services/paciente.service";

export default {
  name: "PacienteList",
  data() {
    return {
      pacientes: [],
      loading: false,
      error: null,
    };
  },
  async mounted() {
    await this.loadPacientes();
  },
  methods: {
    async loadPacientes() {
      this.loading = true;
      this.error = null;
      try {
        this.pacientes = await pacienteService.getAll();
      } catch (error) {
        console.error("Error al cargar pacientes:", error);
        this.error = "Error al cargar los pacientes";
      } finally {
        this.loading = false;
      }
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
  },
};
</script>

<style scoped>
.paciente-list {
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
  transition: background 0.3s;
}
.btn-primary:hover {
  background: #229954;
}
.loading, .error {
  text-align: center;
  padding: 20px;
  font-size: 18px;
}
.error {
  color: #e74c3c;
}
.table-container {
  overflow-x: auto;
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
  font-weight: 600;
}
tr:hover {
  background: #f8f9fa;
}
.btn-view {
  background: #3498db;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  text-decoration: none;
  font-size: 14px;
}
.btn-view:hover {
  background: #2980b9;
}
</style>

<template>
  <div class="paciente-detail">
    <div v-if="loading" class="loading">Cargando...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div class="header">
        <h1>Detalle del Paciente</h1>
        <div class="actions">
          <router-link :to="`/dashboard/pacientes/${paciente.id_Paciente}/editar`" class="btn-edit">
            Editar
          </router-link>
          <button @click="goBack" class="btn-back">Volver</button>
        </div>
      </div>
      <div class="info-card">
        <h2>Información Personal</h2>
        <div class="info-grid">
          <div class="info-item">
            <strong>Nombre:</strong>
            <span>{{ paciente.usuario?.nombre }} {{ paciente.usuario?.apellido }}</span>
          </div>
          <div class="info-item">
            <strong>Dirección:</strong>
            <span>{{ paciente.direccion }}</span>
          </div>
          <div class="info-item">
            <strong>Ciudad:</strong>
            <span>{{ paciente.ciudad }}</span>
          </div>
          <div class="info-item">
            <strong>Fecha de Nacimiento:</strong>
            <span>{{ formatDate(paciente.fecha_nacimiento) }}</span>
          </div>
          <div class="info-item">
            <strong>Personal Asignado:</strong>
            <span>{{ paciente.nombre_personal }} {{ paciente.apellido_personal }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import pacienteService from "../../services/paciente.service";

export default {
  name: "PacienteDetail",
  data() {
    return {
      paciente: null,
      loading: false,
      error: null,
    };
  },
  async mounted() {
    await this.loadPaciente();
  },
  methods: {
    async loadPaciente() {
      this.loading = true;
      this.error = null;
      try {
        this.paciente = await pacienteService.getById(this.$route.params.id);
      } catch (error) {
        console.error("Error al cargar paciente:", error);
        this.error = "Error al cargar el paciente";
      } finally {
        this.loading = false;
      }
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
    goBack() {
      this.$router.push("/dashboard/pacientes");
    },
  },
};
</script>

<style scoped>
.paciente-detail {
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
.actions {
  display: flex;
  gap: 10px;
}
.btn-edit, .btn-back {
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  border: none;
  cursor: pointer;
  font-size: 16px;
}
.btn-edit {
  background: #3498db;
  color: white;
}
.btn-back {
  background: #95a5a6;
  color: white;
}
.info-card {
  background: #f8f9fa;
  padding: 25px;
  border-radius: 8px;
}
.info-card h2 {
  color: #2c3e50;
  margin-bottom: 20px;
}
.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 15px;
}
.info-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.info-item strong {
  color: #7f8c8d;
  font-size: 14px;
}
.info-item span {
  color: #2c3e50;
  font-size: 16px;
}
.loading, .error {
  text-align: center;
  padding: 20px;
  font-size: 18px;
}
.error {
  color: #e74c3c;
}
</style>

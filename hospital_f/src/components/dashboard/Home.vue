<template>
  <div class="home">
    <h1>Bienvenido al Sistema de Hospitalización en Casa</h1>
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">👥</div>
        <div class="stat-info">
          <h3>{{ stats.pacientes }}</h3>
          <p>Pacientes</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">⚕️</div>
        <div class="stat-info">
          <h3>{{ stats.personal }}</h3>
          <p>Personal de Salud</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">📋</div>
        <div class="stat-info">
          <h3>{{ stats.historias }}</h3>
          <p>Historias Clínicas</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">💓</div>
        <div class="stat-info">
          <h3>{{ stats.signos }}</h3>
          <p>Registros de Signos</p>
        </div>
      </div>
    </div>
    <div class="quick-actions">
      <h2>Acciones Rápidas</h2>
      <div class="actions-grid">
        <router-link to="/dashboard/pacientes/nuevo" class="action-btn">
          ➕ Nuevo Paciente
        </router-link>
        <router-link to="/dashboard/signos/nuevo" class="action-btn">
          💓 Registrar Signos Vitales
        </router-link>
        <router-link to="/dashboard/historias/nueva" class="action-btn">
          📋 Nueva Historia Clínica
        </router-link>
        <router-link to="/dashboard/personal/nuevo" class="action-btn">
          ⚕️ Nuevo Personal
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import pacienteService from "../../services/paciente.service";
import personalService from "../../services/personal.service";
import historiaService from "../../services/historia.service";
import signosService from "../../services/signos.service";

export default {
  name: "Home",
  data() {
    return {
      stats: {
        pacientes: 0,
        personal: 0,
        historias: 0,
        signos: 0,
      },
    };
  },
  async mounted() {
    await this.loadStats();
  },
  methods: {
    async loadStats() {
      try {
        const [pacientes, personal, historias, signos] = await Promise.all([
          pacienteService.getAll(),
          personalService.getAll(),
          historiaService.getAll(),
          signosService.getAll(),
        ]);
        this.stats.pacientes = pacientes.length;
        this.stats.personal = personal.length;
        this.stats.historias = historias.length;
        this.stats.signos = signos.length;
      } catch (error) {
        console.error("Error al cargar estadísticas:", error);
      }
    },
  },
};
</script>

<style scoped>
.home {
  max-width: 1200px;
}
h1 {
  color: #2c3e50;
  margin-bottom: 30px;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}
.stat-card {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 15px;
}
.stat-icon {
  font-size: 40px;
}
.stat-info h3 {
  margin: 0;
  font-size: 32px;
  color: #2c3e50;
}
.stat-info p {
  margin: 5px 0 0 0;
  color: #7f8c8d;
}
.quick-actions h2 {
  color: #2c3e50;
  margin-bottom: 20px;
}
.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}
.action-btn {
  background: #3498db;
  color: white;
  padding: 15px 20px;
  border-radius: 8px;
  text-decoration: none;
  text-align: center;
  transition: background-color 0.3s;
  font-size: 16px;
}
.action-btn:hover {
  background: #2980b9;
}
</style>

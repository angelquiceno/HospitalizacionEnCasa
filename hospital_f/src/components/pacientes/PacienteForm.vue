<template>
  <div class="paciente-form">
    <h1>{{ isEdit ? 'Editar' : 'Nuevo' }} Paciente</h1>
    <div v-if="error" class="error">{{ error }}</div>
    <form @submit.prevent="savePaciente">
      <div class="form-group">
        <label>Usuario:</label>
        <select v-model="paciente.id_user" required>
          <option value="">Seleccione usuario</option>
          <option v-for="user in usuarios" :key="user.id_user" :value="user.id_user">
            {{ user.nombre }} {{ user.apellido }} ({{ user.username }})
          </option>
        </select>
      </div>
      <div class="form-group">
        <label>Personal de Salud:</label>
        <select v-model="paciente.id_PersonalSalud" required>
          <option value="">Seleccione personal</option>
          <option v-for="personal in personalSalud" :key="personal.id_PersonalSalud" :value="personal.id_PersonalSalud">
            {{ personal.usuario?.nombre }} {{ personal.usuario?.apellido }} - {{ personal.rol }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label>Dirección:</label>
        <input v-model="paciente.direccion" type="text" required />
      </div>
      <div class="form-group">
        <label>Ciudad:</label>
        <input v-model="paciente.ciudad" type="text" required />
      </div>
      <div class="form-group">
        <label>Fecha de Nacimiento:</label>
        <input v-model="paciente.fecha_nacimiento" type="date" required />
      </div>
      <div class="form-actions">
        <button type="submit" class="btn-primary" :disabled="loading">
          {{ loading ? 'Guardando...' : 'Guardar' }}
        </button>
        <button type="button" @click="goBack" class="btn-secondary">
          Cancelar
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import pacienteService from "../../services/paciente.service";
import personalService from "../../services/personal.service";
import api from "../../services/api";

export default {
  name: "PacienteForm",
  data() {
    return {
      paciente: {
        id_user: "",
        id_PersonalSalud: "",
        direccion: "",
        ciudad: "",
        fecha_nacimiento: "",
      },
      usuarios: [],
      personalSalud: [],
      loading: false,
      error: null,
      isEdit: false,
    };
  },
  async mounted() {
    await this.loadData();
    if (this.$route.params.id) {
      this.isEdit = true;
      await this.loadPaciente();
    }
  },
  methods: {
    async loadData() {
      try {
        const [users, personal] = await Promise.all([
          api.get("/user/"),
          personalService.getAll(),
        ]);
        this.usuarios = users.data;
        this.personalSalud = personal;
      } catch (error) {
        console.error("Error al cargar datos:", error);
      }
    },
    async loadPaciente() {
      try {
        const data = await pacienteService.getById(this.$route.params.id);
        this.paciente = data;
      } catch (error) {
        console.error("Error al cargar paciente:", error);
        this.error = "Error al cargar el paciente";
      }
    },
    async savePaciente() {
      this.loading = true;
      this.error = null;
      try {
        if (this.isEdit) {
          await pacienteService.update(this.$route.params.id, this.paciente);
        } else {
          await pacienteService.create(this.paciente);
        }
        this.$router.push("/dashboard/pacientes");
      } catch (error) {
        console.error("Error al guardar paciente:", error);
        this.error = "Error al guardar el paciente";
      } finally {
        this.loading = false;
      }
    },
    goBack() {
      this.$router.push("/dashboard/pacientes");
    },
  },
};
</script>

<style scoped>
.paciente-form {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
}
h1 {
  color: #2c3e50;
  margin-bottom: 25px;
}
.error {
  background: #f8d7da;
  color: #721c24;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
}
.form-group {
  margin-bottom: 20px;
}
label {
  display: block;
  margin-bottom: 5px;
  color: #2c3e50;
  font-weight: 600;
}
input, select {
  width: 100%;
  padding: 10px;
  border: 1px solid #bdc3c7;
  border-radius: 5px;
  font-size: 16px;
}
.form-actions {
  display: flex;
  gap: 10px;
  margin-top: 25px;
}
.btn-primary, .btn-secondary {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}
.btn-primary {
  background: #27ae60;
  color: white;
}
.btn-primary:hover:not(:disabled) {
  background: #229954;
}
.btn-secondary {
  background: #95a5a6;
  color: white;
}
.btn-secondary:hover {
  background: #7f8c8d;
}
</style>

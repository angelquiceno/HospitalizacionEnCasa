<template>
  <div class="form-container">
    <h1>Registrar Signos Vitales</h1>
    <form @submit.prevent="save">
      <input v-model="form.id_paciente" placeholder="ID Paciente" required />
      <input v-model.number="form.temperatura" type="number" step="0.1" placeholder="Temperatura (°C)" required />
      <input v-model.number="form.fCardiaca" type="number" placeholder="Frecuencia Cardíaca" required />
      <input v-model.number="form.fRespiratoria" type="number" placeholder="Frecuencia Respiratoria" required />
      <input v-model.number="form.oximetria" type="number" step="0.1" placeholder="Oximetría (%)" required />
      <input v-model.number="form.pArterialSistolica" type="number" placeholder="Presión Sistólica" required />
      <input v-model.number="form.pArterialDiastolica" type="number" placeholder="Presión Diastólica" required />
      <input v-model.number="form.glicemias" type="number" step="0.1" placeholder="Glicemia" required />
      <button type="submit">Guardar</button>
    </form>
  </div>
</template>

<script>
import signosService from "../../services/signos.service";
export default {
  data() {
    return {
      form: {
        id_paciente: "",
        temperatura: "",
        fCardiaca: "",
        fRespiratoria: "",
        oximetria: "",
        pArterialSistolica: "",
        pArterialDiastolica: "",
        glicemias: "",
      },
    };
  },
  methods: {
    async save() {
      await signosService.create(this.form);
      this.$router.push("/dashboard/signos");
    },
  },
};
</script>

<style scoped>
.form-container { background: white; padding: 30px; border-radius: 10px; max-width: 600px; }
input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #bdc3c7; border-radius: 5px; }
button { background: #27ae60; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%; margin-top: 10px; }
</style>

<template>
  <div class="form-container">
    <h1>Nueva Historia Clínica</h1>
    <form @submit.prevent="save">
      <input v-model="form.id_paciente" placeholder="ID Paciente" required />
      <textarea v-model="form.diagnostico" placeholder="Diagnóstico" required></textarea>
      <textarea v-model="form.descripcion" placeholder="Descripción" required></textarea>
      <textarea v-model="form.sugerencias" placeholder="Sugerencias"></textarea>
      <input v-model="form.entorno" placeholder="Entorno" />
      <button type="submit">Guardar</button>
    </form>
  </div>
</template>

<script>
import historiaService from "../../services/historia.service";
export default {
  data() {
    return { form: { id_paciente: "", diagnostico: "", descripcion: "", sugerencias: "", entorno: "" } };
  },
  methods: {
    async save() {
      await historiaService.create(this.form);
      this.$router.push("/dashboard/historias");
    },
  },
};
</script>

<style scoped>
.form-container { background: white; padding: 30px; border-radius: 10px; }
input, textarea { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #bdc3c7; border-radius: 5px; }
textarea { min-height: 100px; }
button { background: #27ae60; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
</style>

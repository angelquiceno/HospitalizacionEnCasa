<template>
  <div class="detail-container">
    <h1>Detalle Personal de Salud</h1>
    <div v-if="personal">
      <p><strong>Nombre:</strong> {{ personal.usuario?.nombre }} {{ personal.usuario?.apellido }}</p>
      <p><strong>Rol:</strong> {{ personal.rol }}</p>
      <p><strong>Especialidad:</strong> {{ personal.especialidad }}</p>
      <button @click="$router.push('/dashboard/personal')">Volver</button>
    </div>
  </div>
</template>

<script>
import personalService from "../../services/personal.service";

export default {
  data() {
    return { personal: null };
  },
  async mounted() {
    this.personal = await personalService.getById(this.$route.params.id);
  },
};
</script>

<style scoped>
.detail-container {
  background: white;
  padding: 30px;
  border-radius: 10px;
}
button {
  background: #95a5a6;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}
</style>

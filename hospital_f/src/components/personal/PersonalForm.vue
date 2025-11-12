<template>
  <div class="form-container">
    <h1>Nuevo Personal de Salud</h1>
    <form @submit.prevent="save">
      <input v-model="form.id_user" placeholder="ID Usuario" required />
      <input v-model="form.rol" placeholder="Rol" required />
      <input v-model="form.especialidad" placeholder="Especialidad" required />
      <button type="submit">Guardar</button>
    </form>
  </div>
</template>

<script>
import personalService from "../../services/personal.service";

export default {
  data() {
    return { form: { id_user: "", rol: "", especialidad: "" } };
  },
  methods: {
    async save() {
      await personalService.create(this.form);
      this.$router.push("/dashboard/personal");
    },
  },
};
</script>

<style scoped>
.form-container {
  background: white;
  padding: 30px;
  border-radius: 10px;
}
input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #bdc3c7;
  border-radius: 5px;
}
button {
  background: #27ae60;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>

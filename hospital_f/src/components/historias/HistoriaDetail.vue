<template>
  <div class="detail-container">
    <h1>Detalle Historia Clínica</h1>
    <div v-if="item">
      <p><strong>Diagnóstico:</strong> {{ item.diagnostico }}</p>
      <p><strong>Descripción:</strong> {{ item.descripcion }}</p>
      <p><strong>Sugerencias:</strong> {{ item.sugerencias }}</p>
      <button @click="$router.push('/dashboard/historias')">Volver</button>
    </div>
  </div>
</template>

<script>
import historiaService from "../../services/historia.service";
export default {
  data() {
    return { item: null };
  },
  async mounted() {
    this.item = await historiaService.getById(this.$route.params.id);
  },
};
</script>

<style scoped>
.detail-container { background: white; padding: 30px; border-radius: 10px; }
button { background: #95a5a6; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin-top: 20px; }
</style>

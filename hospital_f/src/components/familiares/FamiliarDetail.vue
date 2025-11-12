<template>
  <div class="detail-container">
    <h1>Detalle Familiar</h1>
    <div v-if="item">
      <p><strong>Email:</strong> {{ item.email }}</p>
      <p><strong>Parentezco:</strong> {{ item.parentezco }}</p>
      <button @click="$router.push('/dashboard/familiares')">Volver</button>
    </div>
  </div>
</template>

<script>
import familiarService from "../../services/familiar.service";
export default {
  data() {
    return { item: null };
  },
  async mounted() {
    this.item = await familiarService.getById(this.$route.params.id);
  },
};
</script>

<style scoped>
.detail-container { background: white; padding: 30px; border-radius: 10px; }
button { background: #95a5a6; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin-top: 20px; }
</style>

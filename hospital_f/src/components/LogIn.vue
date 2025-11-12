<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar sesión</h2>
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
      <form @submit.prevent="processLogInUser">
        <input
          type="text"
          v-model="user.username"
          placeholder="Usuario"
          required
        />
        <br />
        <input
          type="password"
          v-model="user.password"
          placeholder="Contraseña"
          required
        />
        <br />
        <button type="submit" :disabled="loading">
          {{ loading ? "Iniciando..." : "Iniciar Sesión" }}
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import authService from "../services/auth.service";

export default {
  name: "LogIn",
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
      loading: false,
      errorMessage: "",
    };
  },

  methods: {
    async processLogInUser() {
      this.loading = true;
      this.errorMessage = "";

      try {
        await authService.login(this.user.username, this.user.password);
        
        // Obtener información del usuario actual
        const currentUser = await authService.getCurrentUser();
        
        // Emitir evento de login exitoso
        this.$emit("completedLogIn", {
          username: this.user.username,
          user: currentUser,
        });

        // Redirigir al dashboard
        this.$router.push({ name: "dashboard" });
      } catch (error) {
        console.error("Error al iniciar sesión:", error);
        
        if (error.response) {
          if (error.response.status === 401) {
            this.errorMessage = "Usuario o contraseña incorrectos";
          } else if (error.response.status === 400) {
            this.errorMessage = "Por favor complete todos los campos";
          } else {
            this.errorMessage = "Error al iniciar sesión. Intente nuevamente";
          }
        } else if (error.request) {
          this.errorMessage = "No se pudo conectar con el servidor";
        } else {
          this.errorMessage = "Error inesperado. Intente nuevamente";
        }
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container_logIn_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 25%;
  min-width: 300px;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
}
.logIn_user h2 {
  color: #283747;
  margin-bottom: 20px;
}
.error-message {
  background-color: #f8d7da;
  color: #721c24;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
  width: 70%;
  text-align: center;
  border: 1px solid #f5c6cb;
}
.logIn_user form {
  width: 70%;
}
.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
  border-radius: 5px;
}
.logIn_user input:focus {
  outline: none;
  border-color: #5a6c7d;
}
.logIn_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
  cursor: pointer;
  transition: all 0.3s ease;
}
.logIn_user button:hover:not(:disabled) {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
.logIn_user button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
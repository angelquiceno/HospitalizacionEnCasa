<template>
  <div class="signUp_user">
    <div class="container_signUp_user">
      <h2>Registrarse</h2>
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
      <form @submit.prevent="processSignUpUser">
        <input
          type="text"
          v-model="user.username"
          placeholder="Usuario"
          required
        />
        <input
          type="password"
          v-model="user.password"
          placeholder="Contraseña"
          required
          minlength="6"
        />
        <input
          type="password"
          v-model="confirmPassword"
          placeholder="Confirmar Contraseña"
          required
        />
        <input
          type="text"
          v-model="user.nombre"
          placeholder="Nombre"
          required
        />
        <input
          type="text"
          v-model="user.apellido"
          placeholder="Apellido"
          required
        />
        <input
          type="tel"
          v-model="user.telefono"
          placeholder="Teléfono"
          required
        />
        <select v-model="user.perfil" required>
          <option value="" disabled>Seleccione perfil</option>
          <option value="paciente">Paciente</option>
          <option value="familiar">Familiar</option>
          <option value="personal_salud">Personal de Salud</option>
        </select>
        <select v-model="user.genero" required>
          <option value="" disabled>Seleccione género</option>
          <option value="M">Masculino</option>
          <option value="F">Femenino</option>
          <option value="O">Otro</option>
        </select>
        <button type="submit" :disabled="loading">
          {{ loading ? "Registrando..." : "Registrarse" }}
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import authService from "../services/auth.service";

export default {
  name: "SignUp",
  data() {
    return {
      user: {
        username: "",
        password: "",
        nombre: "",
        apellido: "",
        telefono: "",
        perfil: "",
        genero: "",
      },
      confirmPassword: "",
      loading: false,
      errorMessage: "",
    };
  },

  methods: {
    async processSignUpUser() {
      this.errorMessage = "";

      // Validar que las contraseñas coincidan
      if (this.user.password !== this.confirmPassword) {
        this.errorMessage = "Las contraseñas no coinciden";
        return;
      }

      // Validar longitud de contraseña
      if (this.user.password.length < 6) {
        this.errorMessage = "La contraseña debe tener al menos 6 caracteres";
        return;
      }

      this.loading = true;

      try {
        await authService.register(this.user);
        
        // Obtener información del usuario actual
        const currentUser = await authService.getCurrentUser();
        
        // Emitir evento de registro exitoso
        this.$emit("completedSignUp", {
          username: this.user.username,
          user: currentUser,
        });

        // Redirigir al dashboard
        this.$router.push({ name: "dashboard" });
      } catch (error) {
        console.error("Error al registrarse:", error);
        
        if (error.response) {
          if (error.response.status === 400) {
            const errors = error.response.data;
            if (errors.username) {
              this.errorMessage = "El nombre de usuario ya existe";
            } else {
              this.errorMessage = "Por favor verifique los datos ingresados";
            }
          } else {
            this.errorMessage = "Error al registrarse. Intente nuevamente";
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
.signUp_user {
  margin: 0;
  padding: 20px 0;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container_signUp_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 30%;
  min-width: 350px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30px 20px;
}
.signUp_user h2 {
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
.signUp_user form {
  width: 70%;
}
.signUp_user input,
.signUp_user select {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
  border-radius: 5px;
}
.signUp_user input:focus,
.signUp_user select:focus {
  outline: none;
  border-color: #5a6c7d;
}
.signUp_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 10px 0 5px 0;
  cursor: pointer;
  transition: all 0.3s ease;
}
.signUp_user button:hover:not(:disabled) {
  color: #e5e7e9;
  background: #27ae60;
  border: 1px solid #283747;
}
.signUp_user button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>

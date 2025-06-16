<template>
  <div class="login-wrapper">
    <div class="login-card">
      <h2>Iniciar Sesión</h2>
      <p class="subheading">Ingresa tus credenciales para iniciar sesión</p>
      
      <form @submit.prevent="handleLogin">
        <input 
          type="text" 
          class="form-input" 
          placeholder="Dirección de Email *" 
          v-model="username" 
          required 
        />
        <input 
          type="password" 
          class="form-input" 
          placeholder="Contraseña *" 
          v-model="password" 
          required 
        />
        <button type="submit" class="btn-primary">Entrar</button>
        <p v-if="error" class="error-message">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useAuthStore } from '../store/auth';

const username = ref('');
const password = ref('');
const error = ref(null);
const router = useRouter();
const authStore = useAuthStore();

const handleLogin = async () => {
  try {
    error.value = null;
    const response = await axios.post('http://127.0.0.1:8000/api/token/', {
      username: username.value,
      password: password.value,
    });
    authStore.login(response.data.access, response.data.refresh);
    router.push('/');
  } catch (err) {
    error.value = 'Usuario o contraseña incorrectos.';
    console.error('Error de login:', err);
  }
};
</script>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding-top: 5vh;
}
.login-card {
  max-width: 400px;
  width: 100%;
  padding: 2.5rem;
  background-color: var(--white);
  border-radius: 12px;
  box-shadow: var(--shadow);
  text-align: center;
}
h2 {
  font-size: 2rem;
  font-weight: 700;
  color: var(--dark-gray);
  margin-top: 0;
  margin-bottom: 0.5rem;
}
.subheading {
  margin-bottom: 2rem;
  color: var(--text-color);
}
.error-message {
  color: #dc3545;
  margin-top: 1rem;
  font-size: 14px;
}
</style>
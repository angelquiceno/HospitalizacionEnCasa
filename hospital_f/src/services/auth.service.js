import api from './api';

const authService = {
    // Iniciar sesión
    async login(username, password) {
        const response = await api.post('/login/', { username, password });
        const { access, refresh } = response.data;

        // Guardar tokens en localStorage
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        return response.data;
    },

    // Registrar nuevo usuario
    async register(userData) {
        const response = await api.post('/user/', userData);
        const { access, refresh } = response.data;

        // Guardar tokens en localStorage
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        return response.data;
    },

    // Cerrar sesión
    logout() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
    },

    // Obtener usuario actual
    async getCurrentUser() {
        const response = await api.get('/user/me/');
        return response.data;
    },

    // Verificar si el usuario está autenticado
    isAuthenticated() {
        return !!localStorage.getItem('access_token');
    },

    // Obtener token de acceso
    getAccessToken() {
        return localStorage.getItem('access_token');
    },

    // Obtener token de refresco
    getRefreshToken() {
        return localStorage.getItem('refresh_token');
    },
};

export default authService;

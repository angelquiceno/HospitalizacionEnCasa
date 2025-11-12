import api from './api';

const signosService = {
    // Obtener todos los signos vitales
    async getAll() {
        const response = await api.get('/signos/');
        return response.data;
    },

    // Obtener signos vitales por ID
    async getById(id) {
        const response = await api.get(`/signos/${id}/`);
        return response.data;
    },

    // Crear un nuevo registro de signos vitales
    async create(signosData) {
        const response = await api.post('/signos/', signosData);
        return response.data;
    },

    // Actualizar signos vitales
    async update(id, signosData) {
        const response = await api.put(`/signos/${id}/`, signosData);
        return response.data;
    },

    // Actualizar parcialmente signos vitales
    async partialUpdate(id, signosData) {
        const response = await api.patch(`/signos/${id}/`, signosData);
        return response.data;
    },

    // Eliminar signos vitales
    async delete(id) {
        const response = await api.delete(`/signos/${id}/`);
        return response.data;
    },
};

export default signosService;

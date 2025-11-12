import api from './api';

const familiarService = {
    // Obtener todos los familiares
    async getAll() {
        const response = await api.get('/familiar/');
        return response.data;
    },

    // Obtener un familiar por ID
    async getById(id) {
        const response = await api.get(`/familiar/${id}/`);
        return response.data;
    },

    // Crear un nuevo familiar
    async create(familiarData) {
        const response = await api.post('/familiar/', familiarData);
        return response.data;
    },

    // Actualizar un familiar
    async update(id, familiarData) {
        const response = await api.put(`/familiar/${id}/`, familiarData);
        return response.data;
    },

    // Actualizar parcialmente un familiar
    async partialUpdate(id, familiarData) {
        const response = await api.patch(`/familiar/${id}/`, familiarData);
        return response.data;
    },

    // Eliminar un familiar
    async delete(id) {
        const response = await api.delete(`/familiar/${id}/`);
        return response.data;
    },
};

export default familiarService;

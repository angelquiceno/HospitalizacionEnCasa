import api from './api';

const historiaService = {
    // Obtener todas las historias clínicas
    async getAll() {
        const response = await api.get('/historia/');
        return response.data;
    },

    // Obtener una historia clínica por ID
    async getById(id) {
        const response = await api.get(`/historia/${id}/`);
        return response.data;
    },

    // Crear una nueva historia clínica
    async create(historiaData) {
        const response = await api.post('/historia/', historiaData);
        return response.data;
    },

    // Actualizar una historia clínica
    async update(id, historiaData) {
        const response = await api.put(`/historia/${id}/`, historiaData);
        return response.data;
    },

    // Actualizar parcialmente una historia clínica
    async partialUpdate(id, historiaData) {
        const response = await api.patch(`/historia/${id}/`, historiaData);
        return response.data;
    },

    // Eliminar una historia clínica
    async delete(id) {
        const response = await api.delete(`/historia/${id}/`);
        return response.data;
    },
};

export default historiaService;

import api from './api';

const personalService = {
    // Obtener todo el personal de salud
    async getAll() {
        const response = await api.get('/personalSalud/');
        return response.data;
    },

    // Obtener un personal de salud por ID
    async getById(id) {
        const response = await api.get(`/personalSalud/${id}/`);
        return response.data;
    },

    // Crear un nuevo personal de salud
    async create(personalData) {
        const response = await api.post('/personalSalud/', personalData);
        return response.data;
    },

    // Actualizar un personal de salud
    async update(id, personalData) {
        const response = await api.put(`/personalSalud/${id}/`, personalData);
        return response.data;
    },

    // Actualizar parcialmente un personal de salud
    async partialUpdate(id, personalData) {
        const response = await api.patch(`/personalSalud/${id}/`, personalData);
        return response.data;
    },

    // Eliminar un personal de salud
    async delete(id) {
        const response = await api.delete(`/personalSalud/${id}/`);
        return response.data;
    },
};

export default personalService;

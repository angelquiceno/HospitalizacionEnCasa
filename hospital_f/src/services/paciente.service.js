import api from './api';

const pacienteService = {
    // Obtener todos los pacientes
    async getAll() {
        const response = await api.get('/paciente/');
        return response.data;
    },

    // Obtener un paciente por ID
    async getById(id) {
        const response = await api.get(`/paciente/${id}/`);
        return response.data;
    },

    // Crear un nuevo paciente
    async create(pacienteData) {
        const response = await api.post('/paciente/', pacienteData);
        return response.data;
    },

    // Actualizar un paciente
    async update(id, pacienteData) {
        const response = await api.put(`/paciente/${id}/`, pacienteData);
        return response.data;
    },

    // Actualizar parcialmente un paciente
    async partialUpdate(id, pacienteData) {
        const response = await api.patch(`/paciente/${id}/`, pacienteData);
        return response.data;
    },

    // Eliminar un paciente
    async delete(id) {
        const response = await api.delete(`/paciente/${id}/`);
        return response.data;
    },

    // Obtener historias clínicas de un paciente
    async getHistorias(id) {
        const response = await api.get(`/paciente/${id}/historias/`);
        return response.data;
    },

    // Obtener signos vitales de un paciente
    async getSignos(id) {
        const response = await api.get(`/paciente/${id}/signos/`);
        return response.data;
    },

    // Obtener último signo vital de un paciente
    async getUltimoSigno(id) {
        const response = await api.get(`/paciente/${id}/signos/ultimo/`);
        return response.data;
    },
};

export default pacienteService;

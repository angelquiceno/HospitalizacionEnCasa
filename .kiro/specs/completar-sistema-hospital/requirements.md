# Documento de Requisitos

## Introducción

Sistema de Hospitalización en Casa que permite gestionar pacientes, personal de salud, familiares, historias clínicas y signos vitales. El sistema actualmente tiene una implementación parcial con backend Django REST Framework y frontend Vue.js que necesita ser completado y corregido para funcionar correctamente.

## Glosario

- **Sistema**: La aplicación completa de Hospitalización en Casa
- **Backend**: API REST desarrollada en Django REST Framework
- **Frontend**: Aplicación web desarrollada en Vue.js 3
- **Usuario**: Persona que utiliza el sistema (puede ser personal de salud, familiar o paciente)
- **Paciente**: Persona que recibe atención médica en casa
- **Personal de Salud**: Profesional médico que atiende pacientes
- **Familiar**: Persona relacionada con un paciente que puede ver su información
- **Historia Clínica**: Registro médico del paciente
- **Signos Vitales**: Mediciones médicas del paciente (temperatura, presión arterial, etc.)
- **Token JWT**: Token de autenticación JSON Web Token
- **API Endpoint**: Ruta URL del backend que expone funcionalidad

## Requisitos

### Requisito 1: Autenticación y Gestión de Usuarios

**Historia de Usuario:** Como usuario del sistema, quiero poder registrarme e iniciar sesión de forma segura, para acceder a las funcionalidades según mi perfil.

#### Criterios de Aceptación

1. WHEN un usuario envía credenciales válidas al endpoint de login, THE Sistema SHALL generar y retornar tokens JWT de acceso y refresco
2. WHEN un usuario intenta registrarse con un username único, THE Sistema SHALL crear la cuenta y almacenar la contraseña de forma segura usando hash
3. WHEN un usuario intenta acceder a un endpoint protegido sin token válido, THE Sistema SHALL retornar error 401 no autorizado
4. THE Sistema SHALL permitir actualizar información de perfil de usuario autenticado
5. THE Sistema SHALL validar que el username sea único antes de crear un usuario

### Requisito 2: Gestión de Personal de Salud

**Historia de Usuario:** Como administrador del sistema, quiero gestionar el personal de salud, para mantener un registro actualizado de los profesionales disponibles.

#### Criterios de Aceptación

1. WHEN se crea un personal de salud, THE Sistema SHALL asociarlo con un usuario existente y almacenar su rol y especialidad
2. THE Sistema SHALL permitir listar todo el personal de salud registrado
3. THE Sistema SHALL permitir obtener detalles de un personal de salud específico por su ID
4. THE Sistema SHALL permitir actualizar información de un personal de salud existente
5. WHEN se elimina un personal de salud, THE Sistema SHALL remover el registro manteniendo la integridad referencial

### Requisito 3: Gestión de Pacientes

**Historia de Usuario:** Como personal de salud, quiero registrar y gestionar pacientes, para llevar un control de las personas bajo mi cuidado.

#### Criterios de Aceptación

1. WHEN se registra un paciente, THE Sistema SHALL asociarlo con un usuario y un personal de salud responsable
2. THE Sistema SHALL almacenar dirección, ciudad y fecha de nacimiento del paciente
3. THE Sistema SHALL permitir listar todos los pacientes asignados a un personal de salud
4. THE Sistema SHALL permitir actualizar información de un paciente existente
5. THE Sistema SHALL permitir obtener detalles completos de un paciente por su ID

### Requisito 4: Gestión de Familiares

**Historia de Usuario:** Como personal de salud, quiero registrar familiares de pacientes, para mantener contactos de emergencia y personas autorizadas.

#### Criterios de Aceptación

1. WHEN se registra un familiar, THE Sistema SHALL asociarlo con un usuario y un paciente específico
2. THE Sistema SHALL almacenar email y parentesco del familiar
3. THE Sistema SHALL permitir listar todos los familiares de un paciente
4. THE Sistema SHALL permitir actualizar información de un familiar existente
5. THE Sistema SHALL validar que el email tenga formato válido

### Requisito 5: Gestión de Historias Clínicas

**Historia de Usuario:** Como personal de salud, quiero crear y consultar historias clínicas de pacientes, para documentar diagnósticos y tratamientos.

#### Criterios de Aceptación

1. WHEN se crea una historia clínica, THE Sistema SHALL asociarla con un paciente y registrar fecha y hora automáticamente
2. THE Sistema SHALL almacenar diagnóstico, sugerencias, descripción y entorno del paciente
3. THE Sistema SHALL permitir listar todas las historias clínicas de un paciente ordenadas por fecha
4. THE Sistema SHALL permitir obtener detalles de una historia clínica específica
5. THE Sistema SHALL permitir actualizar una historia clínica existente

### Requisito 6: Gestión de Signos Vitales

**Historia de Usuario:** Como personal de salud, quiero registrar signos vitales de pacientes, para monitorear su estado de salud en tiempo real.

#### Criterios de Aceptación

1. WHEN se registran signos vitales, THE Sistema SHALL asociarlos con un paciente y registrar fecha y hora automáticamente
2. THE Sistema SHALL almacenar oximetría, frecuencia respiratoria, frecuencia cardíaca, temperatura, presión arterial y glicemia
3. THE Sistema SHALL permitir listar todos los signos vitales de un paciente ordenados por fecha
4. THE Sistema SHALL validar que los valores numéricos estén en rangos médicamente válidos
5. THE Sistema SHALL permitir obtener el último registro de signos vitales de un paciente

### Requisito 7: Interfaz de Usuario Frontend

**Historia de Usuario:** Como usuario del sistema, quiero una interfaz web intuitiva, para interactuar fácilmente con todas las funcionalidades.

#### Criterios de Aceptación

1. THE Frontend SHALL proporcionar formularios de login y registro de usuarios
2. THE Frontend SHALL mostrar diferentes vistas según el perfil del usuario autenticado
3. WHEN un usuario inicia sesión exitosamente, THE Frontend SHALL almacenar tokens JWT y redirigir al dashboard
4. THE Frontend SHALL proporcionar navegación entre módulos de pacientes, personal, familiares, historias y signos vitales
5. THE Frontend SHALL mostrar mensajes de error claros cuando las operaciones fallen

### Requisito 8: Configuración y Despliegue

**Historia de Usuario:** Como desarrollador, quiero que el proyecto tenga configuración adecuada, para poder ejecutarlo en desarrollo y producción.

#### Criterios de Aceptación

1. THE Sistema SHALL incluir archivo README con instrucciones de instalación y ejecución
2. THE Backend SHALL usar variables de entorno para configuración sensible en lugar de valores hardcodeados
3. THE Sistema SHALL incluir archivo .gitignore para excluir archivos sensibles y dependencias
4. THE Backend SHALL tener configuración separada para desarrollo y producción
5. THE Sistema SHALL incluir scripts de inicialización de base de datos con datos de prueba

### Requisito 9: Validación y Manejo de Errores

**Historia de Usuario:** Como usuario del sistema, quiero recibir mensajes claros cuando algo falla, para entender qué corregir.

#### Criterios de Aceptación

1. WHEN se envían datos inválidos a un endpoint, THE Backend SHALL retornar error 400 con descripción del problema
2. WHEN se intenta acceder a un recurso inexistente, THE Backend SHALL retornar error 404
3. THE Backend SHALL validar todos los campos requeridos antes de crear o actualizar registros
4. THE Frontend SHALL mostrar mensajes de validación en formularios antes de enviar datos
5. THE Sistema SHALL registrar errores en logs para facilitar debugging

### Requisito 10: Endpoints API Completos

**Historia de Usuario:** Como desarrollador frontend, quiero endpoints REST completos y consistentes, para implementar todas las funcionalidades en la interfaz.

#### Criterios de Aceptación

1. THE Backend SHALL exponer endpoints CRUD completos para todas las entidades (Usuario, Paciente, Personal, Familiar, Historia, Signos)
2. THE Backend SHALL seguir convenciones REST para nombres de rutas y métodos HTTP
3. THE Backend SHALL retornar respuestas en formato JSON consistente
4. THE Backend SHALL incluir endpoints para listar con filtros y paginación
5. THE Backend SHALL documentar todos los endpoints disponibles

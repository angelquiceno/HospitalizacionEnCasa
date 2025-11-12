# Guía de Sustentación - Sistema de Hospitalización en Casa

## 📋 Índice
1. [Visión General del Proyecto](#visión-general)
2. [Arquitectura del Sistema](#arquitectura)
3. [Backend - Django REST Framework](#backend)
4. [Frontend - Vue.js](#frontend)
5. [Flujo de Autenticación](#autenticación)
6. [Módulos Principales](#módulos)
7. [Preguntas Frecuentes en Entrevistas](#preguntas-frecuentes)

---

## 🎯 Visión General del Proyecto {#visión-general}

### ¿Qué es este proyecto?
Es un **sistema web full-stack** para gestionar la hospitalización de pacientes en sus casas. Permite registrar pacientes, asignar personal de salud, registrar familiares responsables, llevar historias clínicas y monitorear signos vitales.

### ¿Por qué es importante?
- Reduce costos hospitalarios
- Permite atención personalizada en casa
- Facilita el seguimiento médico remoto
- Mejora la calidad de vida del paciente

### Tecnologías Utilizadas
- **Backend**: Django 4.2 + Django REST Framework + JWT
- **Frontend**: Vue.js 3 + Vue Router + Axios
- **Base de Datos**: SQLite (desarrollo) - fácil migrar a PostgreSQL/MySQL
- **Autenticación**: JSON Web Tokens (JWT)

---

## 🏗️ Arquitectura del Sistema {#arquitectura}

### Patrón Arquitectónico: Cliente-Servidor con API REST

```
┌─────────────────┐         HTTP/JSON          ┌─────────────────┐
│                 │ ◄────────────────────────► │                 │
│  Frontend       │      API REST Calls        │   Backend       │
│  (Vue.js)       │                            │   (Django)      │
│  Puerto 8080    │                            │   Puerto 8000   │
│                 │                            │                 │
└─────────────────┘                            └────────┬────────┘
                                                        │
                                                        ▼
                                                ┌───────────────┐
                                                │   SQLite DB   │
                                                └───────────────┘
```

### ¿Por qué esta arquitectura?
- **Separación de responsabilidades**: Frontend maneja UI, Backend maneja lógica y datos
- **Escalabilidad**: Puedes cambiar el frontend sin tocar el backend
- **Reutilización**: La API puede ser usada por apps móviles, otros clientes
- **Mantenibilidad**: Equipos diferentes pueden trabajar en cada parte

---

## 🔧 Backend - Django REST Framework {#backend}

### Estructura del Backend

```
Hospital_be/
├── appHospital/              # Aplicación principal
│   ├── models/               # Modelos de datos (tablas DB)
│   │   ├── user.py          # Usuario con autenticación
│   │   ├── Paciente.py      # Datos del paciente
│   │   ├── PersonalSalud.py # Médicos, enfermeros
│   │   ├── Familiar.py      # Familiares responsables
│   │   ├── HistoriaClinica.py
│   │   └── SignosVitales.py
│   ├── serializers/          # Conversión datos ↔ JSON
│   ├── views/                # Lógica de endpoints API
│   └── migrations/           # Cambios en la BD
└── projectHospital/
    ├── settings.py           # Configuración
    └── urls.py               # Rutas de la API
```

### Modelos de Datos (Base de Datos)

#### 1. **ClaseUser** - Sistema de Usuarios
```python
- username: nombre de usuario único
- password: contraseña hasheada (seguridad)
- perfil: admin | personal_salud | familiar | paciente
- nombre, apellido, telefono, genero
- is_active: si el usuario está activo
```

**¿Por qué es importante?**
- Usa `AbstractBaseUser` de Django para autenticación robusta
- Las contraseñas se hashean automáticamente (nunca se guardan en texto plano)
- Diferentes perfiles tienen diferentes permisos

#### 2. **ClasePaciente** - Información del Paciente
```python
- id_paciente: identificador único
- nombre, apellido, edad, direccion
- telefono, genero
- user: relación con usuario (ForeignKey)
```

**Relación**: Un usuario puede ser un paciente

#### 3. **ClasePersonalSalud** - Médicos y Enfermeros
```python
- id_personal: identificador único
- nombre, apellido, especialidad
- telefono, genero
- user: relación con usuario
```

**Relación**: Un usuario puede ser personal de salud

#### 4. **ClaseFamiliar** - Familiares Responsables
```python
- id_familiar: identificador único
- nombre, apellido, parentezco
- telefono, email
- paciente: relación con paciente (ForeignKey)
```

**Relación**: Un familiar está asociado a un paciente

#### 5. **ClaseHistoriaClinica** - Historial Médico
```python
- id_historia: identificador único
- fecha: fecha de registro
- diagnostico: diagnóstico médico
- tratamiento: tratamiento prescrito
- observaciones: notas adicionales
- paciente: relación con paciente
- personal_salud: quién registró
```

**Relación**: Muchas historias por paciente, registradas por personal

#### 6. **ClaseSignosVitales** - Monitoreo de Salud
```python
- id_signos: identificador único
- fecha: fecha y hora del registro
- presion_arterial: ej. "120/80"
- frecuencia_cardiaca: pulsaciones por minuto
- temperatura: en grados Celsius
- frecuencia_respiratoria: respiraciones por minuto
- saturacion_oxigeno: porcentaje
- paciente: relación con paciente
```

**Relación**: Múltiples registros de signos por paciente

### API REST Endpoints

#### Autenticación
```
POST /login/              → Iniciar sesión (obtener tokens JWT)
POST /refresh/            → Refrescar token de acceso
POST /user/               → Registrar nuevo usuario
GET  /user/me/            → Obtener datos del usuario actual
```

#### Usuarios
```
GET    /user/             → Listar todos los usuarios
POST   /user/             → Crear usuario
GET    /user/{id}/        → Ver detalle de usuario
PUT    /user/{id}/        → Actualizar usuario
DELETE /user/{id}/        → Eliminar usuario
```

#### Pacientes
```
GET    /paciente/         → Listar pacientes
POST   /paciente/         → Crear paciente
GET    /paciente/{id}/    → Ver detalle
PUT    /paciente/{id}/    → Actualizar
DELETE /paciente/{id}/    → Eliminar
```

#### Personal de Salud
```
GET    /personalSalud/         → Listar personal
POST   /personalSalud/         → Crear personal
GET    /personalSalud/{id}/    → Ver detalle
PUT    /personalSalud/{id}/    → Actualizar
DELETE /personalSalud/{id}/    → Eliminar
```

#### Familiares
```
GET    /familiar/         → Listar familiares
POST   /familiar/         → Crear familiar
GET    /familiar/{id}/    → Ver detalle
PUT    /familiar/{id}/    → Actualizar
DELETE /familiar/{id}/    → Eliminar
```

#### Historias Clínicas
```
GET    /historia/                        → Listar historias
POST   /historia/                        → Crear historia
GET    /historia/{id}/                   → Ver detalle
PUT    /historia/{id}/                   → Actualizar
DELETE /historia/{id}/                   → Eliminar
GET    /paciente/{id}/historias/         → Historias de un paciente
```

#### Signos Vitales
```
GET    /signos/                          → Listar signos
POST   /signos/                          → Crear registro
GET    /signos/{id}/                     → Ver detalle
PUT    /signos/{id}/                     → Actualizar
DELETE /signos/{id}/                     → Eliminar
GET    /paciente/{id}/signos/            → Signos de un paciente
GET    /paciente/{id}/signos/ultimo/     → Último registro
```

### Serializers - ¿Qué son y por qué?

Los **serializers** convierten objetos Python (modelos) a JSON y viceversa.

**Ejemplo**: ClaseUsarioSerializer
```python
# Entrada JSON del frontend:
{
  "username": "juan123",
  "password": "mipassword",
  "nombre": "Juan",
  "apellido": "Pérez"
}

# El serializer:
# 1. Valida los datos
# 2. Hashea la contraseña
# 3. Crea el objeto en la BD
# 4. Retorna JSON sin la contraseña
```

**Ventajas**:
- Validación automática de datos
- Seguridad (no exponer campos sensibles)
- Transformación de datos

---

## 🎨 Frontend - Vue.js {#frontend}

### Estructura del Frontend

```
hospital_f/
├── src/
│   ├── components/           # Componentes Vue
│   │   ├── LogIn.vue        # Pantalla de login
│   │   ├── SignUp.vue       # Registro de usuarios
│   │   ├── Navbar.vue       # Barra de navegación
│   │   ├── Sidebar.vue      # Menú lateral
│   │   ├── Dashboard.vue    # Panel principal
│   │   ├── Home.vue         # Página de inicio
│   │   ├── pacientes/       # Módulo de pacientes
│   │   │   ├── PacienteList.vue
│   │   │   ├── PacienteForm.vue
│   │   │   └── PacienteDetail.vue
│   │   ├── personal/        # Módulo de personal
│   │   ├── familiares/      # Módulo de familiares
│   │   ├── historias/       # Módulo de historias
│   │   └── signos/          # Módulo de signos vitales
│   ├── services/            # Servicios API
│   │   ├── api.js          # Cliente Axios base
│   │   ├── auth.service.js # Autenticación
│   │   ├── paciente.service.js
│   │   └── ...
│   ├── router/
│   │   └── index.js        # Rutas y guards
│   ├── App.vue             # Componente raíz
│   └── main.js             # Punto de entrada
└── package.json
```

### Componentes Principales

#### 1. **LogIn.vue** - Inicio de Sesión
- Formulario con username y password
- Llama a `authService.login()`
- Guarda tokens JWT en localStorage
- Redirige al dashboard si es exitoso
- Muestra errores al usuario

#### 2. **SignUp.vue** - Registro
- Formulario completo con todos los campos
- Valida que las contraseñas coincidan
- Llama a `authService.register()`
- Automáticamente inicia sesión después del registro

#### 3. **Navbar.vue** - Barra Superior
- Muestra nombre del usuario logueado
- Botón de cerrar sesión
- Navegación principal

#### 4. **Sidebar.vue** - Menú Lateral
- Enlaces a todos los módulos
- Solo visible cuando estás logueado

#### 5. **Dashboard.vue** - Panel Principal
- Contenedor que incluye Navbar y Sidebar
- Muestra el contenido según la ruta

### Servicios API

#### api.js - Cliente Base
```javascript
// Configuración de Axios
const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' }
});

// Interceptor: agrega token a cada petición
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Interceptor: maneja errores 401 (no autorizado)
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      // Token expirado, redirigir a login
      localStorage.removeItem('access_token');
      router.push('/login');
    }
    return Promise.reject(error);
  }
);
```

**¿Por qué interceptores?**
- Evita repetir código en cada petición
- Manejo centralizado de autenticación
- Manejo centralizado de errores

#### auth.service.js - Autenticación
```javascript
async login(username, password) {
  // POST /login/
  const response = await api.post('/login/', { username, password });
  
  // Guardar tokens
  localStorage.setItem('access_token', response.data.access);
  localStorage.setItem('refresh_token', response.data.refresh);
  
  return response.data;
}

async register(userData) {
  // POST /user/
  const response = await api.post('/user/', userData);
  
  // Guardar tokens (auto-login)
  localStorage.setItem('access_token', response.data.access);
  localStorage.setItem('refresh_token', response.data.refresh);
  
  return response.data;
}

logout() {
  // Limpiar tokens
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
}
```

### Router - Navegación y Protección

```javascript
const routes = [
  { path: '/login', component: LogIn },
  { path: '/signup', component: SignUp },
  {
    path: '/dashboard',
    component: Dashboard,
    meta: { requiresAuth: true },  // Requiere autenticación
    children: [
      { path: '', component: Home },
      { path: 'pacientes', component: PacienteList },
      // ... más rutas
    ]
  }
];

// Navigation Guard: protege rutas
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = authService.isAuthenticated();
  
  if (requiresAuth && !isAuthenticated) {
    next('/login');  // Redirigir a login
  } else {
    next();  // Permitir navegación
  }
});
```

**¿Qué hace el guard?**
- Verifica si la ruta requiere autenticación
- Verifica si el usuario tiene token válido
- Redirige a login si no está autenticado

---

## 🔐 Flujo de Autenticación {#autenticación}

### ¿Qué es JWT (JSON Web Token)?

Es un **token** (cadena de texto) que contiene información del usuario de forma segura.

**Estructura de un JWT**:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1YW4ifQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

Header.Payload.Signature
```

- **Header**: tipo de token y algoritmo
- **Payload**: datos del usuario (id, username, etc.)
- **Signature**: firma digital para verificar autenticidad

### Flujo Completo de Login

```
1. Usuario ingresa username y password
   ↓
2. Frontend envía POST /login/ con credenciales
   ↓
3. Backend verifica credenciales en la BD
   ↓
4. Si son correctas, genera 2 tokens:
   - access_token (válido 5 min)
   - refresh_token (válido 1 día)
   ↓
5. Frontend guarda tokens en localStorage
   ↓
6. En cada petición, Frontend envía:
   Authorization: Bearer {access_token}
   ↓
7. Backend verifica el token
   ↓
8. Si es válido, procesa la petición
   Si expiró, Frontend usa refresh_token para obtener nuevo access_token
```

### ¿Por qué 2 tokens?

- **Access Token**: corta duración (5 min) - más seguro
- **Refresh Token**: larga duración (1 día) - para renovar access token

Si roban el access token, solo es útil 5 minutos.

---

## 📦 Módulos Principales {#módulos}

### Módulo de Pacientes

**Funcionalidades**:
- Listar todos los pacientes
- Ver detalle de un paciente
- Crear nuevo paciente
- Editar información
- Eliminar paciente

**Componentes**:
- `PacienteList.vue`: tabla con todos los pacientes
- `PacienteForm.vue`: formulario crear/editar
- `PacienteDetail.vue`: vista detallada con historias y signos

**Flujo de Creación**:
```
1. Usuario hace clic en "Nuevo Paciente"
2. Se muestra PacienteForm.vue
3. Usuario llena el formulario
4. Al enviar, llama a pacienteService.create()
5. Service hace POST /paciente/ con los datos
6. Backend valida y guarda en BD
7. Retorna el paciente creado
8. Frontend muestra mensaje de éxito
9. Redirige a la lista de pacientes
```

### Módulo de Historias Clínicas

**Funcionalidades**:
- Ver historias de un paciente específico
- Crear nueva historia clínica
- Editar historia existente
- Ver detalle completo

**Relaciones**:
- Una historia pertenece a un paciente
- Una historia es creada por personal de salud

**Datos importantes**:
- Fecha de registro
- Diagnóstico médico
- Tratamiento prescrito
- Observaciones adicionales

### Módulo de Signos Vitales

**Funcionalidades**:
- Registrar signos vitales de un paciente
- Ver historial de signos
- Ver último registro
- Visualizar evolución (lista cronológica)

**Signos que se registran**:
- Presión arterial (ej. 120/80)
- Frecuencia cardíaca (pulsaciones/min)
- Temperatura (°C)
- Frecuencia respiratoria (respiraciones/min)
- Saturación de oxígeno (%)

**Importancia**:
Permite monitorear la evolución del paciente en casa y detectar anomalías.

---

## ❓ Preguntas Frecuentes en Entrevistas {#preguntas-frecuentes}

### Sobre el Proyecto

**P: ¿Por qué elegiste Django y Vue.js?**
R: Django porque tiene un ORM potente, autenticación integrada y Django REST Framework facilita crear APIs. Vue.js porque es progresivo, fácil de aprender y tiene excelente documentación. La combinación permite desarrollo rápido y mantenible.

**P: ¿Cómo manejas la seguridad?**
R: 
- Contraseñas hasheadas con PBKDF2 (algoritmo de Django)
- Autenticación JWT con tokens de corta duración
- CORS configurado para permitir solo el frontend
- Validaciones en backend (nunca confiar solo en frontend)
- Tokens en localStorage (alternativa: httpOnly cookies)

**P: ¿Qué es una API REST?**
R: Es una interfaz que permite comunicación entre sistemas usando HTTP. Usa métodos estándar (GET, POST, PUT, DELETE) y retorna datos en JSON. Es stateless (sin estado), cada petición es independiente.

**P: ¿Qué es un ORM?**
R: Object-Relational Mapping. Permite trabajar con la base de datos usando objetos Python en lugar de SQL directo. Django ORM traduce automáticamente operaciones Python a consultas SQL.

Ejemplo:
```python
# Con ORM (Django)
pacientes = ClasePaciente.objects.filter(edad__gte=18)

# SQL equivalente
SELECT * FROM paciente WHERE edad >= 18;
```

**P: ¿Cómo funciona la relación entre modelos?**
R: Uso ForeignKey para relaciones uno-a-muchos:
- Un paciente tiene muchas historias clínicas
- Un paciente tiene muchos registros de signos vitales
- Un familiar está asociado a un paciente

Django maneja automáticamente las relaciones y permite consultas como:
```python
paciente.clasehistoriaclinica_set.all()  # Todas las historias del paciente
```

### Sobre el Código

**P: ¿Qué son los serializers?**
R: Son clases que convierten objetos Python a JSON (serialización) y JSON a objetos Python (deserialización). También validan datos de entrada y manejan relaciones entre modelos.

**P: ¿Qué son los interceptores de Axios?**
R: Son funciones que se ejecutan antes de enviar una petición o después de recibir una respuesta. Los uso para:
- Agregar automáticamente el token JWT a cada petición
- Manejar errores 401 (token expirado) de forma centralizada
- Evitar código repetitivo

**P: ¿Qué son los navigation guards?**
R: Son funciones en Vue Router que se ejecutan antes de navegar a una ruta. Los uso para proteger rutas que requieren autenticación, redirigiendo a login si el usuario no está autenticado.

**P: ¿Cómo manejas errores?**
R: 
- Backend: try-catch en vistas, retorno códigos HTTP apropiados (400, 401, 404, 500)
- Frontend: try-catch en servicios, mensajes de error al usuario, interceptores para errores globales

### Sobre Mejoras Futuras

**P: ¿Qué mejorarías del proyecto?**
R:
- Migrar a PostgreSQL para producción
- Agregar tests unitarios y de integración
- Implementar paginación en listas largas
- Agregar gráficas para visualizar signos vitales
- Implementar notificaciones en tiempo real (WebSockets)
- Agregar roles y permisos más granulares
- Implementar recuperación de contraseña por email
- Agregar búsqueda y filtros avanzados
- Dockerizar la aplicación para fácil despliegue

**P: ¿Cómo escalarías este proyecto?**
R:
- Usar PostgreSQL con índices en campos frecuentes
- Implementar caché con Redis
- Separar backend en microservicios si crece mucho
- Usar CDN para archivos estáticos del frontend
- Implementar balanceador de carga
- Agregar monitoreo y logs centralizados

---

## 🎓 Conceptos Clave para Recordar

### Backend
- **Django**: Framework web de Python
- **REST API**: Interfaz de comunicación usando HTTP y JSON
- **ORM**: Mapeo objeto-relacional para trabajar con BD
- **JWT**: Tokens para autenticación sin sesiones
- **Serializers**: Conversión y validación de datos
- **Migrations**: Control de versiones de la base de datos

### Frontend
- **Vue.js**: Framework progresivo de JavaScript
- **SPA**: Single Page Application (no recarga la página)
- **Components**: Piezas reutilizables de UI
- **Router**: Navegación entre vistas
- **Axios**: Cliente HTTP para llamadas API
- **Interceptors**: Middleware para peticiones HTTP

### Arquitectura
- **Cliente-Servidor**: Separación frontend/backend
- **API REST**: Comunicación estandarizada
- **JWT**: Autenticación stateless
- **CRUD**: Create, Read, Update, Delete

---

## 💡 Consejos para la Entrevista

1. **Sé honesto**: Si te preguntan algo que no sabes, admítelo y muestra interés en aprender

2. **Explica el flujo**: Cuando hables de una funcionalidad, explica el flujo completo desde el usuario hasta la base de datos

3. **Menciona decisiones técnicas**: "Elegí JWT porque es stateless y escalable"

4. **Habla de lo que aprendiste**: "Este proyecto me enseñó sobre autenticación, APIs REST y arquitectura cliente-servidor"

5. **Prepara una demo**: Ten el proyecto corriendo para mostrar funcionalidades

6. **Conoce las limitaciones**: "Es un proyecto académico, en producción usaría PostgreSQL y agregaría tests"

7. **Muestra entusiasmo**: Habla con pasión sobre lo que construiste

---

## 📚 Recursos para Profundizar

- **Django**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Vue.js**: https://vuejs.org/guide/
- **JWT**: https://jwt.io/introduction
- **REST API**: https://restfulapi.net/

---

¡Éxito en tu entrevista! 🚀

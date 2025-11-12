# Documento de Diseño - Sistema de Hospitalización en Casa

## Visión General

El sistema es una aplicación web full-stack que permite gestionar la atención médica domiciliaria. Utiliza Django REST Framework para el backend API y Vue.js 3 para el frontend SPA. La arquitectura sigue el patrón cliente-servidor con autenticación JWT.

## Arquitectura

### Arquitectura General

```
┌─────────────────┐         HTTP/REST          ┌──────────────────┐
│                 │ ◄─────────────────────────► │                  │
│  Vue.js 3 SPA   │      JSON + JWT Tokens      │  Django REST API │
│   (Frontend)    │                             │    (Backend)     │
│                 │                             │                  │
└─────────────────┘                             └────────┬─────────┘
                                                         │
                                                         │ ORM
                                                         ▼
                                                ┌─────────────────┐
                                                │   PostgreSQL    │
                                                │    Database     │
                                                └─────────────────┘
```

### Stack Tecnológico

**Backend:**
- Django 4.1
- Django REST Framework 3.13.1
- djangorestframework-simplejwt 5.2.0 (autenticación JWT)
- PostgreSQL (base de datos)
- django-cors-headers 3.13.0 (CORS)

**Frontend:**
- Vue.js 3.2.13
- Vue Router 4.0.3
- Axios 0.27.2 (cliente HTTP)

## Componentes y Interfaces

### Backend - Modelos de Datos

#### 1. ClaseUser (Usuario Base)
```python
- id_user: AutoField (PK)
- username: CharField(45) UNIQUE
- password: CharField(256) HASHED
- perfil: CharField(45) # 'personal_salud', 'familiar', 'paciente'
- nombre: CharField(45)
- apellido: CharField(45)
- telefono: CharField(45)
- genero: CharField(45)
```

**Mejoras necesarias:**
- Agregar validación de email
- Implementar choices para perfil y género
- Agregar campo is_active
- Mejorar el hash de contraseñas (eliminar salt hardcodeado)

#### 2. clasePersonalSalud
```python
- id_PersonalSalud: AutoField (PK)
- id_user: ForeignKey(ClaseUser)
- rol: CharField(45) # 'medico', 'enfermero', 'terapeuta'
- especialidad: CharField(45)
```

**Mejoras necesarias:**
- Agregar choices para rol
- Validar que el usuario tenga perfil 'personal_salud'

#### 3. ClasePaciente
```python
- id_Paciente: AutoField (PK)
- id_PersonalSalud: ForeignKey(clasePersonalSalud)
- id_user: ForeignKey(ClaseUser)
- direccion: CharField(45)
- ciudad: CharField(45)
- fecha_nacimiento: DateField
```

**Mejoras necesarias:**
- Aumentar max_length de dirección
- Agregar validación de edad
- Validar que el usuario tenga perfil 'paciente'

#### 4. ClaseFamiliar
```python
- id_Familiar: AutoField (PK)
- id_user: ForeignKey(ClaseUser)
- id_Paciente: ForeignKey(ClasePaciente)
- email: CharField(45)
- parentezco: CharField(45)
```

**Mejoras necesarias:**
- Cambiar email a EmailField
- Agregar choices para parentezco
- Validar que el usuario tenga perfil 'familiar'

#### 5. ClaseHistoriaClinica
```python
- id_HistoriaClinica: AutoField (PK)
- id_paciente: ForeignKey(ClasePaciente)
- sugerencias: CharField(30)
- diagnostico: CharField(30)
- entorno: CharField(30)
- fecha: DateTimeField
- descripcion: CharField(30)
```

**Mejoras necesarias:**
- Aumentar max_length de todos los campos de texto (usar TextField)
- Agregar auto_now_add=True para fecha
- Agregar campo de personal que registra

#### 6. ClaseSignosVitales
```python
- id_vitales: AutoField (PK)
- id_paciente: ForeignKey(ClasePaciente)
- oximetria: FloatField
- fRespiratoria: FloatField
- fCardiaca: FloatField
- temperatura: FloatField
- pArterial: FloatField
- glicemias: FloatField
- fechaHora: DateTimeField(auto_now_add)
```

**Mejoras necesarias:**
- Agregar validadores de rango para cada signo vital
- Separar presión arterial en sistólica y diastólica

### Backend - Serializers

Cada modelo necesita un serializer completo con:
- Campos de solo lectura para IDs y timestamps
- Validaciones personalizadas
- Representación anidada de relaciones cuando sea apropiado
- Métodos create y update si requieren lógica especial

### Backend - Views y Endpoints

#### Endpoints Actuales (Incompletos)
```
POST   /login/                    # Login JWT
POST   /refresh/                  # Refresh token
POST   /user/                     # Crear usuario
GET    /user/<id>                 # Detalle usuario
POST   /paciente/                 # Crear paciente
GET    /paciente/<id>/            # Detalle paciente
POST   /personalSalud/            # Crear personal
GET    /personalSalud/<id>        # Detalle personal
```

#### Endpoints Faltantes a Implementar
```
# Usuarios
GET    /user/                     # Listar usuarios
PUT    /user/<id>/                # Actualizar usuario
DELETE /user/<id>/                # Eliminar usuario
GET    /user/me/                  # Usuario actual

# Pacientes
GET    /paciente/                 # Listar pacientes
PUT    /paciente/<id>/            # Actualizar paciente
DELETE /paciente/<id>/            # Eliminar paciente

# Personal de Salud
GET    /personalSalud/            # Listar personal
PUT    /personalSalud/<id>/       # Actualizar personal
DELETE /personalSalud/<id>/       # Eliminar personal

# Familiares (completamente faltante)
GET    /familiar/                 # Listar familiares
POST   /familiar/                 # Crear familiar
GET    /familiar/<id>/            # Detalle familiar
PUT    /familiar/<id>/            # Actualizar familiar
DELETE /familiar/<id>/            # Eliminar familiar

# Historias Clínicas (completamente faltante)
GET    /historia/                 # Listar historias
POST   /historia/                 # Crear historia
GET    /historia/<id>/            # Detalle historia
PUT    /historia/<id>/            # Actualizar historia
DELETE /historia/<id>/            # Eliminar historia
GET    /paciente/<id>/historias/  # Historias de un paciente

# Signos Vitales (completamente faltante)
GET    /signos/                   # Listar signos
POST   /signos/                   # Crear signos
GET    /signos/<id>/              # Detalle signos
PUT    /signos/<id>/              # Actualizar signos
DELETE /signos/<id>/              # Eliminar signos
GET    /paciente/<id>/signos/     # Signos de un paciente
GET    /paciente/<id>/signos/ultimo/  # Último registro
```

### Frontend - Componentes

#### Estructura de Componentes Propuesta

```
src/
├── App.vue                      # Componente raíz (ya existe)
├── main.js                      # Entry point (ya existe)
├── router.js                    # Configuración de rutas (necesita expansión)
├── components/
│   ├── auth/
│   │   ├── LogIn.vue           # Ya existe (necesita corrección)
│   │   └── SignUp.vue          # FALTA - Registro de usuarios
│   ├── layout/
│   │   ├── Navbar.vue          # FALTA - Barra de navegación
│   │   └── Sidebar.vue         # FALTA - Menú lateral
│   ├── dashboard/
│   │   ├── Dashboard.vue       # FALTA - Vista principal
│   │   └── Home.vue            # FALTA - Página de inicio
│   ├── pacientes/
│   │   ├── PacienteList.vue    # FALTA - Lista de pacientes
│   │   ├── PacienteForm.vue    # FALTA - Formulario crear/editar
│   │   └── PacienteDetail.vue  # FALTA - Detalle de paciente
│   ├── personal/
│   │   ├── PersonalList.vue    # FALTA - Lista de personal
│   │   ├── PersonalForm.vue    # FALTA - Formulario crear/editar
│   │   └── PersonalDetail.vue  # FALTA - Detalle de personal
│   ├── familiares/
│   │   ├── FamiliarList.vue    # FALTA - Lista de familiares
│   │   ├── FamiliarForm.vue    # FALTA - Formulario crear/editar
│   │   └── FamiliarDetail.vue  # FALTA - Detalle de familiar
│   ├── historias/
│   │   ├── HistoriaList.vue    # FALTA - Lista de historias
│   │   ├── HistoriaForm.vue    # FALTA - Formulario crear/editar
│   │   └── HistoriaDetail.vue  # FALTA - Detalle de historia
│   └── signos/
│       ├── SignosForm.vue      # FALTA - Formulario registrar signos
│       ├── SignosList.vue      # FALTA - Lista de signos vitales
│       └── SignosChart.vue     # FALTA - Gráfica de evolución
└── services/
    ├── api.js                   # FALTA - Cliente API base
    ├── auth.service.js          # FALTA - Servicio de autenticación
    ├── paciente.service.js      # FALTA - Servicio de pacientes
    ├── personal.service.js      # FALTA - Servicio de personal
    ├── familiar.service.js      # FALTA - Servicio de familiares
    ├── historia.service.js      # FALTA - Servicio de historias
    └── signos.service.js        # FALTA - Servicio de signos vitales
```

## Modelos de Datos

### Diagrama de Relaciones

```
┌──────────────┐
│  ClaseUser   │
│              │
│ - id_user    │
│ - username   │
│ - password   │
│ - perfil     │
│ - nombre     │
│ - apellido   │
└──────┬───────┘
       │
       │ 1:1
       ├─────────────────────────────────┐
       │                                 │
       ▼                                 ▼
┌──────────────────┐            ┌─────────────────┐
│ clasePersonalSalud│            │  ClaseFamiliar  │
│                  │            │                 │
│ - id_PersonalSalud│            │ - id_Familiar   │
│ - rol            │            │ - email         │
│ - especialidad   │            │ - parentezco    │
└────────┬─────────┘            └────────┬────────┘
         │                               │
         │ 1:N                           │ N:1
         ▼                               │
┌──────────────────┐                     │
│  ClasePaciente   │◄────────────────────┘
│                  │
│ - id_Paciente    │
│ - direccion      │
│ - ciudad         │
│ - fecha_nacimiento│
└────────┬─────────┘
         │
         │ 1:N
         ├──────────────────┐
         ▼                  ▼
┌──────────────────┐  ┌──────────────────┐
│ClaseHistoriaClinica│  │ClaseSignosVitales│
│                  │  │                  │
│ - diagnostico    │  │ - oximetria      │
│ - sugerencias    │  │ - fRespiratoria  │
│ - descripcion    │  │ - fCardiaca      │
│ - fecha          │  │ - temperatura    │
└──────────────────┘  │ - pArterial      │
                      │ - glicemias      │
                      │ - fechaHora      │
                      └──────────────────┘
```

## Manejo de Errores

### Backend
- Usar excepciones de DRF (ValidationError, NotFound, PermissionDenied)
- Implementar exception handler personalizado
- Retornar respuestas consistentes:
```json
{
  "error": "Descripción del error",
  "details": { "campo": ["mensaje de validación"] }
}
```

### Frontend
- Interceptor de Axios para manejar errores globalmente
- Mostrar mensajes de error en UI
- Manejar errores 401 redirigiendo a login
- Manejar errores de red

## Estrategia de Testing

### Backend
- Tests unitarios para modelos (validaciones)
- Tests de serializers (validación de datos)
- Tests de endpoints (CRUD completo)
- Tests de autenticación JWT
- Usar Django TestCase y APITestCase

### Frontend
- Tests unitarios de componentes (opcional)
- Tests de integración de servicios (opcional)
- Tests E2E de flujos principales (opcional)

## Seguridad

### Implementaciones Necesarias

1. **Autenticación:**
   - JWT con tokens de acceso (5 min) y refresco (1 día)
   - Almacenar tokens en localStorage
   - Interceptor para agregar token a requests

2. **Autorización:**
   - Permisos basados en perfil de usuario
   - Personal de salud puede ver sus pacientes
   - Familiares solo ven su paciente asignado
   - Pacientes ven su propia información

3. **Validación:**
   - Validar todos los inputs en backend
   - Sanitizar datos antes de guardar
   - Validar tipos de datos y rangos

4. **Configuración:**
   - Mover SECRET_KEY a variable de entorno
   - Mover credenciales de BD a variables de entorno
   - Configurar ALLOWED_HOSTS para producción
   - Deshabilitar DEBUG en producción

## Configuración y Despliegue

### Variables de Entorno Necesarias

```env
# Backend
SECRET_KEY=<django-secret-key>
DEBUG=False
DATABASE_URL=<postgresql-url>
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8080

# Frontend
VUE_APP_API_URL=http://localhost:8000
```

### Archivos de Configuración Necesarios

1. **.env.example** - Template de variables de entorno
2. **.gitignore** - Excluir archivos sensibles
3. **README.md** - Documentación completa
4. **requirements.txt** - Ya existe, puede necesitar actualizaciones

### Scripts de Inicialización

1. Script para crear superusuario
2. Script para cargar datos de prueba
3. Script para ejecutar migraciones

## Mejoras de Código Existente

### Problemas Identificados

1. **LogIn.vue** - URL hardcodeada incorrecta:
```javascript
// Actual (INCORRECTO):
axios.post("https://bank-be-luis.herokuapp.com/login/", ...)

// Debe ser:
axios.post("http://localhost:8000/login/", ...)
// O mejor: usar variable de entorno
```

2. **settings.py** - Credenciales hardcodeadas:
```python
# Mover a variables de entorno
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
```

3. **user.py** - Salt hardcodeado:
```python
# Eliminar salt hardcodeado, Django maneja esto automáticamente
def save(self, **kwargs):
    if not self.pk:  # Solo hashear si es nuevo
        self.password = make_password(self.password)
    super().save(**kwargs)
```

4. **router.js** - Configuración incompleta:
```javascript
// Falta configurar rutas para todos los módulos
// Falta guards de autenticación
```

5. **URLs faltantes** - Muchos endpoints no están registrados en urls.py

## Flujos de Usuario Principales

### 1. Registro e Inicio de Sesión
```
Usuario → Formulario Registro → POST /user/ → Crear cuenta
Usuario → Formulario Login → POST /login/ → Recibir tokens → Guardar en localStorage → Redirigir a Dashboard
```

### 2. Gestión de Pacientes (Personal de Salud)
```
Personal → Dashboard → Ver lista pacientes → GET /paciente/
Personal → Crear paciente → Formulario → POST /paciente/ → Actualizar lista
Personal → Ver detalle → GET /paciente/<id>/ → Mostrar info completa
Personal → Registrar signos vitales → Formulario → POST /signos/ → Actualizar historial
Personal → Crear historia clínica → Formulario → POST /historia/ → Guardar registro
```

### 3. Consulta de Información (Familiar)
```
Familiar → Login → Dashboard → Ver paciente asignado → GET /paciente/<id>/
Familiar → Ver historias clínicas → GET /paciente/<id>/historias/
Familiar → Ver signos vitales → GET /paciente/<id>/signos/
```

## Prioridades de Implementación

### Fase 1: Correcciones Críticas
1. Corregir URL del backend en LogIn.vue
2. Mover credenciales a variables de entorno
3. Corregir hash de contraseñas en modelo User
4. Completar endpoints faltantes en urls.py

### Fase 2: Completar Backend
1. Implementar vistas faltantes (Familiar, Historia, Signos)
2. Agregar métodos PUT y DELETE a vistas existentes
3. Mejorar validaciones en modelos y serializers
4. Implementar permisos y autorización

### Fase 3: Completar Frontend
1. Crear servicios API
2. Implementar componente SignUp
3. Crear Dashboard y navegación
4. Implementar módulos de gestión (Pacientes, Personal, etc.)
5. Agregar guards de autenticación en router

### Fase 4: Mejoras y Documentación
1. Agregar README completo
2. Crear archivos .env.example y .gitignore
3. Implementar manejo de errores robusto
4. Agregar validaciones en frontend
5. Mejorar UI/UX
